str = input()
n = int(str.split(" ")[0])
m = int(str.split(" ")[1])

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

print(int(gcd(n,m)),int(lcm(m,n)))