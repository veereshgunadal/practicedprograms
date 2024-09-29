print(" without functions \n")

l = [i for i in range(1,10)]

num = int(input(" Enter the number to search : "))
n = len(l)
i = 0
flag = 0
while i < n:
    if num == l[i]:
        flag = 1
        print(" found ")
        break
    i = i+1
if flag == 0:
    print(" not found ")


def linear_search(l, num):
    n = len(l)
    i = 0
    flag = 0
    while i < n:
        if num == l[i]:
            flag = 1
            print(" found ")
            break
        i = i+1
    if flag == 0:
        print(" not found ")

l = [i for i in range(1,10)]
num = int(input(" Enter the number to search : "))
linear_search(l, num)