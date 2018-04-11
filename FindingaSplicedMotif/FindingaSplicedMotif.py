import re
def read(filename):
    with open(filename, "r") as f:
        fileContent = ("").join(f.read().split())
        rawList = re.split(r">Rosalind_\d+", fileContent)
        del rawList[0]
        return rawList


def findSplicedMotif(rawList):
    j = 0
    for i in range(len(rawList[0])):
        if rawList[0][i] == rawList[1][j]:
            print(i+1, end=" ")
            if j == len(rawList[1])-1:
                break
            else:
                j += 1

if __name__ == "__main__":
    rawList = read("./rosalind_sseq.txt")
    findSplicedMotif(rawList)
    