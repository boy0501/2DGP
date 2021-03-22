def isPrime(a):
	for i in range(2,a//2):
		if a%i==0:
			return False
	return True
def ispan(a):
	if(a==reverse(a)):
		if(isPrime(a)):
			return True
	else:
		return False
def reverse(a):
	b = str(a)
	result = ""
	for l in range(len(b)):
		result+=b[-l-1]
	return int(result)
good = eval(input())
while(True):
	if(ispan(good)):
		print(good)
		break
	else:
		good+=1
