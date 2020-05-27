def binomialCoefficient(n, k): 
	if (k > n - k): 
		k = n - k 
	res = 1
	for i in range(k): 
		res = res * (n - i) 
		res = res / (i + 1) 
	return res 
def totalnumberofways(n): 
	c = binomialCoefficient(2*n, n) 
	return c/(n + 1) 
for _ in range(int(input())):
    S = str(input())
    S = "".join(S.split())
    print(int(totalnumberofways(len(S) - 1))%(1000000007))
 
