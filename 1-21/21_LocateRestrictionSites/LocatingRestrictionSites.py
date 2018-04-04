"""
Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement. 

For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. 

See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length 

between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4

"""
import re
def read(filename):
    with open(filename, "r") as f:
        fileContent = ("").join(f.read().split())
        dnaString = re.split(r">Rosalind_\d+", fileContent)
        return dnaString[1]


def reverseString(dnaString):
    reverseDict = {"A":"T", "T":"A", "C":"G", "G":"C"}
    rawList = [reverseDict[n] for n in list(dnaString)]
    rawList.reverse()
    reverseString = ("").join(rawList)
    return reverseString


def locatResSites(dnaString):
    for i in range(4, 13, 2):
        for j in range(0, len(dnaString)-i+1):
            fragment = dnaString[j:j+i]
            if reverseString(fragment) == fragment:
                print(j+1, i)

if __name__ == "__main__":
    filename = "./rosalind_revp.txt"
    dnaString = read(filename)
    #print(reverseString("ATGCAT"))
    locatResSites(dnaString)
