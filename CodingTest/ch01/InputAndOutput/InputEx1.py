# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백을 기준으로 구분하여 입력
# input().split() : split()이 공백을 기준으로 나눠주는 메소드이므로 공백을 기준으로 문자열을 입력받는다.
# map(int, input().split())) : map은 어떤 리스트가 있을 때 각 원소에 어떤 함수를 적용할때 서용한다.
data = list(map(int, input().split()))

print(n)
print(data)