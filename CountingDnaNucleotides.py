"""
Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output

20 12 17 21
"""

def count(String):
    sequenceList = list(String)
    numA = 0
    numC = 0
    numG = 0
    numT = 0
    endIndex = len(sequenceList)
    for n in range(0, endIndex):
        if sequenceList[n] == "A":
            numA = numA + 1
        elif sequenceList[n] == "C":
            numC = numC + 1
        elif sequenceList[n] == "G":
            numG = numG + 1
        elif sequenceList[n] == "T":
            numT = numT + 1
    print("A = %d, C = %d, G = %d, T = %d" % (numA, numC, numG, numT))

if __name__ == "__main__":
    String = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    count(String)