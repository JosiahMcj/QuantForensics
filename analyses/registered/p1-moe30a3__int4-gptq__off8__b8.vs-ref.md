# p1-moe30a3/int4-gptq/off8/b8  vs  p1-moe30a3/bf16/off0/b1

status: **REGISTERED** (A2)
law 1 (same weights): declared-only (published quant; source revision not verifiable)
hosts: cell ['node-d'], baseline ['node-c']
determinism: cell flip rate 0.562 (59/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 43 [0.74,0.93] | 42 [0.71,0.92] | 1/2 | 1 | identical 17, near_tie_flip 3, real_break 30 | no detectable change |
| math | 40 | 27 [0.52,0.80] | 32 [0.65,0.90] | 7/2 | 0.18 | identical 1, real_break 39 | no detectable change |
| long_context | 15 | 14 [0.70,0.99] | 15 [0.80,1.00] | 1/0 | 1 | identical 6, real_break 9 | no detectable change |

worst stratum (gates, law 7): math
