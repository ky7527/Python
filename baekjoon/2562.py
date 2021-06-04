# 최댓값
n = []

for i in range(9):
    i = int(input())
    n.append(i) # append 리스트 요소 추가

print(max(n))
print(n.index(max(n))+1) # max함수로 가장 큰 수를 찾고 index함수로 위치를 찾는다. 인덱스는 0부터 시작이라 1을 더해줘야함