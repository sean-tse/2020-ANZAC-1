import math

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=list(range(3,n+1,2))
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=int((m*m-3)/2)
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def max_prime_diff(n):
    diff = n
    primenums = primes(n+1)
    for i in range(len(primenums)):
        if (n - primenums[i]) in primenums:
            diff = (n - primenums[i]) - primenums[i]
            break
    return diff

def goldbach_steps(n):
    count = 0
    while n > 2:
        n = max_prime_diff(n)
        count += 1
    return count

n = int(input())
print(goldbach_steps(n))