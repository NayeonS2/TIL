# 현대자동차에서는 부드럽고 빠른 변속이 가능한 8단 습식 DCT 변속기를 개발하여 N라인 고성능차에 적용하였다.
# 관련하여 SW 엔지니어인 당신에게 연속적으로 변속이 가능한지 점검할 수 있는 프로그램을 만들라는 임무가 내려왔다.
# 당신은 변속기가 1단에서 8단으로 연속적으로 변속을 한다면 ascending,
# 8단에서 1단으로 연속적으로 변속한다면 descending,
# 둘다 아니라면 mixed 라고 정의했다.
# 변속한 순서가 주어졌을 때 이것이 ascending인지, descending인지, 아니면 mixed인지 출력하는 프로그램을 작성하시오.

# 주어지는 숫자는 문제 설명에서 설명한 변속 정도이며, 1부터 8까지 숫자가 한번씩 등장한다.

# 첫째 줄에 8개 숫자가 주어진다.
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

import sys
input = sys.stdin.readline

asc = list(x for x in range(1,9))
dsc = list(x for x in range(8,0,-1))

lst = list(map(int,input().split()))

if lst == asc:
    print("ascending")
elif lst == dsc:
    print("descending")
else:
    print("mixed")
