# answer: >Rosalind_6848 53.457172
import re
def cut(rawData):
    pureSequenceSet = re.split(r'>Rosalind_\d+', rawData)
    del pureSequenceSet[0]
    return pureSequenceSet
    

def count(String):
    sequenceList = list(String)
    numC = sequenceList.count("C")
    numG = sequenceList.count("G")
    ratio = (numC+numG)/len(sequenceList)
    return ratio


def calAndCompare(rawString):
    ratioList = [ count(n) for n in pureSequenceSet]
    maxRatioIndex = ratioList.index(max(ratioList))
    return maxRatioIndex, max(ratioList)


def openFile(filename):
    return open(filename, "r")


def clean(file):
    # 去除文章中所有空格的方法
    rawData = ('').join(file.read().split())
    idSet = re.findall(r'>Rosalind_\d+', rawData)
    return rawData, idSet

if __name__ == "__main__":
    filename = "./rosalind_gc.txt"
    file = openFile(filename)
    rawData, idset = clean(file)    
    pureSequenceSet = cut(rawData)
    maxIndex, maxRatio = calAndCompare(pureSequenceSet)
    print(idset[maxIndex])
    print(round(maxRatio*100, 6))
    file.close()
    