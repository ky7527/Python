# 나머지
n = []

for i in range(10):
    a = int(input())
    b = a % 42
    n.append(b)

s = set(n) # set() - 자료 중복 제거
print(len(s)) # len() - 리스트 길이 출력