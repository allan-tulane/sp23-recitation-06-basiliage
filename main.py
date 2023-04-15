import math, queue
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
  freq = {}
  for char in f:
    freq[char] = freq.get(char, 0) + 1

   
  queue = [Node(char=c, freq=f) for c, f in freq.items()]
  queue.sort(key=lambda n: n.freq)

    # Build the Huffman tree by repeatedly merging nodes with the lowest frequency
  while len(queue) > 1:
    left = queue.pop(0)
    right = queue.pop(0)
    parent = Node(freq=left.freq + right.freq, left=left, right=right)
    queue.append(parent)
    queue.sort(key=lambda n: n.freq)

  return queue[0]

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
 if (node.left == None) and (node.right == None):
        code[node.data[1]] = prefix

    if node.right:
        get_code(node.right, prefix + "1")
    if node.left:
        get_code(node.left, prefix + "0")
    return code
  
    

  


# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
  get_frequencies(f)
    

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
  if not C or not f:
    return None

  cost = 0
  freq = {}
  for char in C:
    freq[char] = freq.get(char,0)+1

  for char, freq in freq.items():
    node = Node(char)
    code_len = len(node.code)
    cost += freq * code_len
  return cost



f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))