
phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    answer = True

    nums = {}

    for phone in phone_book:
        temp = ''
        for i in range(len(phone)-1):
            temp += str(phone[i])
            nums[temp] = 1

    for phone in phone_book:
        if phone in nums:
            answer = False
    return answer



print(solution(phone_book))




