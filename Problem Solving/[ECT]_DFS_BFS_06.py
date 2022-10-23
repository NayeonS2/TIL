# 괄호 변환

p = '()))((()'

def balanced_idx(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1
        if cnt == 0:
            return i

def is_proper(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer               # 빈문자열은 그대로 반환

    idx = balanced_idx(p)

    u = p[:idx+1]                   # 문자열을 균형잡힌 문자열 u,v 로 나눔
    v = p[idx+1:]

    if is_proper(u):
        answer = u + solution(v)    # u가 올바른 문자열이면, v를 1단계부터 다시 수행한 결과를 u에 이어붙인 후 반환
    else:
        answer += '('               # 아니라면, 빈 문자열에 '(' 를 붙이고
        answer += solution(v)       # v를 1단계부터 다시 수행한 결과를 u에 이어붙인 후
        answer += ')'               # 다시 ')'를 붙임

        u = list(u[1:-1])           # u의 첫번째, 마지막째 문자를 제거하고,

        for i in range(len(u)):     # 나머지 문자열의 괄호 방향을 뒤집어서
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += ''.join(u)        # 뒤에 이어 붙임

    return answer



print(solution(p))