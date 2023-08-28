# 뒤집기
import sys
sys.stdin = open('input.txt')

s = input()

lst = []

for i in range(len(s)):
    if ''.join(lst) == s:
        break
    tmp = s[i]

    for j in range(i+1, len(s)):

            if s[i] == s[j]:
                tmp += s[j]
                if i==len(s)-1 or j==len(s)-1:
                    lst.append(tmp)
                    break

            else:
                lst.append(tmp)
                i = j
                tmp = s[i]
                if i==len(s)-1 or j==len(s)-1:
                    lst.append(tmp)
                    break

one = 0
zero = 0

for comp in lst:
    if '1' in comp:
        one += 1
    else:
        zero += 1


print(min(one,zero))