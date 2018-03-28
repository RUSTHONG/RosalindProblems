"""
Problem

Given two strings s and t of equal length, the Hamming distance between s and t, 

denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output

7
"""
def openFile(fileName):
    file = open(fileName, "r")
    stringList = file.read().split()
    return stringList


def countDistance(dnaString):
    distance = 0
    for i in range(0, len(dnaString[0])):
        if dnaString[0][i] != dnaString[1][i]:
            distance += 1
            i += 1
    return distance


if __name__ == "__main__":
    fileName = "./rosalind_hamm.txt"
    dnaString = openFile(fileName)
    dnaDistance = countDistance(dnaString)
    print(dnaDistance)

"""
推荐算法：
def mutation_count(x1, x2):
    mutations=0
    for i,j in zip(x1,x2):
        if i != j :
            mutations+=1
    return mutations
"""   
    