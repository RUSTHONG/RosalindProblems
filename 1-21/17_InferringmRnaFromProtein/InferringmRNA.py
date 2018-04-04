"""
Problem

For positive integers a and n, a modulo n (written amodn in shorthand) is the remainder（余数） when a is 

divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to 

the modulo operation. We say that a and b are congruent(一致) modulo n if amodn=bmodn; in this case, we 

use the notation a≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

"""
from collections import defaultdict
def convertDict(convertTable):
    file = open(convertTable, "r").read()
    mediumList = file.split()
    convertDict = {k:v for k,v in zip(mediumList[::2], mediumList[1::2])}
    return convertDict

def swapValueAndkey(convertDict):
    d = defaultdict(list)
    for k, v in convertDict.items():
        d[v].append(k)
    return d

def read(filename):
    with open(filename, "r") as f:
        proteinString = f.read()
        proteinList = list(proteinString)
        f.close()
        return proteinList


def calMod(proteinList):
    situList = [len(swapDict[n]) for n in proteinList]
    product = 1
    for i in range(0, len(situList)):
        product *= situList[i]
    mod = product*3 % 1000000
    return mod

if __name__ == "__main__":
    convertDict = convertDict("./RnaCodonTable.txt")
    swapDict = swapValueAndkey(convertDict)
    proteinList = read("./rosalind_mrna.txt")
    del proteinList[-1]
    #print(proteinList)
    result = calMod(proteinList)
    print(result)
