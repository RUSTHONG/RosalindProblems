"""
Problem

Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total 

reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading 

the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. 

Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""
import re
def convertDict(convertTable):
    file = open(convertTable, "r").read()
    mediumList = file.split()
    convertDict = {k:v for k,v in zip(mediumList[::2], mediumList[1::2])}
    return convertDict


def read(filename):
    with open(filename, "r") as f:
        stringList = f.read().split()
        del stringList[0]
        dnaString = ("").join(stringList)
        f.close()
        return dnaString


def dnaConvertToRna(dnaString):
    rnaString = dnaString.replace("T", "U")
    return rnaString


def reverseComplememt(dnaString):
    reverseDict = {"A":"T", "T":"A", "C":"G", "G":"C"}
    reverseList = [reverseDict[n] for n in list(dnaString)]
    reverseList.reverse()
    reverseComplememt = ("").join(reverseList)
    return reverseComplememt


def problem(rnaString):
    indice = []
    result = []
    for i in range(len(rnaString)-3):
        if convertDict[rnaString[i:i+3]] == "M":
            indice.append(i)

    for i in indice:
        stopMark = False
        proteinString = ""
        for j in range(i, len(rnaString)-3, 3):
            protein = convertDict[rnaString[j:j+3]]
            if not protein:
                break
            if protein == "Stop":
                stopMark = True
                break
            proteinString += protein
        if stopMark:
            result.append(proteinString)
    return result

if __name__ == "__main__":
    convertTable = "./RnaCodonTable.txt"
    filename = "./rosalind_orf.txt"
    convertDict = convertDict(convertTable)
    dnaString = read(filename)
    reverseDnaString = reverseComplememt(dnaString)
    a = problem(dnaConvertToRna(dnaString))
    b = problem(dnaConvertToRna(reverseDnaString))
    for n in set(a + b):
        print(n)


      

            

        
        
