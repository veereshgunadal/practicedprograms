print(" without function \n")

l = [i for i in range(1,10)]

num = int(input(" Enter the number to search : "))

low = 0
high = len(l) - 1
flag = 0
while low <= high:
    mid = (low + high)//2
    if num == l[mid]:
        flag = 1
        print(" found ")
        break
    elif num < l[mid]:
        high = mid - 1
    elif num > l[mid]:
        low = mid + 1
if flag == 0:
    print(" not found ")


print(" \n with function \n")

def binary_search(l, num):
    low = 0
    high = len(l) - 1
    flag = 0
    while low <= high:
        mid = (low + high)//2
        if num == l[mid]:
            flag = 1
            print(" found ")
            break
        elif num < l[mid]:
            high = mid - 1
        elif num > l[mid]:
            low = mid + 1
    if flag == 0:
        print(" not found ")
 
l = [i for i in range(1,10)]
num = int(input(" Enter the number to search : "))

binary_search(l, num)