def read(filename):
    with open(filename, "r") as f:
        fileContent = f.read().split("\n")
        nodeNum = fileContent[0]
        nodeConnection = fileContent[1:]
        nodeEdge = [map(int, n.split(" ")) for n in nodeConnection]
        return nodeNum, nodeEdge




if __name__ == "__main__":
    nodeNum, nodeEdge = read("./test.txt")
    print(nodeNum)
    