# 111_Map_IQ.py
# Topic: map() with a lambda - convert units (ms -> seconds)
#
# Real-world use: API response times arrive in milliseconds;
# map() converts every value to seconds (divide by 1000).
# A lambda is used directly inside map - no named function needed.

response_times_ms = [1200, 1500, 1800]


def mil_sec(x):
    return x / 1000

response_times_s = list(map(lambda x: x/1000, response_times_ms))
print(response_times_s)   # [1.2, 1.5, 1.8]
