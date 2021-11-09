def is_armstrong(n: int) -> bool:
    str_n = str(n)
    return sum([int(d) ** len(str_n) for d in str_n]) == n