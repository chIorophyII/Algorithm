import sys
In = sys.stdin.readline
N = int(In())

for i in range(N):
    bracket = In().strip()
    stack = []
    for j in range(len(bracket)):
        if bracket[j] == "(":
            stack.append(bracket[j])
        elif len(stack) == 0:
            stack.append(bracket[j])
            break
        else:
            stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")