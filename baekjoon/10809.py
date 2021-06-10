# 알파벳 찾기
S = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S: # S에 알파벳 존재 유무 확인
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')