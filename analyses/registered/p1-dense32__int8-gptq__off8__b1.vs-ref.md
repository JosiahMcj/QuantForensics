# p1-dense32/int8-gptq/off8/b1  vs  p1-dense32/bf16/off0/b1

status: **REGISTERED** (A1)
law 1 (same weights): declared-only (published quant; source revision not verifiable)
hosts: cell ['node-c'], baseline ['node-a']
determinism: cell flip rate 0.000 (0/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 41 [0.69,0.90] | 44 [0.76,0.94] | 3/0 | 0.25 | identical 34, near_tie_flip 4, real_break 12 | no detectable change |
| math | 40 | 27 [0.52,0.80] | 25 [0.47,0.76] | 1/3 | 0.625 | identical 13, near_tie_flip 11, real_break 16 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 15 | no detectable change |

worst stratum (gates, law 7): code
