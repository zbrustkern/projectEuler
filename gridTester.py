def gridTester(n):
	with open("eleven.txt", 'r') as f:
		data = [map(int, line.split()) for line in f]
	
	a = 1

	for j in range(0,n,1):
		for i in data[j]:
			if a < i*(i+1)*(i+2)*(i+3)*(i+4):
				a = i*(i+1)*(i+2)*(i+3)*(i+4)

	return a

"""	for j in range(0,n-4,1):
		for i in range(0,n-4,1):
			if (data[j,i]*data[j,(i+1)]*data[j,(i+2)]*data[j,(i+3)]*data[j,(i+4)]) > 0:
				a = data[j,i]*data[j,(i+1)]*data[j,(i+2)]*data[j,(i+3)]*data[j,(i+4)]
"""


if __name__ == "__main__":
	print gridTester(20)