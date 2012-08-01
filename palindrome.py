def threeDigit(n):
	for i in range(101,999,1):
		if not n % i and (n / i) < 999:
			return True
	return False

def palindrome():
	for i in xrange(998001,100001,-1):
		if str(i)[0] == str(i)[5] and str(i)[1] == str(i)[4] and \
		str(i)[2] == str(i)[3] and threeDigit(i):
			return i

print palindrome()