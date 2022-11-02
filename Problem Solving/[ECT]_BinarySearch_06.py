# 프로그래머스 가사검색
# 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
# 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.
# 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.

from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    rev_arr = [[] for _ in range(10001)]

    for w in words:
        arr[len(w)].append(w)
        rev_arr[len(w)].append(w[::-1])

    for i in range(10001):
        arr[i].sort()
        rev_arr[i].sort()

    for pat in queries:
        if pat[0] != '?':   # 접두사
            ans = bisect_right(arr[len(pat)], pat.replace('?','z')) - bisect_left(arr[len(pat)], pat.replace('?','a'))
        else:   # 접미사
            ans = bisect_right(rev_arr[len(pat)], pat[::-1].replace('?', 'z')) - bisect_left(rev_arr[len(pat)], pat[::-1].replace('?', 'a'))
        answer.append(ans)
    return answer

print(solution(words,queries))