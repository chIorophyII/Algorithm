import sys
N = int(sys.stdin.readline())
deque = []

for i in range(N):
    order = sys.stdin.readline().rstrip()

    if " " in order:
        order, num = order.split()

    if order == "push_front":
        deque.insert(0, int(num))
    if order == "push_back":
        deque.append(int(num))
    if order == "pop_front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
    if order == "pop_back":
        if not deque:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    if order == "size":
        print(len(deque))
    if order == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    if order == "front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
    if order == "back":
        if not deque:
            print(-1)
        else:
            print(deque[-1])