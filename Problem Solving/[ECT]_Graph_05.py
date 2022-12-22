# 탑승구
# 비행기를 최대 몇 대 도킹할 수 있는지 출력
# 가능한 큰 번호 탑승구로 도킹

# g 탑승구 도킹후엔 g-1 탑승구와 union
# 도킹전에 루트가 0인지 확인하고, 아닐때만 도킹
# 0이면 break!

import sys
sys.stdin = open("input.txt")

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

G = int(input())
P = int(input())

parent = [0]*(G+1)

for i in range(1,G+1):
    parent[i] = i

cnt = 0
for p in range(1,P+1):
    now_parent = find_parent(parent,int(input()))
    # 도킹전에 루트가 0인지 확인하고, 아닐때만 도킹
    if now_parent == 0:
        break
    else:
        # g 탑승구 도킹후엔 g-1 탑승구와 union
        union_parent(parent,now_parent,now_parent-1)
        cnt += 1
print(cnt)

