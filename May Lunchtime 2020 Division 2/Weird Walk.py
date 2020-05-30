for _ in range(int(input())):
    N = int(input())
    la = [int(i) for i in input().split()]
    lb = [int(i) for i in input().split()]
    xa = 0
    xb = 0
    dis = 0
    if la[0] == lb[0]:
        dis += la[0]
    xa += la[0]
    xb +=lb[0]
    for i in range(N-1):
        if xa == xb and la[i+1] == lb[i+1]:
            dis += (la[i+1])
        xa += la[i+1]
        xb += lb[i+1]
    print(dis)