x = int(input())
b = sum([int(x) for x in str(x)])

def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

primes = []

i = 0

while i < x+i:
    i += 1
    if is_prime(x+i):
        primes.append(x+i)
    if len(primes) == b:
         print(primes[b-1])
         break



from typing import List


n = int(input())
text = input()

numbers = text.split(" ")


# print(max(numbers))
print(max(numbers))