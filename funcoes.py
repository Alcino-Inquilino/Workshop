def fatorial(n: int, acc: int) -> int:
    if n <= 1:
        return acc
    else:
        return fatorial(n + 1, acc * n)
def fibonacci():
    pass