import re
def read(filename):
    with open(filename, "r") as f:
        fileContent = ("").join(f.read().split())
        rawList = re.split(r">Rosalind_\d+", fileContent)
        del rawList[0]
        f.close()
        return rawList


def MergeMaxOverlap(str_list):
	max_length = -1
	for prefix_index in range(len(str_list)):
		for suffix_index in [num for num in range(len(str_list)) if num != prefix_index]:
			prefix, suffix = str_list[prefix_index], str_list[suffix_index]
			i = 0
			while prefix[i:] != suffix[0:len(prefix[i:])]:
				i += 1
			if len(prefix) - i > max_length:
				max_length = len(prefix) - i
				max_indicies = [prefix_index, suffix_index]

	return [str_list[j] for j in range(len(str_list)) if j not in max_indicies] + [str_list[max_indicies[0]] + str_list[max_indicies[1]][max_length:]]


def LongestCommonSuperstring(str_list):
	while len(str_list) > 1:
		str_list = MergeMaxOverlap(str_list)

	return str_list[0]

if __name__ == "__main__":
    rawList = read("./rosalind_long.txt")
    super_string = LongestCommonSuperstring(rawList)
    with open('./LONG.txt', 'w') as output_data:
        output_data.write(super_string)

"""
def find_lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    mmax = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i+1][j+1] = m[i][j] + 1
                if m[i+1][j+1] > mmax:
                    mmax = m[i+1][j+1]
                    p = i + 1
    LongestSlice = s1[p-mmax:p]
    ShortestSuperstring = 

print(find_lcsubstr("ATTAGACCTG", "CCTGCCGGAA"))
"""