import random
l = [i for i in range(1,10)]

random.shuffle(l)
print(f' list {l}')
for i in range(len(l)-1, 0, -1):
    for j in range(i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
    print(f' after {i} is {l} ')
print(f' sorted list is {l}')