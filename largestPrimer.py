def primeTester(n):
	if n % 2 == 0 and n!=2:
		return False
	"""by breaking mid-loop it removes unnecessary counting"""
	for i in range(3, n**0.5+1, 2):
		if not n % i:
			return False 
	return True




def largestPrimer(n):
	x = 1
	for i in range(3, n**0.5+1, 2):
		if not n % i and primeTester(i):
			x = i
	return x

print largestPrimer(600851475143)