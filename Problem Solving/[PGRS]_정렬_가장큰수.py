numbers = [303,30]
def solution(numbers):
    if set(numbers) == {0}:
        numbers = list(set(numbers))

    tmp = []
    for num in numbers:
        tmp.append(((str(num)*4)[:4],num))
    tmp.sort(reverse=True)

    answer = []
    for n in tmp:
        answer.append(n[1])
    return ''.join(map(str,answer))
print(solution(numbers))

