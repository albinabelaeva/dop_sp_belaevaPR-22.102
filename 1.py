# b=int(input())
# a=0
# for i in range(1, b+1):
#     for j in range(1, b+1):
#         a+=(i&j)
# print(a)

a = int(input())
listt = []
for i in range(a):
    b = int(input())
    s = 0
    for i in range(1, b+1):
        for j in range(1, b+1):
            s+= (i&j)
    listt.append(s)
for i in listt:
    print(i)