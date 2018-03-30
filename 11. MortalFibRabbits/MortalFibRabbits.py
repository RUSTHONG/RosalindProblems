"""
Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, 

which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches 

maturity in one month and produces a single pair of offspring (one male, one female) each subsequent 

month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the 

case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit 

tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month 

if all rabbits live for m months.
"""
# 智障型解法
def cal(n, m):
    s = [0]*4
    s[0] = 1
    for i in range(1, n):
        s[1:m+1] = s[0:m]
        s[0] = sum(s[2:])
    #print(s)
    print(sum(s[:-1]))

cal(81,19)

"""
优秀的解法
#!/usr/bin/env python
def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in xrange(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)
"""