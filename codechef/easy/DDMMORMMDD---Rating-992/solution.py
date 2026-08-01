t = int(input())

for _ in range(t):
    s = input().strip()
    first, second, _ = s.split('/')

    a = int(first)
    b = int(second)

    if a <= 12 and b <= 12:
        print("BOTH")
    elif a > 12:
        print("DD/MM/YYYY")
    else:
        print("MM/DD/YYYY")