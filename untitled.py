import itertools
import time

N = 148
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

# to check


'''
Here, we keep track of all possible sums in A, returning false if there are any duplicates, and true otherwise.
'''
def foundSidonSet(A,allsets):
	sums = allsets[str(A[:-1])]
	for i in range(len(A)):
		if A[i]+A[-1] in sums:
			return False
		sums.add(A[i]+A[-1])
	allsets[str(A)] = allsets[str(A[:-1])].union(sums)
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
	for n in range(1,2):
		sidonSet = list([n])
		sidonSets.append(sidonSet)
		allsets[str(sidonSet)] = set([n])
	for n in range(1,N):
		cardinalityIncrement = list()
		for sidonSet in sidonSets:
			for i in range(sidonSet[-1]+1,N+1):
				newSidon = sidonSet.copy()
				newSidon.append(i)
				if foundSidonSet(newSidon,allsets):
					cardinalityIncrement.append(newSidon)
		sidonSets = cardinalityIncrement
		
		if n >=12:
			print(cardinalityIncrement)
		print(cardinalityIncrement[0])
		# print(sidonSets)
		# print("Stage: ",n)

	# for n in range(sidonSet[-1],size+1):
	# 	print(n)
	# 	candidate = sidonSet
	# 	candidate.append(n)
	# 	if foundSidonSet(candidate,allsets):
	# 		length = len(candidate)
	# 		if length<=upper_bound:
	# 			if max_size < length:
	# 				max_size = length
	# 			largestSidonSet(candidate)

	# for n in bounds:
	# 	print(n)
	# 	substart = time.time()
	# 	sidonSetsSizeN = makeSidonSets(n,N)
	# 	print(time.time()-substart)
	# 	for A in sidonSetsSizeN:
	# 		if foundSidonSet(A):
	# 			return "size: ", n, A
	# return "didn't find any"

'''
makes possible Sidon sets of size n from N.
how can we efficiently generate all the potential Sidon Sets of size n from N?
Omit: 
- sets with n and 2n
- sets with 1, n, n+1; 2, n, n+2; k, n, n+k
- 
'''
# def makeSidonSets(n,N):
# 	print("Checking sets of size ",n," of ",N)
# 	return list(itertools.combinations(range(1,N+1),n))
start = time.time()
largestSidonSet()
print(time.time()-start)
