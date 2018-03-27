"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset

GATGGAACTTGACTACGTAAATT

Sample Output

GAUGGAACUUGACUACGUAAAUU
"""
def transcribingDnaIntoRna(dnaSequence):
    dnaSequenceList = list(dnaSequence)
    endIndex = len(dnaSequenceList)
    for n in range(0, endIndex):
        if dnaSequenceList[n] == "T":
            dnaSequenceList[n] = "U"
            n += 1
    rnaSequence = ("").join(dnaSequenceList)
    print(rnaSequence)

if __name__ == "__main__":
    dnaSequence = "GATGGAACTTGACTACGTAAATT"
    transcribingDnaIntoRna(dnaSequence)

