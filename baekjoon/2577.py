# 숫자의 개수
a = input()
b = input()
c = input()

# a*b*c의 값 구하기
num = int(a)*int(b)*int(c)
# 결과값을 배열로 만들기
num = str(num)
# count()를 사용해 개수 구하기
for i in range(0, 10):
    print(num.count(str(i)))