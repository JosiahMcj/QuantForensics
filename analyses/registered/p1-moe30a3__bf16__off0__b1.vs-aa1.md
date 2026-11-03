# p1-moe30a3/bf16/off0/b1  vs  p1-moe30a3/bf16/off0/b1

status: **REGISTERED** (A2)
law 1 (same weights): reference
hosts: cell ['node-c'], baseline ['node-a']
determinism: cell flip rate 0.000 (0/105), baseline 0.000
padded vocab ids sampled: none
baseline-unstable tasks (excluded from break counts): 0

| stratum | n | cell pass | baseline pass | b/c | McNemar p | divergences | verdict |
|---|---|---|---|---|---|---|---|
| code | 50 | 42 [0.71,0.92] | 42 [0.71,0.92] | 0/0 | 1 | identical 50 | no detectable change |
| math | 40 | 32 [0.65,0.90] | 32 [0.65,0.90] | 0/0 | 1 | identical 40 | no detectable change |
| long_context | 15 | 15 [0.80,1.00] | 15 [0.80,1.00] | 0/0 | 1 | identical 15 | no detectable change |

worst stratum (gates, law 7): code
