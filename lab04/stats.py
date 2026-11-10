import math


def parse_record(line: str) -> dict:
    """Разбирает строку «город;температура;дата» в словарь."""
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"ожидалось 3 поля, получено {len(parts)}: {line!r}")

    city, temp_text, date = (part.strip() for part in parts)
    if not city:
        raise ValueError(f"пустой город: {line!r}")
    if not date:
        raise ValueError(f"пустая дата: {line!r}")

    try:
        temp = float(temp_text)
    except ValueError:
        raise ValueError(f"температура не число: {temp_text!r}") from None
    if not math.isfinite(temp):
        raise ValueError(f"температура не число: {temp_text!r}")

    return {"city": city, "temp": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    return [parse_record(line) for line in lines]


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        total[city] = total.get(city, 0) + record["temp"]
        count[city] = count.get(city, 0) + 1
    return {city: total[city] / count[city] for city in total}


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    return max(averages, key=averages.get)
