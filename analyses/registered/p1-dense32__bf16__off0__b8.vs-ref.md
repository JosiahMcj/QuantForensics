# p1-dense32/bf16/off0/b8  vs  p1-dense32/bf16/off0/b1

status: **REGISTERED** (A1)
law 1 (same weights): reference
hosts: cell ['node-b'], baseline ['node-a']
determinism: cell flip rate 0.505 (53/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 43 [0.74,0.93] | 44 [0.76,0.94] | 1/0 | 1 | identical 34, near_tie_flip 4, real_break 12 | no detectable change |
| math | 40 | 26 [0.50,0.78] | 25 [0.47,0.76] | 1/2 | 1 | identical 7, near_tie_flip 15, real_break 18 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 15 | no detectable change |

worst stratum (gates, law 7): code
