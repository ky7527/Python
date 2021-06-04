# 더하기 사이클

n = int(input())  # 68
num = n
cnt = 0           # 사이클 수

while True :
    a = n // 10   # 6
    b = n % 10    # 8
    c = (a+b) % 10  # 6 + 8 = 1"4"
    num = (b*10) + c # 80 + 4 = 84

    cnt = cnt + 1   # 사이클 수 +1
    if(num == n):
        break
print(cnt)