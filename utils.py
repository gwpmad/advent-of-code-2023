def open_file(day: str) -> str:
    with open(f"./day_{day}/input", encoding="utf-8") as f:
        return f.read().strip()
