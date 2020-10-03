array = [3, 5, 1, 2, 4] # 5개의 데이터(N=5)

for i in array:
    for j in array:
        temp = i * j
        print(temp)
# 시간복잡도 O(N^2)

