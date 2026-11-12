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