# p1-moe30a3/bf16/off8/b8  vs  p1-moe30a3/bf16/off0/b1

status: **REGISTERED** (A2)
law 1 (same weights): reference
hosts: cell ['node-d'], baseline ['node-c']
determinism: cell flip rate 0.571 (60/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 42 [0.71,0.92] | 42 [0.71,0.92] | 0/0 | 1 | identical 33, near_tie_flip 6, real_break 11 | no detectable change |
| math | 40 | 33 [0.68,0.91] | 32 [0.65,0.90] | 1/2 | 1 | identical 7, near_tie_flip 9, real_break 24 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 12, real_break 3 | no detectable change |

worst stratum (gates, law 7): code
