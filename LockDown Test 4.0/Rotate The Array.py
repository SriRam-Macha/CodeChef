for _ in range(int(input())):
    N,D = [int(i) for i in input().split()]
    ls = [int(i) for i in input().split()]
    print(*ls[-D:] + ls[:-D])