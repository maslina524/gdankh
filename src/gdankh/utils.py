def chunks(l: list, c: int) -> list:
    return [l[i:i+c] for i in range(0, len(l), c)]