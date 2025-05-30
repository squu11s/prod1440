def compute_f():
    f = [1, 3]  
    A = []
 
    if f[0] % 2 != 0:
        A.append(f[0])
    if f[1] % 2 != 0:
        A.append(f[1])

    n = 2
    while len(A) < 40:
        next_val = 5 * f[n-1] + f[n-2]
        f.append(next_val)
        if next_val % 2 != 0:
            A.append(next_val)
        n += 1

    return A[39]  

result = compute_f()
print("40-й нечётный элемент массива A:", result)