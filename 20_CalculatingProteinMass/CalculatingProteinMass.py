def read(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
        rawList = fileContent.split()
        monoDict = {k:v for (k,v) in zip(rawList[::2], rawList[1::2])}
        f.close()
        return monoDict


def calMass(filename, monoDict):
    with open(filename, "r") as f:
        fileContent = f.read().replace("\n", "")
        weightList = [float(monoDict[n]) for n in list(fileContent)]
        proteinMass = sum(weightList)
        return proteinMass


if __name__ == "__main__":
    monoMassTable = "./MonoMassTable.txt"
    monoDict = read(monoMassTable)
    proteinMass = calMass("./rosalind_prtm.txt", monoDict)
    print("%.3f" % proteinMass)