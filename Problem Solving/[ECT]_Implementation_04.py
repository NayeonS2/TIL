# 문자열 재정렬
# 모든 알파벳 오름차순 정렬
# 알파벳 정렬한 뒤에 숫자 모두 더한 값을 이어서 출력

s = 'AJKDLSI412K4JSJ9D'

alpha = []
sum_ = 0
for i in range(len(s)):
    if s[i].isdigit():
        sum_ += int(s[i])
    else:
        alpha.append(s[i])
alpha.sort()
ans = ''.join(alpha) + str(sum_)

print(ans)