import random

l = [i for i in range(1,10)]

random.shuffle(l)
print(f' list is {l} ')

for i in range(len(l)-1):
    min_index = i
    for j in range(i+1, len(l)):
        if l[min_index] > l[j]:
            min_index = j
    temp = l[i]
    l[i] = l[min_index]
    l[min_index] = temp
    
    print(f' after {i} is {l} ')

print(f' sorted list is {l} ')