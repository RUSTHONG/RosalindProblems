def read(filename):
    with open(filename, "r") as f:
        fileContent = f.read().split()
        length = fileContent[0]
        dnaString = fileContent[1]
        arrayA = fileContent[2:]
        f.close()
        return length, dnaString, arrayA


def calExpectedNum(length, dnaString, arrayA):
    for i in arrayA:
        ExpectedNum = 1
        for j in dnaString:
            if j in ["A", "T"]:
                ExpectedNum *= (1-float(i))*0.5
            if j in ["C", "G"]:
                ExpectedNum *= float(i)*0.5
        result = ExpectedNum*(int(length)-len(dnaString)+1)
        print(round(result, 3), end=" ")


if __name__ == "__main__":
    length, dnaString, arrayA = read("./rosalind_eval.txt")
    calExpectedNum(length, dnaString, arrayA)