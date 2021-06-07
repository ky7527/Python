# 평균
n = int(input()) # 과목수
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for socre in test_list :
    new_list.append(socre/max_score*100) # 새로운 점수 생성
test_avg = sum(new_list)/n
print(test_avg)