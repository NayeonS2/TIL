S = input()
# 숫자 덩어리 세서 0,1 중 덩어리 수가 적은쪽
nums = list(S)

temp = []
tmp = ''
i = 0
tmp += nums[i]
while True:

    if i == len(nums)-1:
        temp.append(tmp)
        break
    else:
        try:
            if nums[i] == nums[i+1]:    # 숫자 덩어리 수 구하기
                tmp += nums[i+1]

            else:
                temp.append(tmp)
                tmp = nums[i+1]
            i += 1
        except:
            pass

zero_ = 0
one_ = 0
for dumm in temp:   # 0 덩어리 1 덩어리 갯수 비교
    if '1' in dumm:
        one_+=1
    else:
        zero_+=1
print(min(zero_,one_))



