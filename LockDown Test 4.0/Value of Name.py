for _ in range(int(input())):
    S = str(input())
    F = ''
    for i in S:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            F += '0'
        elif i.isalpha():
            F +='1'
    print((int(F,2))%(1000000007))



