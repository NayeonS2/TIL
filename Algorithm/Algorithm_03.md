# 03. 문자열 (String)

## Brute Force 알고리즘
- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식
- <img src="./algo_03_img/bruteforce.png">
- ```python
    p = 'is'
    t = 'This is a book~!'
    M = len(p)  # 찾을 패턴 길이
    N = len(t)  # 전체 텍스트 길이

    def bruteforce(p, t):
        j = 0
        i = 0

        while j < M and i < N:
            if t[i] != p[j]:
                i = i-j
                j = -1
            i += 1
            j +=1

        if j == M:
            return i-M
        else:
            return -1

    print(bruteforce(p,t))  # 2
  ```
- 시간 복잡도
    - 최악의 경우 모든 위치에서 패턴을 비교해야 하므로 O(MN)이 됨


---

## KMP 알고리즘
- 불일치가 발생한 텍스트 문자열의 앞 부분에 어떤 문자가 있는지를 미리 알고있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴내에서 반복하는 구간이 있을것이라는 전제하에 진행, 반복이 없다면 무의미함
- 시간 복잡도 : O(M + N)
<img src="./algo_03_img/kmp_01.png">
<img src="./algo_03_img/kmp_02.png">
<img src="./algo_03_img/kmp_03.png">
<img src="./algo_03_img/kmp_04.png">

- 전처리 (Preprocessing)
    - 패턴에 대한 리턴 인덱스를 생성하는 것이 목적
    - 패턴은 패턴 내에 최전단 문자부터 일정길이가 중복되어야 한다.
    - 1부터 M-1까지 인덱스 i에 대해서 문자에 대해 j위치의 문자와 동일한지 확인
        - j는 문자가 일치할 때만 0 ~ M-1까지 증가
    - 일치하면 리턴인덱스 리스트에 j + 1(중복횟수  + 1) 저장
    - 불일치할 경우 j = 0
        - edge case : 해당 문자가 패턴 최전단 문자와 일치할 경우 lps에 1 저장, j += 1

- KMP
    - 패턴과 텍스트 내에 문자마다 비교
        - 일치 : 인덱스 증가시키기
        - 불일치
            - edge case : 패턴 비교 위치가 최전단 문자였을 땐 텍스트 위치 한 칸 이동
                - j = 0일 때 i += 1
            - 비교 위치가 패턴의 최전단 문자가 아니였다면 j = lps[j - 1]

- ```python
    text = 'babab cdabcdabcef ij'
    pattern = 'abcdabcef' # 000012300

    def pre_process(p):
        lps = [0] * len(p)

        j = 0

        for i in range(1, len(p)):
            if p[i] == p[j]:
                lps[i] = j + 1
                j += 1
            else:
                j = 0
                if p[i] == p[j]:
                    lps[i] = j + 1
                    j += 1
        return lps

    def KMP(t, p):
        lps = pre_process(p)
        i = 0
        j = 0

        while i < len(t):
            if p[j] == t[i]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i +=1
            if j == len(p):
                return i - j
        else:
            return -1

    print(KMP(text,pattern))    # 8
   ```
---
## Boyer Moore 알고리즘
- 패턴 문자열의 오른쪽 끝 부분에서부터 왼쪽 앞부분 방향으로 문자를 비교하는 방식
- 보통 상황에서 문자열 앞부분보다 뒷부분이 불일치가 일어날 확률이 높다는 성질을 이용한 알고리즘
- 패턴문자열에 대한 이동거리 skip table을 만들어놓고 적절한 이동 거리만큼 점프해가며 비교함
- 시간 복잡도 : 일반적으로 O(N) 보다 적음 (최악의 경우 O(MN))
  - 찾으려는 문자열 패턴 길이 M, 총 문자열 길이 N
- 장점 : 원본 문자열을 모두 보지 않아도 검색 가능
- 단점 : 구현이 비교적 복잡함
<img src="./algo_03_img/boyermoore_01.png">
<img src="./algo_03_img/boyermoore_02.png">
- ```python
    def pre_process(pattern):
        M = len(pattern)  # 패턴의 길이

        skip_table = dict()
        for i in range(M-1):
            skip_table[pattern[i]] = M - i - 1

        return skip_table


    def boyer_moore(text, pattern):
        skip_table = pre_process(pattern)
        M = len(pattern)

        i = 0  # text index
        while i <= len(text) - M:
            j = M - 1   # 뒤에서 비교해야 되기 때문 j를 끝에 index
            k = i + (M-1)  # 비교를 시작할 위치 (현재위치 + M번째 인덱스)

            # 비교할 j가 남아있고, text와 pattern이 일치하면
            # 그 다음 앞에 글자를 비교하기 위해 인덱스 감소
            while j >= 0 and pattern[j] == text[k]:
                j -= 1
                k -= 1

            if j == -1:  # 일치 함
                return i
            # 일치하지 않는다면
            else:
                # i를 비교할 시작 위치를 skip table에서 가져온다.
                i += skip_table.get(text[i+M-1], M)

        return -1  # 일치되는 패턴이 없음


    text = 'ABC ABCDAB ABCDABCDABDE'
    pattern = 'ABCDABD'

    print(boyer_moore(text, pattern))   # 15
  ```

