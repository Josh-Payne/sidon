import time

N = 50
max_size = 0

'''
This function uses the Sieve of Eratosthenes method to find all primes under n and returns the largest one.
'''

def largest_prime_below(n):
	primes = list(range(n))
	for i in range(2,int(n**(0.5))+1):
		if i in primes:
			j = i
			while j*i < n:
				if (j*i in primes):
					primes.remove(j*i)
				j+=1
	return primes.pop()
    
erdos_turan_bound = lambda n: int((n**(0.5))+(2*(n**(0.25)))+10)

'''
Here, we keep track of all possible sums in A, returning false if there are any duplicates, and true otherwise.
'''
def foundSidonSet(A,allsets):
	sums = allsets[str(A[:-1])].copy()
	for i in range(len(A)):
		# for j in range(i,len(A)):
		if A[i]+A[-1] in sums:
			return False
		sums.add(A[i]+A[-1])
	allsets[str(A)] = sums
	return True

'''
from class: largest prime below square root of N < max sidon set size below N < Erdos-Turan bound for N.
This tests all integers in that range in reversed order to find the largest Sidon Set.
'''
def largestSidonSet():
	upper_bound = erdos_turan_bound(N)
	lower_bound = largest_prime_below(int(N**0.5))
	sidonSets = list()
	allsets = dict()
	for n in range(1,upper_bound-int(upper_bound/2)):
		sidonSet = list([n])
		sidonSets.append(sidonSet)
		allsets[str(sidonSet)] = set([n])
	for n in range(2,upper_bound):
		cardinalityIncrement = list()
		for sidonSet in sidonSets:
			if sidonSet[-1] <= N-max((8-n),0):
				for i in range(sidonSet[-1]+1,N+1):
					newSidon = sidonSet.copy()
					newSidon.append(i)
					if foundSidonSet(newSidon,allsets):
						cardinalityIncrement.append(newSidon)
			allsets.pop(str(sidonSet),None)

		sidonSets = cardinalityIncrement
		print(len(sidonSets))
		if (n>7):
			print(sidonSets)

# def makeSidonSets(n,N):
# 	print("Checking sets of size ",n," of ",N)
# 	return list(itertools.combinations(range(1,N+1),n))
start = time.time()
largestSidonSet()
print(time.time()-start)
