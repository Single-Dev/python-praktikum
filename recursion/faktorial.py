def fakt(n):
    print(n, end=' ')
    if n == 1:
        return 1
    else:
        return n * fakt(n-1)

print(fakt(500))