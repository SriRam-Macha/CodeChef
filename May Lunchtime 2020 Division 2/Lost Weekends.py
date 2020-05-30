for _ in range(int(input())):
    L = [int(i) for i in input().split()]
    sumL = sum(L[:5]) * L[5]
    print(sumL)
    if sumL <= 120:
        print("No")
    else:
        print("Yes") 