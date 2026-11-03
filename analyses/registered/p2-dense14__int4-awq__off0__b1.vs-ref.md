# p2-dense14/int4-awq/off0/b1  vs  p2-dense14/bf16/off0/b1

status: **REGISTERED** (A5)
law 1 (same weights): declared-only (published quant; source revision not verifiable)
hosts: cell ['node-e'], baseline ['node-e']
determinism: cell flip rate 0.000 (0/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 37 [0.60,0.84] | 39 [0.65,0.87] | 4/2 | 0.688 | identical 2, near_tie_flip 6, real_break 42 | no detectable change |
| math | 40 | 21 [0.37,0.67] | 25 [0.47,0.76] | 7/3 | 0.344 | near_tie_flip 5, real_break 35 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 15 | no detectable change |

worst stratum (gates, law 7): math
