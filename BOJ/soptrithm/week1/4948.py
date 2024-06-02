import sys
import math
input = sys.stdin.readline

N = 246912
prime = [1 for i in range(N+1)]
prime[1] = 0 # 1은 소수도, 합성수도 아니므로

for i in range(2, int(math.sqrt(N))+1):
	if prime[i] == 1:
		j = 2
		while i*j <= N:
			prime[i*j] = 0
			j += 1

while True:
	n = int(input())
	if n == 0:
		break
	print(sum(prime[n+1:2*n+1]))