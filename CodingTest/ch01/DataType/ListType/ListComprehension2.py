# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
# 어떠한 변수를 선언하지 않을 때 _를 사용한다.
array = [[0] * m for _ in range(n)]
print(array)

# N X M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 4
m = 3
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)
