def faktorial(N):
    i=1
    fakt=1
    while i!=N+1:
        fakt = fakt*i        
        i += 1
    return fakt

print(faktorial(5))