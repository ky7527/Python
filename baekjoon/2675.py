# 문자열 반복
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    R, S = input().split() # 입력 값을 R, S로 나눔.
    R = int(R) # 형변환
    S = str(S) # 형변환
    for i in range(len(S)):
        print(R*S[i] ,end='') # 문자열의 인덱스 * R의 개수만큼. end의 역할은 공백없애기위함.
    print()