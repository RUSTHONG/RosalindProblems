def read(filename):
    with open(filename, "r") as f:
        fileContent = f.read().split()
        N = int(fileContent[0])
        x = float(fileContent[1])
        dnaString = ("").join(fileContent[2:])
        return N, x, dnaString


def calComLog(dnaString):
    codon_count = [0, 0]
    for i in dnaString:
        if i in ["A", "T"]:
            codon_count[0] += 1
        if i in ["C", "G"]:
            codon_count[1] += 1
    return codon_count


def calMatchingMotif(codon_count, x, N):
    result = ((0.5*(1-x))**codon_count[0])*((0.5*x)**(codon_count[1]))
    print("%.3f" % (1-(1-result)**N))

if __name__ == "__main__":
    N, x, dnaString = read("./rosalind_rstr.txt")
    codon_count = calComLog(dnaString)
    calMatchingMotif(codon_count, x, N)
    
    