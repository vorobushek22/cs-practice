import re
import json

def csv_to_records(text: str) -> list[dict]:
    """CSV с заголовком -> список словарей. Значения остаются строками."""
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    header = lines[0].split(",")
    records = []
    for line in lines[1:]:
        values = line.split(",")
        # если в строке меньше значений, чем в заголовке, добиваем пустыми
        values += [""] * (len(header) - len(values))
        records.append(dict(zip(header, values)))
    return records

def _convert(value: str):
    """Приводит строку к int, float, bool или оставляет строкой."""
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value)
    return value

def parse_settings(lines: list[str]) -> dict:
    """Простой YAML: «ключ: значение», списки через «- », комментарии после #."""
    result = {}
    current_list = None  # ключ списка, который сейчас заполняем
 
    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
 
        if line.startswith("-"):
            if current_list is not None:
                result[current_list].append(_convert(line[1:].strip()))
            continue
 
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value == "":
            result[key] = []
            current_list = key
        else:
            result[key] = _convert(value)
            current_list = None
 
    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из справочника. Поля записи важнее."""
    merged = []
    for row in rows:
        value = row.get(key)
        info = extra.get(value)
        if info is None and value is not None:
            info = extra.get(str(value))  # ключи в JSON всегда строки
        merged.append({**(info or {}), **row})
    return merged

def records_to_json(records: list[dict]) -> str:
    """Список словарей -> JSON: отступ 2, ключи по алфавиту, кириллица как есть."""
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)