# 문자열 재정렬
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