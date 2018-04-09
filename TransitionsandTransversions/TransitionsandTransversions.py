import re
transitionList = [("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")]
transversionList = [("A", "C"), ("C", "A"), ("A", "T"), ("T", "A"), 
                     ("C", "G"), ("G", "C"), ("G", "T"), ("T", "G")]

def read(filename):
    with open(filename) as f:
        fileContent = ("").join(f.read().split())
        rawList = re.split(r">Rosalind_\d+", fileContent)
        del rawList[0]
        return rawList


def calRatio(rawList):
    countTransition = 0
    countTransversion = 0
    for i in zip(list(rawList[0]), list(rawList[1])):
        if i in transitionList:
            countTransition += 1
        if i in transversionList:
            countTransversion += 1
    ratio = countTransition/countTransversion
    print("%.11f" % ratio)

if __name__ == "__main__":
    filename = "./rosalind_tran.txt"
    rawList = read(filename)
    calRatio(rawList)
