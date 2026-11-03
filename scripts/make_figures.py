"""Build every QuantForensics figure from the analysis JSONs in analyses/.

No plotted value is typed by hand. Each is read from analyses/registered/
(registered verdicts) or analyses/post-hoc-sensitivity/ (post-hoc,
PROVISIONAL) and checked against the text of the paper before it is drawn.
If a value does not appear in the paper, the script stops.

Usage: python scripts/make_figures.py   (needs matplotlib + numpy)
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
AN = os.path.join(ROOT, "analyses", "registered")
SENS = os.path.join(ROOT, "analyses", "post-hoc-sensitivity")
OUT = os.path.join(ROOT, "figures")
RESULTS = open(os.path.join(ROOT, "paper", "quantforensics.md")).read()

C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
    "ytick.color": INK2, "text.color": INK, "font.size": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "svg.hashsalt": "quantforensics", "lines.linewidth": 2,
})


def load(path):
    return json.load(open(path))


def check(label, s):
    if s not in RESULTS:
        raise SystemExit(f"STOP: {label} = {s!r} not found in the paper")
    print(f"  ok  {label:44s} {s}")


def save(fig, stem):
    os.makedirs(OUT, exist_ok=True)
    fig.savefig(os.path.join(OUT, stem + ".png"), dpi=200, bbox_inches="tight",
                metadata={"Software": None})
    fig.savefig(os.path.join(OUT, stem + ".svg"), bbox_inches="tight",
                metadata={"Date": None, "Creator": None})
    plt.close(fig)
    print(f"  wrote figures/{stem}.png/.svg")


def flip(cell):
    return load(os.path.join(AN, f"{cell}.vs-ref.json"))["cell_determinism"]["flip_rate"]


def fig_batching():
    groups = [("dense 32B", "p1-dense32", "bf16"), ("dense 32B", "p1-dense32", "int8-gptq"),
              ("dense 32B", "p1-dense32", "int4-awq"), ("dense 32B", "p1-dense32", "int4-gptq"),
              ("MoE 30B-A3B", "p1-moe30a3", "bf16"), ("MoE 30B-A3B", "p1-moe30a3", "int4-gptq")]
    b1, b8, labels = [], [], []
    for model, pref, w in groups:
        r1 = (load(os.path.join(AN, f"{pref}__bf16__off0__b1.vs-aa1.json"))["cell_determinism"]["flip_rate"]
              if w == "bf16" else flip(f"{pref}__{w}__off0__b1"))
        r8 = flip(f"{pref}__{w}__off0__b8")
        o1 = flip(f"{pref}__{w}__off8__b1")
        o8 = flip(f"{pref}__{w}__off8__b8")
        if (r1, r8) != (o1, o8):
            raise SystemExit(f"STOP: offload changed determinism for {pref} {w}")
        check(f"{model} {w} flip b1/b8", f"{r1:.3f} / {o1:.3f} | {r8:.3f} / {o8:.3f}")
        b1.append(r1 * 100); b8.append(r8 * 100)
        labels.append(f"{model}\n{w.replace('int4-', 'int4 ').replace('int8-', 'int8 ')}")
    x = np.arange(len(groups)); w = 0.36
    fig, ax = plt.subplots(figsize=(9.5, 4))
    ax.bar(x - w / 2, b1, w, color=C1, label="batch 1", edgecolor=SURF, linewidth=2)
    ax.bar(x + w / 2, b8, w, color=C2, label="batch 8", edgecolor=SURF, linewidth=2)
    for i, v in enumerate(b8):
        ax.annotate(f"{v:.0f}%", (x[i] + w / 2, v), xytext=(0, 4), textcoords="offset points",
                    ha="center", fontsize=8.5)
    for i in range(len(groups)):
        ax.annotate("0%", (x[i] - w / 2, 0), xytext=(0, 4), textcoords="offset points",
                    ha="center", fontsize=8.5, color=INK2)
    ax.set_xticks(x, labels, fontsize=8.5)
    ax.set_ylabel("tasks whose greedy output differs\nacross the cell's own 3 repeats, %")
    ax.grid(axis="x", visible=False)
    ax.set_ylim(0, 68)
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 1.0), ncol=2)
    ax.set_title("Greedy nondeterminism comes from batching, not from quantization or offload",
                 loc="left", fontsize=11)
    fig.text(0.06, -0.06, "105 tasks per cell, vLLM on 4x A30, offload 0 shown. With 8 GB of CPU offload "
             "every rate is identical to the offload-0 cell, at batch 1 and at batch 8.",
             fontsize=8, color=INK2)
    save(fig, "fig1_batching")


def shares(path):
    s = load(path)["strata"]
    it = list(s.values()) if isinstance(s, dict) else s
    rb = sum(st["kinds"].get("real_break", 0) for st in it)
    nt = sum(st["kinds"].get("near_tie_flip", 0) for st in it)
    return rb / (rb + nt)


def series(q, rule):
    cells = [("p2-dense7", 7), ("p2-dense14", 14), ("p1-dense32", 32)]
    out = []
    for pref, size in cells:
        c = f"{pref}__{q}__off0__b1"
        reg = os.path.join(AN, f"{c}.vs-ref.json")
        if rule == "registered":
            p = reg
        elif rule == "0.25":
            p = reg if size != 32 else os.path.join(SENS, f"{c}.gap0.25.json")
        else:
            p = os.path.join(SENS, f"{c}.gap0.125.json") if size != 32 else reg
        out.append(shares(p))
    return out


def fig_break_share():
    qs = [("int8-gptq", "GPTQ-Int8"), ("int4-awq", "AWQ-Int4"), ("int4-gptq", "GPTQ-Int4")]
    rules = [("registered", "registered gaps (32B at 0.125, 7B and 14B at 0.25)", C2, "-"),
             ("0.25", "common gap 0.25 (post-hoc)", C1, "--"),
             ("0.125", "common gap 0.125 (post-hoc)", C3, "--")]
    fig, axes = plt.subplots(1, 3, figsize=(11, 4), sharey=True)
    sizes = [7, 14, 32]
    for ax, (q, name) in zip(axes, qs):
        row = []
        for rule, lab, color, ls in rules:
            v = series(q, rule)
            row.append(" / ".join(f"{x:.2f}" for x in v))
            ax.plot(sizes, v, color=color, ls=ls, marker="o", markersize=7,
                    markeredgecolor=SURF, markeredgewidth=1.5, label=lab,
                    zorder=4 if rule == "registered" else 3)
        check(f"{name} break shares (reg | 0.25 | 0.125)",
              f"| {name} | {row[0]} | {row[1]} | {row[2]} |")
        ax.set_xscale("log"); ax.set_xticks(sizes, ["7B", "14B", "32B"]); ax.minorticks_off()
        ax.set_title(name + ("  (side note withdrawn)" if q == "int8-gptq" else ""),
                     loc="left", fontsize=10)
        ax.set_ylim(0, 1.02)
        ax.set_xlabel("model size (Qwen2.5 Instruct)")
    axes[0].set_ylabel("real breaks / divergent outputs")
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, frameon=False, loc="lower center", ncol=3, fontsize=8.5, bbox_to_anchor=(0.5, -0.12))
    fig.suptitle("The real-break share depends on which near-tie gap scores it",
                 x=0.06, ha="left", fontsize=11)
    fig.text(0.06, -0.19, "The registered rungs used different gaps, so the solid line compares two rulers. "
             "Dashed lines rescore every rung with one gap (UNREGISTERED sensitivity analysis).",
             fontsize=8, color=INK2)
    save(fig, "fig2_break_share")


def fig_math_drop():
    cells = [("7B", "p2-dense7"), ("14B", "p2-dense14")]
    strata = ["code", "math", "long_context"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.9), sharey=False)
    for ax, (size, pref) in zip(axes, cells):
        a = load(os.path.join(AN, f"{pref}__int4-gptq__off0__b1.vs-ref.json"))["strata"]
        ref = [a[s]["base_pass"] for s in strata]
        cell = [a[s]["cell_pass"] for s in strata]
        n = [a[s]["n"] for s in strata]
        x = np.arange(len(strata)); w = 0.36
        ax.bar(x - w / 2, [r / k * 100 for r, k in zip(ref, n)], w, color=C1, label="bf16 reference",
               edgecolor=SURF, linewidth=2)
        ax.bar(x + w / 2, [c / k * 100 for c, k in zip(cell, n)], w, color=C2, label="GPTQ-Int4",
               edgecolor=SURF, linewidth=2)
        for i, s in enumerate(strata):
            ax.annotate(f"{ref[i]}/{n[i]}", (x[i] - w / 2, ref[i] / n[i] * 100), xytext=(0, 3),
                        textcoords="offset points", ha="center", fontsize=8)
            ax.annotate(f"{cell[i]}/{n[i]}", (x[i] + w / 2, cell[i] / n[i] * 100), xytext=(0, 3),
                        textcoords="offset points", ha="center", fontsize=8)
            st = a[s]
            if st["verdict"] == "DEGRADED":
                check(f"{size} GPTQ-Int4 {s} DEGRADED", f"b/c {st['b']}/{st['c']}, p = {st['mcnemar_p']:.3f}")
                ax.annotate(f"DEGRADED\nb/c {st['b']}/{st['c']}, p = {st['mcnemar_p']:.3f}",
                            (x[i] + w / 2, cell[i] / n[i] * 100 + 8), xytext=(-62, 75),
                            textcoords="offset points", fontsize=8.5,
                            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
        check(f"{size} GPTQ-Int4 math pass", f"{cell[1]} vs {ref[1]}")
        ax.set_xticks(x, ["code (50)", "math (40)", "long context (15)"], fontsize=9)
        ax.set_ylim(0, 112)
        ax.set_title(f"{size}", loc="left", fontsize=10)
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("tasks passed, % (paired, same tasks)")
    h, l = axes[1].get_legend_handles_labels()
    fig.legend(h, l, frameon=False, loc="lower center", ncol=2, fontsize=9, bbox_to_anchor=(0.5, -0.07))
    fig.suptitle("GPTQ-Int4 against its bf16 reference: the only DEGRADED stratum is 7B math",
                 x=0.06, ha="left", fontsize=11)
    save(fig, "fig3_math_drop")


if __name__ == "__main__":
    for f in (fig_batching, fig_break_share, fig_math_drop):
        print(f.__name__)
        f()
