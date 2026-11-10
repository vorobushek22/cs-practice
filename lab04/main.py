import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

non_empty = [line for line in lines if line.strip()]
skipped = len(non_empty) - len(records)

print(len(records))
print(skipped)
if records:
    best = warmest_city(records)
    print(f"{average_by_city(records)[best]:.1f}")
else:
    print("Нет данных")