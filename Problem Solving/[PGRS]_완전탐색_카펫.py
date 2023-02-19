brown = 10
yellow = 2


def solution(brown, yellow):

    def decim(n):
        tmp = []
        for i in range(1,n+1):
            if n%i == 0:
                tmp.append(i)
        return tmp

    decims = decim(brown+yellow)

    if len(decims) % 2 == 0:
        idx_l = len(decims)//2 - 1
        idx_r = len(decims) // 2

    elif len(decims) %  2 == 1:
        idx_l = len(decims)//2
        idx_r = len(decims)//2

    while True:
        if (decims[idx_l]-2)*(decims[idx_r]-2) == yellow:
            return [decims[idx_r],decims[idx_l]]
        else:
            idx_l -= 1
            idx_r += 1

print(solution(brown,yellow))

