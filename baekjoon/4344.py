# 평균은 넘겠지
t = int(input())

for i in range(t):
    c = list(map(int, input().split()))
    avg = sum(c[1:])/c[0] # c[0]:학생수 c[1:]:점수
    cnt = 0
    for score in c[1:]:
        if score > avg:
            cnt += 1 # 평균 이상인 학생 수
    rate = cnt/c[0] *100
    print(f'{rate:.3f}%')
    