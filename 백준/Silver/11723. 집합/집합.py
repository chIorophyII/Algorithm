import sys

N = int(sys.stdin.readline())
S = set()

for i in range(N):
    init = sys.stdin.readline().strip()

    if init == "all":
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    elif init == "empty":
        S = set()

    else:
        op = init.split()[0]
        num = init.split()[1]
        num = int(num)

        if op == "add":
            S.add(num)
        elif op == "remove":
            if num in S:
                S.remove(num)
        elif op == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif op == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)
