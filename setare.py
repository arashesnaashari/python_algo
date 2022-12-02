n = int(input())
# x = n*"*"

# y = n-2


########1
# print(x)
# for i in range(y) :
#     print("*" + (y)*" " + "*")
# print(x)


#########2
# for i in range(n) :
#     if i == n-1 or i == 0 :
#         array.append(x)
#     else:
#         array.append("*" + (y)*" " + "*")
# for i in range(n) :
#     print(array[i])

# array3 = ['***', '*    *', '***']
# array4 = ['****', '*    *', '*    *', '****']
# array5 = ['*****', '*    *', '*    *', '*    *', '*****']
# array6 = ['******', '*    *', '*    *', '*    *', '*    *', '******']
# array7 = ['*******', '*    *', '*    *', '*    *', '*    *','*    *', '*******']
# array8 = ['********', '*    *', '*    *', '*    *', '*    *','*    *','*    *', '********']
# array9 = ['*********', '*    *', '*    *', '*    *', '*    *','*    *','*    *','*    *', '*********']
# array10 = ['**********', '*    *', '*    *', '*    *', '*    *','*    *','*    *','*    *','*    *', '**********']

# if n == 3 :
#     for i in range(n) :
#         print(array3[i])
# if n == 4 :
#     for i in range(n) :
#         print(array4[i])
# if n == 5 :
#     for i in range(n) :
#         print(array5[i])
# if n == 6 :
#     for i in range(n) :
#         print(array6[i])
# if n == 7 :
#     for i in range(n) :
#         print(array7[i])
# if n == 8 :
#     for i in range(n) :
#         print(array8[i])
# if n == 9 :
#     for i in range(n) :
#         print(array9[i])
# if n == 10 :
#     for i in range(n) :
#         print(array10[i])

def full_line(num):
    x = ''
    for j in range(num):
        x+= "*"
    print(x)

full_line(n)
string = ''
for i in range(n):
    if i == 0 or i == n-1:
        string += "*"
    else:
        string += " "

for i in range(n-2):
    print(string)
full_line(n)
            

