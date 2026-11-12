LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line: str) -> dict:
    """Разбирает строку «время уровень сообщение» в словарь."""
    parts = line.strip().split(None, 2)
    if len(parts) != 3:
        raise ValueError(f"ожидалось 3 части: время, уровень, сообщение: {line!r}")

    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"неизвестный уровень {level!r}: {line!r}")

    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    """Сколько строк каждого уровня; испорченные считаются под ключом BROKEN."""
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            key = parse_event(line)["level"]
        except ValueError:
            key = "BROKEN"
        counts[key] = counts.get(key, 0) + 1
    return counts


def top_errors(lines, n: int) -> list[list]:
    """n самых частых сообщений уровня ERROR: пары [сообщение, сколько раз]."""
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            message = event["message"]
            counts[message] = counts.get(message, 0) + 1

    ordered = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return [[message, count] for message, count in ordered[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    """Текст отчёта по готовым подсчётам."""
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for message, count in errors:
        lines.append(f"- {message} — {count}")
    return "\n".join(lines) + "\n"