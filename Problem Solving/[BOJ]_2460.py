# 지능형 기차 2

max_ = 0
people = 0
for _ in range(10):
    off, on = map(int,input().split())
    people -= off
    people += on

    if people > max_:
        max_ = people
print(max_)