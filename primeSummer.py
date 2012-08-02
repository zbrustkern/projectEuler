def primeTester(n):
	if n % 2 == 0 and n!=2:
		return False
	"""by breaking mid-loop it removes unnecessary counting"""
	for i in range(3, n**0.5+1, 2):
		if not n % i:
			return False 
	return True


def primeSummer(n):
	i = 3
	c = 2
	while i < n:
		if primeTester(i):
			 c += i
		i += 1

	return c

if __name__ == "__main__":
	print primeSummer(2000000)