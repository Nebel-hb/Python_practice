def fibonacci_list(n):
    fib = [1, 1]
    if n == 1:
        fib = [1]
    else:
        for k in range(2, n):
            fib.append(fib[k-1]+fib[k-2])
    return fib