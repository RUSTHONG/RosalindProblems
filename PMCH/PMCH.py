from math import factorial
def read(filename):
    with open(filename, "r") as f:
        fileContent = f.read().split()
        rnaString = ("").join(fileContent[1:])
        return rnaString


def calPMCH(rnaString):
    pmch = factorial(rnaString.count("A"))*factorial(rnaString.count("C"))
    return pmch


if __name__ == "__main__":
    rnaString = read("./rosalind_pmch.txt")
    pmch = calPMCH(rnaString)
    print(pmch)