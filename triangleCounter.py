def factorCounter(n):
	f = 0
	for i in range(1, n+1, 1):
		if not n % i:
			f +=1
	return f

def triangleCounter(n):
	a = 1
	i = 2
	j = 1

	while a <= n:
		a = factorCounter(j)
		print j
		j += i
		i += 1
	return a

if __name__ == "__main__":
	print triangleCounter(200)