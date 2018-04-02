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


convertTable = "./RnaCodonTable.txt"
filename = "./test.txt"
convertDict = convertDict(convertTable)
dnaString = read(filename)
rnaString = dnaConvertToRna(dnaString)

testList = re.findall(r"\b(AUG)\S*?(UAG)\b", rnaString)
print(testList)
"""
i = 0
while i < len(rnaString)-3:
    if rnaString[i:i+3] == "AUG":
        proteinString = ""
        for j in range(i, len(rnaString)-3, 3):
            if rnaString[j:j+3] not in ["UAG", "UAA", "UGA"]:
                proteinString += convertDict[rnaString[j:j+3]]
            else:
                break
        i = j
        print(proteinString)
    i += 1 
                
 


    else:
        while i < len(rnaString)-3:
            if rnaString not in ["UAG", "UAA", "UGA"]:
                proteinString += convertDict[rnaString[i:i+3]]
                i +=3 
            else:
                print(proteinString)
    """            

            

        
        
