def nomer_func(n):
    print(n)
    if n <= 1: #toxtash sharti
        return
    else:
        nomer_func(n-1) # recursion

nomer_func(10)