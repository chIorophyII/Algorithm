import sys

N = int(sys.stdin.readline())

def fibonacci(num):
    num1, num2 = 0, 1

    for i in range(N):
        num1, num2 = num2, num1+num2

    return num1
print(fibonacci(N))