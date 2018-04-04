"""
Problem

A matrix is a rectangular table of values divided into rows and columns. An m*n matrix has m rows and n columns. 

Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4*n 

matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, 

P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each 

position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of 

the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible 

consensus strings.

            A T C C A G C T
            G G G C A A C T
            A T G G A T C T
DNA Strings A A G C A A C C
            T T G G A A C T
            A T G C C A T T
            A T G G C A C T

        A   5 1 0 0 5 5 0 0
Profile	C   0 0 1 4 2 0 6 1
        G   1 1 6 3 0 1 0 0
        T   1 5 0 0 0 1 1 6

Consensus   A T G C A A C T

"""
import re
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

file = open("./rosalind_cons.txt", "r").read().replace("\n", "")

def cut(rawData):
    rawDataList = re.split(r">Rosalind_\d+", rawData)
    del rawDataList[0]
    return rawDataList


def convertToMatrix(rawDataList):
    rawDataList = [list(n) for n in rawDataList]
    dataMatrix = np.array(rawDataList).T.tolist()
    return dataMatrix


def calProfile(processedList):
    baseList = ["A", "C", "G", "T"]
    for n in baseList:
        result = [str(i.count(n)) for i in processedList]
        print("%s: %s" %(n, (" ").join(result)))


def calConsensus(processedList):
    baseList = ["A", "C", "G", "T"]
    #profileList = []
    df = DataFrame()
    for n in baseList:
        List = [i.count(n) for i in processedList]       
        df[n] = Series(List)
    for value in df.idxmax(axis=1):
        print(value, end="")
    
    
    
if __name__ == "__main__":   
    rawDataList = cut(file)
    processedList = convertToMatrix(rawDataList)
    calConsensus(processedList)
    print(" ")
    calProfile(processedList)

