size = 5000

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
    
erdos_turan_bound = lambda n: int(n**(0.5)+2*(n**(0.25)+10))

# print(erdos_turan_bound(N))
# print(largest_prime_below(int(math.floor(N**(0.5)))))

'''
Here, we keep track of all possible sums in A, returning false if there are any duplicates, and true otherwise.
'''
def foundSidonSet(A):
	sums = []
	for i in range(len(A)):
		for j in range(i,len(A)):
			if A[i]+A[j] in sums:
				return False
			sums.append(A[i]+A[j])
	return True

'''
from class: square of the largest prime below N < max sidon set size below N < erdos turan bound for N.
This tests all integers in that range in reversed order to find the largest Sidon Set.
'''
def largestSidonSet(N):
	for n in reversed(range(largest_prime_below(N),erdos_turan_bound(N))):
		for A in makeSidonSets(n,N):
			if foundSidonSet(A):
				return n
'''
makes possible Sidon sets of size n from N.
'''
def makeSidonSets(n,N):
	# how can we efficiently generate all the potential Sidon Sets of size n from N? Would we really need to generate N choose n sets?
	return[[]]

print(largestSidonSet(size))
