# cook your dish here
t = int(input())

for _ in range(t):
    x = int(input())
    s = input().strip()

    carlsen = 2 * s.count('C') + s.count('D')
    chef = 2 * s.count('N') + s.count('D')

    if carlsen > chef:
        print(60 * x)
    elif carlsen == chef:
        print(55 * x)
    else:
        print(40 * x)