print(" Without recusion \n")

n = int(input("Enter the num : "))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1

print(f" Factorial of {n} is {fact} ")

print(" \n with recursion \n")

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)

n = int(input(" Enter the num : "))
print(f" Factorial of {n} is {fact(n)}")