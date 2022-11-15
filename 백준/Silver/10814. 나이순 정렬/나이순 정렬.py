import sys
N = int(sys.stdin.readline())
dic = dict()

for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    if age in dic:
        dic[age].append(name)
    else:
        dic[age] = [name]

dic = sorted(dic.items())

for i in dic:
    for j in range(len(i[1])):
        print(int(i[0]), i[1][j])