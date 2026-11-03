# p2-dense7/int4-gptq/off0/b1  vs  p2-dense7/bf16/off0/b1

status: **REGISTERED** (A4)
law 1 (same weights): declared-only (published quant; source revision not verifiable)
hosts: cell ['node-e'], baseline ['node-e']
determinism: cell flip rate 0.000 (0/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 39 [0.65,0.87] | 39 [0.65,0.87] | 2/2 | 1 | identical 2, near_tie_flip 4, real_break 44 | no detectable change |
| math | 40 | 7 [0.09,0.32] | 17 [0.29,0.58] | 12/2 | 0.0129 | near_tie_flip 9, real_break 31 | DEGRADED |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 2, real_break 13 | no detectable change |

worst stratum (gates, law 7): math
