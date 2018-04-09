#coding=utf-8
# math.log(x) 就相当于数学中的ln(x)，x>0，求底数为e的对数，e = 2.718281828459；
# math.log10(x) 就相当于数学中的lg(x)，x>0，求底数为10的对数；
from math import log10
def read(filename):
    with open(filename, "r") as f:
        fileContent = f.read().split()
        stringList = fileContent[0]
        arrayA = fileContent[1:]
        arrayA = map(float, arrayA)
        return stringList, arrayA


def calComLog(stringList):
    codon_count = [0, 0]
    for i in stringList:
        if i in ["A", "T"]:
            codon_count[0] += 1
        if i in ["C", "G"]:
            codon_count[1] += 1
    return codon_count


def calArrayB(codon_count):
    result = []
    for gc_value in arrayA:
        valueB = codon_count[0]*log10(0.5*(1-gc_value)) + codon_count[1]*log10(0.5*gc_value)
        result.append(str(round(valueB, 3)))
    print((" ").join(result))

if __name__ == "__main__":
    stringList, arrayA = read("./rosalind_prob.txt")
    codon_count = calComLog(stringList)
    calArrayB(codon_count)