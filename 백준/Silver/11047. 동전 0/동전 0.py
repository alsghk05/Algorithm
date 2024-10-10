n, k = map(int, input().split())
kind = list()
num = 0

for i in range(n):
    kind.append(int(input()))

for i in reversed(range(n)):
    num += k//kind[i]
    k = k%kind[i]

print(num)