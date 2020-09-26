i = 1
j = 1
result1 = 0
result2 = 0

while i <= 9:
    result1 += i
    i += 1

print(result1)

while j <= 9:
    if j % 2 == 1:
        result2 += j
    j += 1

print(result2)