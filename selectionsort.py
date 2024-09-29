import random

l = [i for i in range(1,10)]

random.shuffle(l)
print(f' list is {l}')

for i in range(1,len(l)):
    for j in range(i, 0, -1):
        if l[j-1] > l[j]:
            temp = l[j-1]
            l[j-1] = l[j]
            l[j] = temp
    
print(f' after {i} is {l} ')

print(f' sorted list is {l}')