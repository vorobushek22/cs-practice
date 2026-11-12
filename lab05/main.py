from pathlib import Path

from logstats import count_levels, format_report, top_errors

here = Path(__file__).parent

name = input().strip()
path = Path(name)
if not path.exists():
    path = here / name

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)
with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

print(sum(counts.values()))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

with open(here / "report.txt", "w", encoding="utf-8", newline="\n") as report:
    report.write(format_report(counts, errors))