x = int(input())
i=0

if x == 0 or x == 1 :
    print(2)
else:
    while x > 2**i:
        i += 1
        if x == 2**i:
            print(2**(i+1))
        elif x < 2**i:
            print(2**i)

        
