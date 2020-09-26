# n, m, k를 공백을 기준으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

n = int(input())
m = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
print(arr)