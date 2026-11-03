# p2-dense14/int4-gptq/off0/b1  vs  p2-dense14/bf16/off0/b1

status: **REGISTERED** (A5)
law 1 (same weights): declared-only (published quant; source revision not verifiable)
hosts: cell ['node-e'], baseline ['node-e']
determinism: cell flip rate 0.000 (0/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 34 [0.54,0.79] | 39 [0.65,0.87] | 8/3 | 0.227 | identical 2, near_tie_flip 3, real_break 45 | no detectable change |
| math | 40 | 19 [0.33,0.63] | 25 [0.47,0.76] | 8/2 | 0.109 | near_tie_flip 15, real_break 25 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 14, real_break 1 | no detectable change |

worst stratum (gates, law 7): math
