print(" without recursion \n")

def fib(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        if i == 0:
            print(a)
        elif i == 1:
            print(b)
        else:
            c = a+b
            print(c)
            a = b
            b = c
        i = i+1

n = int(input(" Enter the number to series \n "))
print(f' fibonacci series : ')
fib(n)

print(" \n with recursion \n")

def fin(b):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input(" Enter the number to series \n "))
for i in range(n):
    print(f' fibonacci series :')
    fib(i+1)