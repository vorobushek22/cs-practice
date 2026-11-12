def count_by_extension(paths: list[str]) -> dict[str, int]:
    """Сколько файлов каждого расширения (в нижнем регистре, без точки)."""
    counts = {}
    for path in paths:
        name = path.split("/")[-1]
        ext = name.rpartition(".")[2].lower() if "." in name else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    """Путь с наибольшей вложенностью; при равенстве — первый по алфавиту."""
    if not paths:
        return ""
    return min(paths, key=lambda path: (-path.count("/"), path))

def human_size(n_bytes: int) -> str:
    """Размер в удобных единицах: 1536 -> «1.5 КБ»."""
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size = n_bytes
    for unit in ("КБ", "МБ", "ГБ", "ТБ"):
        size /= 1024
        if size < 1024 or unit == "ТБ":
            return f"{size:.1f} {unit}"