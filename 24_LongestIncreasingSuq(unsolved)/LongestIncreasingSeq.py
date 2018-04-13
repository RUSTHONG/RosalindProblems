"""
Problem
A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, 

(5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. 

For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing 

subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

Sample Dataset
5
5 1 4 2 3

Sample Output
1 2 3
5 4 2
"""
# -*- coding: utf-8 -*-
from math import ceil
def BinarySearchLEQ(S, data, value):
	'''Use a binary search to return the index of the smallest item in 'S' greater than or equal to 'value'.'''
	original_S = S
	while len(S)>1:
		# index is the exact middle if odd, and the lower value if even.
		index = int(ceil(len(S)/2.0 - 1))
		if data[S[index]] < value:
			S = S[index+1:]

		else:
			S = S[:index+1]

	return original_S.index(S[0])


def LongestIncSubstring(data):
	'''Returns an ordered list of the longest increasing substring.'''
	S = [0]
	parent = [None]*len(data)

	for index in range(1,len(data)):

		if data[index] > data[S[len(S)-1]]:
			parent[index] = S[len(S)-1] 
			S.append(index)

		else:
			update_index = BinarySearchLEQ(S, data, data[index])
			S[update_index] = index
			parent[index] = S[update_index-1] 

	# Get the indicies of each element in the longest increasing subsequence in reverse order.
	LIS = [S[len(S)-1]]
	for i in range(0,len(S)-1):
		LIS.append(parent[LIS[len(LIS)-1]])
	
	# Convert indicies to values and reverse.
	LIS = [data[i] for i in LIS]
	LIS.reverse()
	
	return LIS


if __name__ == '__main__':

	with open('./rosalind_lgis.txt') as input_data:
		perm = map(int, input_data.readlines()[1].split())

	LIS = map(str, LongestIncSubstring(perm))

	# The longest decreasing subsequence is just the longest increasing subsequence of -1*permutation.  
	negperm = [-1*i for i in perm]
	LDS = map(str, [-1*i for i in LongestIncSubstring(negperm)])

	with open('./LGIS.txt', 'w') as output_data:
		output_data.write(' '.join(LIS) + '\n')
		output_data.write(' '.join(LDS))
    

    
