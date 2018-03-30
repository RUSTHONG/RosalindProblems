"""
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.

Sample Dataset

AAAACCCGGT

Sample Output

ACCGGGTTTT
"""
def complementingDNA(dnaString):
    dnaList = list(dnaString)
    # 批量替换的方法
    pattern = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complementList = [pattern[x] if x in pattern else x for x in dnaList]
    complementList.reverse() # reverse表示一种方法，不可存入变量
    reversedComplement = ("").join(complementList)
    print(reversedComplement)

if __name__ == "__main__":
    file = open("./rosalind_revc.txt", "r")
    dnaString = file.read()
    complementingDNA(dnaString)
