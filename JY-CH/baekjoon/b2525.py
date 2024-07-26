# 오븐 시계


# 정수로 받을거에요
# 시간과 분, 요리시간을 변수명으로 설정.
h, m = map(int, input().split())
cook_m = int(input())

# A, B, C 범위 설정 (의미가 있나?)
# 입력값이 주어지는 문제에서는 큰 의미가 없으나
# 만약 오전 오후와 시간 표기가 필요하다면 그때는 필요함.?
0 <= h <= 23
0 <= m <= 59
0 <= cook_m <= 1000

# 조건을 설정할건데

# 시간이 23시 전이고 조리시간과 분의 합이 60을 넘는다면
# 입력된 시간에 조리시간과 분의 합을 60으로 나눈 몫을 더하고,
# 분을 조리시간과 분의 합을 60으로 나눈 나머지를 출력한다.
if h < 23 and ((cook_m + m) >= 60):
    print((h + ((cook_m + m) // 60)), ((cook_m + m) % 60))
# 시간이 23시고 조리시간과 분의 합이 60을 넘는다면
# 입력된 시간에 (조리시간과 분의 합을 60으로 나눈 몫)을 더한 다음 1을 빼주고,
# 분을 조리시간과 분의 합을 60으로 나눈 나머지를 출력한다.
elif h == 23 and ((cook_m + m) >= 60) :
    print((0 + (((cook_m + m) // 60) - 1)), ((cook_m + m) % 60))
else :
    print(h, (cook_m + m))



# elif h < 23 and ((cook_m + m) < 60):
#     print(h, (cook_m + m))




