

t = int(input(""))
list = []

for i in range(t):
    given = str(input(""))
    a = int(given.split(' ')[0])
    b = int(given.split(' ')[1])
    last = ( a**b )% 10
    list.append(last)


for i in list:
    print(i)