# p1-moe30a3/int4-gptq/off0/b1  vs  p1-moe30a3/bf16/off0/b1

status: **REGISTERED** (A2)
law 1 (same weights): declared-only (published quant; source revision not verifiable)
hosts: cell ['node-c'], baseline ['node-c']
determinism: cell flip rate 0.000 (0/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 43 [0.74,0.93] | 42 [0.71,0.92] | 2/3 | 1 | identical 16, near_tie_flip 3, real_break 31 | no detectable change |
| math | 40 | 29 [0.57,0.84] | 32 [0.65,0.90] | 5/2 | 0.453 | identical 1, near_tie_flip 4, real_break 35 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 7, near_tie_flip 1, real_break 7 | no detectable change |

worst stratum (gates, law 7): math
