from random import randrange

def qsort(arr):
    # pivot = arr.pop(0)
    pivot = arr.pop(randrange(len(arr)))
    kichik = [i for i in arr if i<=pivot]
    katta = [i for i in arr if i>pivot]
    print(f'{kichik} + [{pivot}] + {katta}')
    return qsort(kichik) + [pivot] + qsort(katta)

list1 = [1, 5, 2, 100]
print(list1)
# list2 = list(range(10))
print(qsort(list1))