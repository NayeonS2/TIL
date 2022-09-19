# 8. Computational Thinking

## 서론 - 프로그래밍과 논리/수학

- 명제
  - 참이나 거짓을 알 수 있는 식이나 문장
  - p, q, r ...로 표현
- 진릿값
  - 참이나 거짓을 표현
  - T, F 또는 1, 0

- 연산 (결합)
  - 부정 NOT
    - p가 명제일 때, 명제의 진릿값이 반대
    - ~p또는 ㄱp로 표기 (not p 또는 p의 부정으로 읽음)
  - 논리곱 AND
    - p, q가 명제일 때, p, q 모두 참일 때만 참이 되는 명제.
    - p ^ q (p and q, p 그리고 q)
  - 논리합 OR
    - p, q가 명제일 때, p, q 모두 거짓일 때만 거짓이 되는 명제.
    - p V q (p or q, p 또는 q)
  - 배타적 논리합 XOR (exclusive OR)
    - p, q가 명제일 때, p, q 중 하나만 참일 때 참이 되는 명제.
    - p xor q
    - T T -> F / T F -> T / F T -> T / F F -> F
- 합성
  - 연산자 우선순위
    - ㄱ > V, ^ > ->, <->  (NOT > OR, AND > ->, <->)
    - 항진명제 : 진릿값이 항상 참
    - 모순명제 : 진릿값이 항상 거짓
    - 사건명제 : 항진명제도 모순명제도 아닌 명제
- 조건명제
  - p, q가 명제일 때, 명제 p가 조건(또는 원인), q가 결론(또는 결과)로 제시되는 명제.
  - p -> q (p이면 q이다.)
  - **p가 F면 p -> q는 T**
  - **q가 T면 p -> q는 T**
- 쌍방조건명제
  - p, q가 명제일 때, 명제 p와 q가 모두 조건이면서 결론인 명제
  - p <-> q (p면 q고, q면 p다.)
  - T T -> T / F F -> T / T F -> F / F T -> F