from itertools import permutations
def read(filename):
    with open(filename, "r") as f:
        fileContent = int(f.read())
        f.close()
        return fileContent


def calSignedPermutation(fileContent):
    rawList = [n for n in range(1, fileContent+1)]
    dataList = rawList + [-n for n in rawList]
    permutationList = list(permutations(dataList, fileContent))
    overlapList = []
    for i in permutationList:
        for j in i:
            if -j in i:
                overlapList.append(i)
                continue
    result = set(permutationList) - set(overlapList)
    with open("./output.txt", "w") as out:
        out.write(str(len(result)))
        for n in result:
            out.write("\n" + (" ").join(map(str, n)))



if __name__ == "__main__":
    filename = "./rosalind_sign.txt"
    fileContent = read(filename)
    calSignedPermutation(fileContent)
