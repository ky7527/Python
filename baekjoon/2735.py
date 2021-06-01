# 윤년
Y = int(input())

if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0 :
    print(1) # 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
else :
    print(0)