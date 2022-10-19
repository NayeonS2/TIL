# 시간표 짜기


N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int,input().split()))[1:])
M = int(input())
students = []
for _ in range(M):
    students.append(list(map(int,input().split()))[1:])


for student in students:
    cnt = 0
    for time in times:
        if set(student)&set(time) == set(time): # 수업시간이 학생빈시간에 완전히 포함될때 cnt+=1
            cnt += 1
    print(cnt)