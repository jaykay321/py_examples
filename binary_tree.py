class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftchild = None
        self.rightchild = None

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def getLeftChild(self):
        return self.leftchild

    def getRightChild(self):
        return self.rightchild

    def insertLeftChild(self,newNode):
        if not self.leftchild:
            self.leftchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertRightChild(self,newNode):
        if not self.rightchild:
            self.rightchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t

"""
Tree traversal
"""
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

"""
Testing tree
"""

r = BinaryTree("A")
#print(r.getRootVal())
#print(r.getLeftChild())
r.insertLeftChild('B')
r.insertRightChild('C')
r.getLeftChild().insertLeftChild('D')
r.getLeftChild().insertRightChild('E')
r.getRightChild().insertLeftChild('F')
r.getRightChild().insertRightChild('G')

print(preorder(r))
print(inorder(r))
print(postorder(r))
