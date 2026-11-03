# p1-dense32/int4-awq/off0/b1  vs  p1-dense32/bf16/off0/b1

status: **REGISTERED** (A1)
law 1 (same weights): declared-only (published quant; source revision not verifiable)
hosts: cell ['node-a'], baseline ['node-a']
determinism: cell flip rate 0.000 (0/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 42 [0.71,0.92] | 44 [0.76,0.94] | 3/1 | 0.625 | identical 8, near_tie_flip 1, real_break 41 | no detectable change |
| math | 40 | 26 [0.50,0.78] | 25 [0.47,0.76] | 2/3 | 1 | identical 1, near_tie_flip 8, real_break 31 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 15 | no detectable change |

worst stratum (gates, law 7): code
