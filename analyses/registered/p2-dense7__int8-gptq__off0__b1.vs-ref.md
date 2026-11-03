# p2-dense7/int8-gptq/off0/b1  vs  p2-dense7/bf16/off0/b1

status: **REGISTERED** (A4)
law 1 (same weights): declared-only (published quant; source revision not verifiable)
hosts: cell ['node-e'], baseline ['node-e']
determinism: cell flip rate 0.000 (0/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 38 [0.63,0.86] | 39 [0.65,0.87] | 1/0 | 1 | identical 32, near_tie_flip 13, real_break 5 | no detectable change |
| math | 40 | 16 [0.26,0.55] | 17 [0.29,0.58] | 1/0 | 1 | identical 20, near_tie_flip 16, real_break 4 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 14, real_break 1 | no detectable change |

worst stratum (gates, law 7): math
