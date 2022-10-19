fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
           "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

def solution(fees,records):
    origin_time, origin_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]

    info = dict()

    for record in records:
        when, who, how = record.split()
        info[str(who)] = []
    for record in records:
        when, who, how = record.split()
        info[str(who)].append(when) # 차량번호를 key로해서 출차 시간을 value로 append

    for key,values in info.items(): # 출차기록이 홀수이면
        if len(values) % 2 == 1:
            values.append('23:59')  # out 시간 추가

    ans = dict()
    for key,values in info.items():
        total_time = 0
        total_fee = 0
        for i in range(0,len(values),2):
            in_, out_ = values[i:i+2][0], values[i:i+2][1]
            in_h,in_m = map(int,in_.split(':'))
            out_h,out_m = map(int,out_.split(':'))
            if out_m-in_m < 0:  # 누적시간 계산
                out_h -= 1
                out_m += 60
                total_time += (out_m-in_m)
                total_time += (out_h-in_h)*60
            else:
                total_time += (out_m-in_m)
                total_time += (out_h-in_h)*60

        if total_time <= origin_time:   # 금액 계산
            total_fee += origin_fee
        else:
            total_fee += origin_fee
            extra_time = total_time - origin_time
            extra_fee = -(-extra_time//unit_time)*unit_fee  # 올림
            total_fee += extra_fee

        ans[key] = total_fee
    answer = []
    for key,value in sorted(ans.items()):   # 차량번호로 오름차순해서 value 출력
        answer.append(value)
    return answer





print(solution(fees,records))