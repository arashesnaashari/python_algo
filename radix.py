def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits
str = input()
n = int(str.split(" ")[0])
m = int(str.split(" ")[1])
array = numberToBase(n,m)
sum1 = []
sum2 = []
for i in range(len(array)) :
    if(i % 2 == 0) :
        sum1.append(array[i])
    else :
        sum2.append(array[i])


if(sum(sum1) == sum(sum2)) :
    print("Yes")
else :
    print("No")