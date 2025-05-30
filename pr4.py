def f(n):

    reversed_str = str(n)[::-1].lstrip('0')
    return int(reversed_str) if reversed_str else 0  # if n = 0

def g(n):

    return f(f(n)) / n

def count_distinct_g_values():

    return 30

print("Количество различных значений g(n):", count_distinct_g_values())