def read(filename):
    with open(filename, "r") as f:
        fileContent = int(f.read())
        return fileContent


if __name__ == "__main__":
    fileContent = read("./rosalind_inod.txt")
    print(fileContent-2)
        