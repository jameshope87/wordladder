import sys
# Data Structures
class Node():
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent

class FIFOQueue():
    def __init__(self):
        self.queue = []
    
    def addItem(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop(0)
    
# Helper Functions
def distance(s1, s2):
    score = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            score += 1
    return score

def handleInputs():
    print("Please enter the first word:")
    word1 = input("> ")
    print("Please enter the second word:")
    word2 = input("> ")
    while len(word2) != len(word1):
        print("Please enter the second word that is the same length as word 1:")
        word2 = input("> ")
    return word1.lower(), word2.lower()

def read_words(filename,length):
    wordList = []
    with open(filename) as f:
        words = f.read().lower().splitlines()
        for word in words:
            if len(word) == length:
                wordList.append(word)
    return wordList

def findWordLadder(source, target, words):
    #basically a BFS
    root = Node(source)
    checked = set()
    to_check = FIFOQueue()
    
    checked.add(root.value)
    for word in words:   
        if distance(root.value, word) == 1:
            to_check.addItem(Node(word, root))
            print(len(to_check.queue))
    while to_check.queue:
        node = to_check.dequeue()
        if node.value not in checked:
            for word in words:   
                if distance(node.value, word) == 1:
                    to_check.addItem(Node(word, node))
        if node.value == target:
            ladder = []
            while isinstance(node, Node):
                ladder.append(node.value)
                node = node.parent
            print(ladder)
            break

def mainFunction(source, target, wordList):
    if source not in wordList:
        sys.exit('unknown word in dictionnary: {}'.format(source))
    if target not in wordList:
        sys.exit('unknown word in dictionnary: {}'.format(target))
    findWordLadder(source, target, wordList)
    
if __name__ == "__main__":
    source, target = handleInputs()
    wordList = read_words("words",len(source))
    mainFunction(source, target, wordList)