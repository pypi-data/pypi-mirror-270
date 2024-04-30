import math
x = ['A','B', 'C', 'D', 'E', 'F'] 
freq = [40,30,10,10,6,4]

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.nodes = []

freq_node = {}
for i in range(len(x)):
    n = Node()
    n.nodes.append(x[i])
    freq_node[n] = [freq[i],0]


def get_smallest():
    sorted_dict = sorted(freq_node.items(), key=lambda x: (x[1][0], -x[1][1]))

    return sorted_dict[:2]

while len(freq_node)!=1:
    ns1, ns2 = get_smallest()
    n1 = list(ns1)[0]
    n2 = list(ns2)[0]
    v1 = list(ns1)[1][0]
    v2 = list(ns2)[1][0]
    n = Node()
    n.left = n1
    n.right = n2
    n1.parent = n
    n2.parent = n
    n.nodes.extend(n1.nodes)
    n.nodes.extend(n2.nodes)
    del freq_node[n1]
    del freq_node[n2]
    freq_node[n] = [v1+v2, len(n.nodes)]
huffman_codes = {}
for char in x:
    code = ""
    temp = n
    while temp.left or temp.right:
        if char in temp.left.nodes:
            code += "1"

            temp = temp.left
        else:

            temp = temp.right
            code += "0"
    huffman_codes[char] = code
    print(char, "->", code)


def calculate_metrics(freq, huffman_codes):
    total = sum(freq)
    prob = [round(f/total,2) for f in freq]
    len_codes = [len(code) for code in huffman_codes.values()]
    Lavg = 0
    for i in range(len(prob)):
        Lavg += prob[i]*len_codes[i]
    print("--------------------")
    print("Average CodeWord Length: ", Lavg)

    entropy = 0
    for p in prob:
        entropy -= p*math.log2(p)
    print("Entropy: ", entropy)
    print("Efficiency: ", entropy*100/Lavg, "%")
    print("Redundancy:", 1-entropy/Lavg)