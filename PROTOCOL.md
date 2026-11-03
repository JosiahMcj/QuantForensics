# QuantForensics PROTOCOL (laws registered 2026-09-25, before any run)

Spec: `DESIGN.md`. Laws only. Thresholds (near-tie gap, score margins,
reference flip rate) come from the bf16 reference's own A/A' runs and are
added as dated, append-only amendments BEFORE the results they govern.

## Laws

1. **Same weights.** Every quantized cell is a quantization of the exact
   reference checkpoint (sha256 recorded). A quant built from a different
   revision is a different experiment.
2. **Reference noise is the floor.** A quantized cell "degrades" a stratum
   only when its drop exceeds the reference's own A/A' spread on that
   stratum. Differences inside the floor are reported as "no detectable
   change", never as "lossless".
3. **Separate the confound first.** No claim that quantization causes
   nondeterminism until the offload x batching factorial shows the effect
   survives with offload off and batch 1.
4. **Determinism is measured, not assumed.** Every cell gets exact greedy
   repeats; output hashes are compared. The bf16 reference is measured the
   same way; if IT flips, that rate is the floor.
5. **Classify every divergence.** A differing greedy output gets a
   first-divergence token and the reference's top-1/top-2 logprob gap
   there. Below the registered near-tie gap = benign flip; above = real
   break. Unclassified divergences block the verdict.
6. **Send every sampling param**.
7. **Per-sample outcomes, worst task gates**.
8. **Size cap is stated.** Any result on a model without a bf16 reference
   is labelled quant-vs-quant.
9. **Known positive.** Each detector (divergence, vocab integrity) must
   fire on a planted defect before its negatives count.

## Amendments

- **A1 2026-09-26 -- dense reference floor (p1-dense32, Qwen2.5-32B-Instruct
  bf16, vLLM 0.29.0 TP4).** Registered from the reference's own A/A'
  (2 loads on two different nodes, 3 exact repeats each, all 105 tasks, BEFORE any
  P1 cell was analysed). Evidence: 0
  within-load flips, 0 cross-load flips, per-stratum pass spread 0.000
  (code 0.88, math 0.625, long_context 1.0). Because the spread is exactly
  0, law 2's floor is replaced for this reference by: a stratum DEGRADES
  only when discordant tasks favour the reference (b > c) with exact
  two-sided McNemar p < **alpha = 0.05**. **near_tie_gap = 0.125** (the
  reference's p1 token gap; bf16 logprobs come in 0.125 steps, so with the
  strict `gap < near_tie_gap` test only EXACT reference ties count as
  benign flips). Thresholds file: `thresholds.A1.json`.
- **A2 2026-09-26 -- MoE reference floor (p1-moe30a3, Qwen3-30B-A3B bf16,
  thinking=false, vLLM 0.29.0 TP4).** Same procedure and rule as A1. Evidence:
  0 within-load and 0 cross-load flips; spread 0.000 (code 0.84, math 0.8,
  long_context 1.0). **alpha = 0.05; near_tie_gap = 0.25** (reference p1 gap:
  gaps of 0.0 and 0.125 count as benign). Thresholds file:
  `thresholds.A2.json`.
- **A3 2026-10-29 -- P2 PRE-REGISTRATION: the size ladder (registered
  before any P2 run, install, or download).**
  - *Question.* Does quantization damage grow as the model shrinks? P1
    covered one dense size (32B) and found no stratum DEGRADED. P2 asks the
    same question at 7B and 14B in the same family.
  - *Design.* Plans `p2-dense7.plan.json` (TP1) and
    `p2-dense14.plan.json` (TP2), derived mechanically from
    `p1-dense.plan.json`: every held and decode knob identical to P1
    except tensor_parallel. Weights per size: bf16 reference,
    GPTQ-Int8, AWQ-Int4, GPTQ-Int4, all official Qwen releases of
    Qwen2.5-{7B,14B}-Instruct (law 1, checked on HF 2026-10-29). Batch 1,
    offload 0 only: P1 showed batching, not quantization, moves
    determinism, so b1/off0 isolates the quantization effect (law 3 is
    already satisfied by P1). 3 exact repeats per cell, all 105 tasks,
    frozen suite unchanged. 8 cells.
  - *Floors.* Each new bf16 reference gets its own A/A' (2 loads x 3
    repeats) and its floor is registered as A4 (7B) and A5 (14B) BEFORE
    any P2 cell of that size is analysed, by the same rule as A1: if the
    reference spread is 0, a stratum DEGRADES only when discordant tasks
    favour the reference (b > c) at exact two-sided McNemar p < 0.05, and
    near_tie_gap = that reference's p1 token gap. If a spread is NONZERO,
    law 2 applies as written and the floor is that spread.
  - *Primary outcome.* Per (size, quant, stratum): DEGRADED / no detectable
    change, against the same-size bf16 reference. Secondary: per cell, the
    divergence rate and the fraction of divergences that are real breaks
    (reference gap >= near_tie_gap).
  - *Predictions, registered now so they can fail.* (P2.1) int8 shows no
    detectable change on any stratum at either size. (P2.2) int4
    real-break fraction is higher at 7B than at 14B than at 32B (monotone
    in size). (P2.3) math is the first stratum to reach DEGRADED, if any
    does (P1's watched cell). A non-monotone (P2.2) result is reported as
    a refutation, not explained away.
  - *32B rung.* The 32B points come from P1's b1/off0 cells only if their
    instrument run-hash equals the P2 run-hash. Otherwise the 32B rung is
    re-run under P2 and the P1 numbers are not mixed in.
  - *Power, stated up front.* n = 50/40/15 per stratum (code/math/long
    context). A null is "no detectable change at this n", never
    "lossless". A 5-point math drop is inside what this suite resolves.

- **A5 2026-10-30 -- 14B reference floor (p2-dense14, Qwen2.5-14B-Instruct
  bf16, vLLM 0.29.0 TP2).** Registered from the reference's own A/A'
  (2 loads, jobs 12340 + 12341, 3 exact repeats each, all 105 tasks) BEFORE
  any P2 14B cell had run, under the rule A3 pre-specified (the A1 rule). Evidence: within-load flip rates 0.0 and
  0.0, 0 cross-load flips, per-stratum pass spread 0.000 (code 0.78, math
  0.625, long_context 1.0). Spread is exactly 0, so a stratum DEGRADES only
  when discordant tasks favour the reference (b > c) with exact two-sided
  McNemar p < **alpha = 0.05**. **near_tie_gap = 0.25** (the reference's
  p1 token gap, 0.2499999). Thresholds file:
  `thresholds.A5.json`. (A4, the 7B floor, follows when its
  second A/A' load finishes.)
- **A4 2026-10-30 -- 7B reference floor (p2-dense7, Qwen2.5-7B-Instruct
  bf16, vLLM 0.29.0 TP1).** Registered from the reference's own A/A'
  (2 loads, jobs 12342 + 12343, 3 exact repeats each, all 105 tasks) BEFORE
  any P2 7B cell had run, under the rule A3 pre-specified. Evidence:
  within-load flip rates 0.0 and 0.0, 0 cross-load flips, per-stratum pass
  spread 0.000 (code 0.78, math 0.425, long_context 1.0). Spread is exactly
  0, so a stratum DEGRADES only when discordant tasks favour the reference
  (b > c) with exact two-sided McNemar p < **alpha = 0.05**.
  **near_tie_gap = 0.25** (the reference's p1 token gap). Thresholds file:
  `thresholds.A4.json`.
