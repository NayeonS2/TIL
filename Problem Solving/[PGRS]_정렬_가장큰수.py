numbers = [232,23]
def solution(numbers):
    if set(numbers) == {numbers[0]}:
        numbers = list(set(numbers))


    numbers.sort(key=lambda x: (-int((str(x)+'0'*(3-len(str(x))))[-3]),-int((str(x)+'0'*(3-len(str(x))))[-2]),-int((str(x)+'0'*(3-len(str(x))))[-1])))

    return ''.join(map(str,numbers))
print(solution(numbers))

