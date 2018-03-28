"""
Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset

AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output

MAMAPRTEINSTRING
"""
import re


def processTable(tableFilename):
    file = open(tableFilename, "r").read()
    tableList = re.split(r"\s+", file)
    return tableList


def convertToDict(tableList):
    dictionary = {}
    for (k, v) in zip(tableList[::2], tableList[1::2]):
        dictionary[k] = v
    return dictionary


def splitRnaString(rnaStringFilename):
    rnaString = open(rnaStringFilename, "r").read()
    splitString = [rnaString[i:i+3] for i in range(0, len(rnaString), 3)]
    return splitString

def completeTranslation(splitString, dictionary):
    rnaTranslationString = ("").join([dictionary[x] if x in dictionary.keys() else x for x in splitString])
    return rnaTranslationString


if __name__ == "__main__":
    tableFilename = "./RnaCodonTable.txt"
    tableList = processTable(tableFilename)
    #print(tableList)
    rnaTableDict = convertToDict(tableList)
    #print(rnaTableDict)
    splitString = splitRnaString("./rosalind_prot.txt")
    #print(splitString)
    rnaTranslationString = completeTranslation(splitString, rnaTableDict)
    print(rnaTranslationString)
    