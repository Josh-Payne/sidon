import itertools

size = 26

'''
This function uses the Sieve of Eratosthenes method to find all primes under n and returns the largest one.
'''

def largest_prime_below(n):
	primes = range(n)
	for i in range(2,int(n**(0.5))+1):
		if i in primes:
			j = i
			while j*i < n:
				if (j*i in primes):
					primes.remove(j*i)
				j+=1
	return primes.pop()
    
erdos_turan_bound = lambda n: int((n**(0.5))+(2*(n**(0.25)))+10)

# to check
print(erdos_turan_bound(size))
print(largest_prime_below(int(size**(0.5))))

'''
Here, we keep track of all possible sums in A, returning false if there are any duplicates, and true otherwise.
'''
def foundSidonSet(A):
	sums = set()
	for i in range(len(A)):
		for j in range(i,len(A)):
			if A[i]+A[j] in sums:
				return False
			sums.add(A[i]+A[j])
	return True

'''
from class: largest prime below square root of N < max sidon set size below N < Erdos-Turan bound for N.
This tests all integers in that range in reversed order to find the largest Sidon Set.
'''
def largestSidonSet(N):
	print("largest prime below square root of N: ",largest_prime_below(int(size**(0.5))),"Erdos-Turan bound for N: ",min(erdos_turan_bound(N),N))
	for n in reversed(range(largest_prime_below(int(size**(0.5))),min(erdos_turan_bound(N),N))):
		print(n)
		for A in makeSidonSets(n,N):
			if foundSidonSet(A):
				return "size: ", n, A
	return "didn't find any"

'''
makes possible Sidon sets of size n from N.
how can we efficiently generate all the potential Sidon Sets of size n from N?
Omit: 
- sets with n and 2n
- sets with 1, n, n+1; 2, n, n+2; k, n, n+k
- 
'''
def makeSidonSets(n,N):
	print("Checking sets of size ",n," of ",N)
	return set(itertools.combinations(range(1,N+1),n))

print("largest found: ",largestSidonSet(size))
