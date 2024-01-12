def f(day):
    if day == 10:
        return 1

    n = f(day + 1)
    return n * 2 + 1


print(f(1))