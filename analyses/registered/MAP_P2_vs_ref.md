# QuantForensics map

status: REGISTERED

| cell | baseline | law 1 | flip rate | padded ids | code pass (d, b/c, verdict) | math pass (d, b/c, verdict) | long_context pass (d, b/c, verdict) | worst |
|---|---|---|---|---|---|---|---|---|
| p2-dense14/int4-awq/off0/b1 | p2-dense14/bf16/off0/b1 | declared-only | 0.000 | 0 | 37/50 (-0.04, 4/2, no detectable change, 42 real breaks) | 21/40 (-0.10, 7/3, no detectable change, 35 real breaks) | 15/15 (+0.00, 0/0, no detectable change) | math |
| p2-dense14/int4-gptq/off0/b1 | p2-dense14/bf16/off0/b1 | declared-only | 0.000 | 0 | 34/50 (-0.10, 8/3, no detectable change, 45 real breaks) | 19/40 (-0.15, 8/2, no detectable change, 25 real breaks) | 15/15 (+0.00, 0/0, no detectable change, 1 real breaks) | math |
| p2-dense14/int8-gptq/off0/b1 | p2-dense14/bf16/off0/b1 | declared-only | 0.000 | 0 | 38/50 (-0.02, 1/0, no detectable change, 10 real breaks) | 21/40 (-0.10, 4/0, no detectable change, 7 real breaks) | 15/15 (+0.00, 0/0, no detectable change) | math |
| p2-dense7/int4-awq/off0/b1 | p2-dense7/bf16/off0/b1 | declared-only | 0.000 | 0 | 36/50 (-0.06, 5/2, no detectable change, 44 real breaks) | 13/40 (-0.10, 5/1, no detectable change, 30 real breaks) | 15/15 (+0.00, 0/0, no detectable change, 1 real breaks) | math |
| p2-dense7/int4-gptq/off0/b1 | p2-dense7/bf16/off0/b1 | declared-only | 0.000 | 0 | 39/50 (+0.00, 2/2, no detectable change, 44 real breaks) | 7/40 (-0.25, 12/2, DEGRADED, 31 real breaks) | 15/15 (+0.00, 0/0, no detectable change, 13 real breaks) | math |
| p2-dense7/int8-gptq/off0/b1 | p2-dense7/bf16/off0/b1 | declared-only | 0.000 | 0 | 38/50 (-0.02, 1/0, no detectable change, 5 real breaks) | 16/40 (-0.03, 1/0, no detectable change, 4 real breaks) | 15/15 (+0.00, 0/0, no detectable change, 1 real breaks) | math |
