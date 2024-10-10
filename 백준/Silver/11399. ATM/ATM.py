n = int(input())
num_list = list(map(int, input().split()))
answer = 0

num_list.sort()

for i in range(1, n+1):
    answer += sum(num_list[0:i])

print(answer)