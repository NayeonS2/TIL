# 무지의 먹방 라이브 (실패)

food_times = [4,2,1,5,3,1,2,10]
k = 5

def solution(food_times, k):
    i = 0
    t = 0
    while True:
        answer = i % len(food_times)

        if set(food_times) == {0}:
            break
        else:
            if t == k:
                if set(food_times) == {0}:
                    return -1
                else:
                    i = answer
                    while i <= len(food_times)-1:
                        if food_times[i] > 0:
                            return i + 1
                        else:
                            i += 1

            if food_times[answer] > 0:
                food_times[answer] -= 1

                t += 1
                i += 1
            else:
                i += 1

    return -1

print(solution(food_times,k))