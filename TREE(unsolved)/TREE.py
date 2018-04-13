def read(filename):
    with open(filename, "r") as f:
        fileContent = f.read().split("\n")
        nodeNum = fileContent[0]
        nodeConnection = fileContent[1:]
        nodeEdge = [map(int, n.split()) for n in nodeConnection]
        del nodeEdge[-1]
        return nodeNum, nodeEdge


def produceTree(nodeNum, nodeEdge):
    connected_nodes = [{i} for i in range(1, int(nodeNum)+1)]
    for edge in nodeEdge:
        temp_nodes = set()
        del_nodes = []
        for nodes in connected_nodes:
            if (edge[0] in nodes) and (edge[1] in nodes):
                break
            elif (edge[0] in nodes) or (edge[1] in nodes):
                temp_nodes.update(nodes) 
                del_nodes.append(nodes)
                if len(del_nodes) == 2:
                    break
        if len(del_nodes) != 0:
            temp_nodes.add(edge[0])
            temp_nodes.add(edge[1])
            for nodes in del_nodes:
                connected_nodes.remove(nodes)
            connected_nodes.append(temp_nodes)
    print(len(connected_nodes)-1)

if __name__ == "__main__":
    nodeNum, nodeEdge = read("./rosalind_tree.txt")
    produceTree(nodeNum, nodeEdge)
    