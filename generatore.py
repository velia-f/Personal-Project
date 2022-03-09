#generatore casuale di numeri
import random

li = []
va = random.randint(0,10)
for i in range(0,10):
    while va in li:
        va = random.randint(0,15)
    li.append(va)
    print(str(va)+'\n')
    print(li)
    i+=1
print('\n\nAdesso è finito')