import sys

N = int(sys.stdin.readline())
# 0 -> 1 0
# 1 -> 0 1
# 2 -> f(2)=f(1)+f(0)=1 1
# 3 -> f(3)=f(2)+f(1)=1 2
# 4 -> f(4)=f(3)+f(2)=2 3
# 5 -> f(5)=f(4)+f(3)=3 5 ...

zero = [1,0,1]
one = [0,1,1]

def zeroandone(num):
    if len(zero) <= num:
        for i in range(len(zero), num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    return "{0} {1}".format(zero[num], one[num])

for i in range(N):
    n = int(sys.stdin.readline())
    print(zeroandone(n))