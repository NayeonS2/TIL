# 벌집
# 한바퀴씩 생각
target = int(input())

# 1 2 9 22 41
#
# 1 4 13
# 3 9
#
# 1 6 17 34 58
# 5 11 17 24

strt = 1
cnt = 1

while target>strt:
    strt += cnt*6
    cnt += 1

print(cnt)