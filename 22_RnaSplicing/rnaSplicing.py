"""
Problem

After identifying the exons(外显子) and introns(内含子) of an RNA string, we only need to delete the introns and concatenate(串联) the 

exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings 

are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will 

exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""
import re
def convertDict(convertTable):
    file = open(convertTable, "r").read()
    mediumList = file.split()
    convertDict = {k:v for k,v in zip(mediumList[::2], mediumList[1::2])}
    return convertDict


def dnaConvertToRna(dnaString):
    rnaString = dnaString.replace("T", "U")
    return rnaString


def transToProtein(rnaString, convertDict):
    proteinStirng = ""
    for i in range(0, len(rnaString)-3+1, 3):    
        proteinStirng += convertDict[rnaString[i:i+3]] if convertDict[rnaString[i:i+3]] != 'Stop' else ""
    print(proteinStirng)


def extractdnaString(filename):
    with open(filename, "r") as f:
        fileContent = ("").join(f.read().split())
        rawList = re.split(r">Rosalind_\d+", fileContent)
        del rawList[0]
        return rawList

if __name__ == "__main__":
    convertTable = "./RnaCodonTable.txt"
    convertDict = convertDict(convertTable)
    filename = "./rosalind_splc.txt"
    dnaList = extractdnaString(filename)
    dnaString = dnaList[0]
    for i in dnaList[1:]:
        dnaString = dnaString.replace(i, '')
    rnaString = dnaConvertToRna(dnaString)
    transToProtein(rnaString, convertDict)
