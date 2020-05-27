for _ in range(int(input())):
    N = int(input())
    ingrediants = list(map(int, input().split()))
    templist,counter,count,temp = [],[],0,1
    ingrediants.append(-100)
    for i in range(N):
        if ingrediants[i]!=ingrediants[i+1]:
            if ingrediants[i] not in templist and count not in counter:
                templist.append(ingrediants[i])
                counter.append(count)
                count = 0
            else:
                temp =0
                break
        else:
            count += 1
    if temp != 0:
        print('YES')
    else:
        print('NO')

    