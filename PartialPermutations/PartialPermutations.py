from scipy.special import perm
def read(filename):
    with open(filename) as f:
        fileContent = f.read().split()
        n = fileContent[0]
        k = fileContent[1]
        f.close()
        return n, k

def calPartialPermutations(n, k):
    result = perm(n, k)
    print(int(result % 1000000))


if __name__ == "__main__":
    n, k = read("./rosalind_pper.txt")
    calPartialPermutations(int(n), int(k))