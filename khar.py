x = input()
y = x.split(" ")
ar = []

stage = True
while len(ar) < int(y[2]) :
    if stage == True :
        ar.append(int(y[0]))
        stage = False
    else :
        ar.append(int(y[1]))
        stage = True


# for i in range(int(y[2])) : 
#     if len(ar) % 2 == 0 :
#         ar.append(int(y[0]))
#     else :
#         ar.append(int(y[1]))


    
print(sum(ar))

