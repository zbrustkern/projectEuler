def primeTester(n):
	if n % 2 == 0 and n!=2:
		return False
	"""by breaking mid-loop it removes unnecessary counting"""
	for i in range(3, n**0.5+1, 2):
		if not n % i:
			return False 
	return True

def primeFinder(a):
	if a == 2 or a == 3 or a == 5 or a == 7:
		return a
	#don't bother counting the first four, then...
	i = 11
	c = 4
	while c != a:
		if primeTester(i):
			 c += 1
		i += 1

	return i - 1


if __name__ == "__main__":
	print primeFinder(10001)