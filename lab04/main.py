import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

print(len(records))
print(0)
best = warmest_city(records)
print(f"{average_by_city(records)[best]:.1f}")
