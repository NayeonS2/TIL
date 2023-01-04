def solution(nums):
    temp = {}
    for n in nums:
        n_key = str(n)
        if n_key not in temp:
            temp[n_key] = 1
        else:
            temp[n_key] += 1
    pick = len(nums)//2
    if len(temp) < pick:
        answer = len(temp)
    else:
        answer = pick
    return answer

nums = [3,3,3,2,2,2]

print(solution(nums))