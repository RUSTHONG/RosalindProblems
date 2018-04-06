"""
Problem

For a collection of strings, a larger string containing every one of the smaller strings as 

a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads 

serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA 

format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to 

reconstruct the entire chromosome from these reads by gluing together pairs of reads that 

overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a 

reconstructed chromosome).

Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample Output
ATTAGACCTGCCGGAATAC
"""
import re
def read(filename):
    with open(filename, "r") as f:
        fileContent = ("").join(f.read().split())
        stringList = re.split(r">Rosalind_\d+", fileContent)
        del stringList[0]
        return stringList


def calUnion(stringList):
    for i in range(0, len(stringList)-1):
        union = list(set(stringList[i]) | set(stringList[i+1]))
    print(union)


if __name__ == "__main__":
    filename = "./test.txt"
    stringList = read(filename)
    calUnion(stringList)