# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).


# Taken the code from the Module - 3

def isPrime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif n % 2 == 0:
		return False
	else:
		for i in range(3, n):
			if n % i == 0:
				return False
		return True

def count_digits(k):
	return len(str(k))
	# cnt = 0
	# while k > 0:
	# 	cnt += 1
	# 	k = k // 10
	# return cnt

def rotateNumber(k, cntDigits):
	# unitsDigit = k % 10
	# k = k // 10
	# k = unitsDigit * (10 ** (cntDigits-1)) + k
	# return k
	s = str(k)
	unitsDigit = s[-1]
	s = unitsDigit + s[0:len(s) - 1]
	return int(k)

print (rotateNumber(19, 2))
print (rotateNumber(91, 2))
print (rotateNumber(3412, 4))
print (rotateNumber(2341, 4))

def does_contain_zero(k):
	k = str(k)
	for i in k:
		if i == '0':
			return True
	return False

def isCircularPrime(k):
	cntDigits = count_digits(k)
	if cntDigits == 1 and isPrime(k):
		return True
	else:
		cnt = 0
		while cnt < cntDigits:
			if not isPrime(k):
				return False
			k = rotateNumber(k, cntDigits)
			cnt += 1
		if (cnt == cntDigits):
			return True
	return False

def nthcircularprime(n):
	k = 2
	cnt = -1
	while True:
		if (does_contain_zero(k)):
			k += 1
			continue
		if isCircularPrime(k):
			cnt += 1
		if cnt == n:
			break
		k += 1
	return k


# print(nthCircularPrime(int(input())))
