R = int(input())
for _ in range(R):
    a_picture = list(map(int,input().split()))[1:]
    b_picture = list(map(int, input().split()))[1:]


    picture = [4,3,2,1]

    for i in range(len(picture)):
        if a_picture.count(picture[i]) > b_picture.count(picture[i]):
            print('A')
            break
        elif a_picture.count(picture[i]) < b_picture.count(picture[i]):
            print('B')
            break

        if i == 3:
            print('D')