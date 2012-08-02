
def lcm(a, b):
	n = a
	while n % b != 0:
		n += a
	return n

def oneToTwenty():
	num = lcm(11,12)

	for i in range(13, 20, 1):
		num = lcm(num, i)
	return num

if __name__ == "__main__":
	print oneToTwenty()
