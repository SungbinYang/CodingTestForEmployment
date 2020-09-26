scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 세 번재 인자는 스텝이라 하고 이 간격을 유지한다. 단, 생략할경우 1이다.
for i in range(1, 100, 3):
    print(i)
