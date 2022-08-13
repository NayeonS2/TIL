import sys
sys.stdin = open('input.txt')

T = int(input())

def find_page(l,r,key):

    cnt = 0
    while l <= r:
        mid = (l + r)//2
        if mid == key:

            break
        elif mid > key:

            r = mid
        else:

            l = mid
        cnt +=1

    return cnt




for tc in range(1,T+1):
    P, A, B = map(int,input().split())


    if find_page(1,P,A) > find_page(1,P,B):
        print(f'#{tc} B')
    elif find_page(1,P,A) < find_page(1,P,B):
        print(f'#{tc} A')
    elif find_page(1,P,A) == find_page(1,P,B):
        print(f'#{tc} 0')