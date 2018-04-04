"""
Problem

A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common 

substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not 

as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC"

and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset

>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC
"""

import re
def find_lcsubstr(s1, s2):   
    m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  #生成0矩阵，为方便后续计算，比字符串长度多了一列  
    mmax=0   #最长匹配的长度  
    p=0  #最长匹配对应在s1中的最后一位  
    for i in range(len(s1)):  
        for j in range(len(s2)):  
            if s1[i]==s2[j]:  
                m[i+1][j+1]=m[i][j]+1  
                if m[i+1][j+1]>mmax:  
                    mmax=m[i+1][j+1]  
                    p=i+1  
    return s1[p-mmax:p] #返回最长子串及其长度


def extractData(filename):
    fileContent = open(filename, "r").read()
    cutSpaceContent = ("").join(fileContent.split())
    rawDataList = re.split(r">Rosalind_\d+", cutSpaceContent)
    del rawDataList[0]
    return rawDataList

def calLongestCommonSubstring(rawDataList):
    for i in range(0, len(rawDataList)-1):
        result = find_lcsubstr(rawDataList[i], rawDataList[i+1])
    return result

if __name__ == "__main__":
    filename = "./rosalind_lcsm.txt"
    rawDataList = extractData(filename)
    result = calLongestCommonSubstring(rawDataList)
    print(result)
    