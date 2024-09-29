prime = []
non_prime = []

for i in range(2,101):
    j = 2
    count = 2
    while j < i:
        if i % j == 0:
            count = count + 1
            break
        j = j+1
    if count == 2:
        prime.append(i)
    else:
        non_prime.append(i)

print(f' Prime numbers {prime}')
print(f' Non Prime numbers {non_prime}')