N = int(input())
S = bin(N).replace("0b", "")
print(int(S[::-1],2))
