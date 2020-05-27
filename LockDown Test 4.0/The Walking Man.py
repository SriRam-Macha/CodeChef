t=int(input())
for i in range(t):
    a,b=[int(i) for i in input().split()]
    if a==0:
        b=b*2
    final=pow(a,2)+int(b/2)*2*a+pow(int(b/2)-1,2)+int(b/2)-1
    if b%2!=0:
        final=final+b-1
    print(final%1000000007)