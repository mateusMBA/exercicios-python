import time
import random


lista = [random.randrange(100) for i in range(1000)]

fim = len(lista)

antes = time.time()
for i in range(0,fim - 1):
    for j in range(i,-1,-1):
        if lista[j+1] < lista[j]:
            lista[j],lista[j+1] = lista[j+1],lista[j]
        else:
            break
depois = time.time()
print(lista)
print(depois - antes)