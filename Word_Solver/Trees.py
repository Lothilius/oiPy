# Files: Trees.py
#
# Description: Creates a Tree sturcture.

class BinaryTree:
    """A BinaryTree really is just a pointer to a BinaryTreeNode."""

    def __init__(self, root=None):
        """To create a tree, pass a pointer to a BinaryTreeNode;
            defaults to None.
        """
        self._root = root

    def isEmpty(self):
        return self._root is None

    def getRoot(self):
        return self._root

    def setRoot(self, node):
        self._root = node
        return self._root


class BinaryTreeNode:
    """A BinaryTreeNode has three fields:
        - a value, which can be arbitrary
        - a left pointer to another BinaryTreeNode
        - a right pointer to another BinaryTreeNode
    """

    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def getValue(self):
        return self._value

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setLeft(self, newNode):
        self._left = newNode
        return self._left

    def setRight(self, newNode):
        self._right = newNode
        return self._right

    def isLeafNode(self):
        return not self._left and not self._right

    # Find depth of the node
    def nodeDepth(node, v):
        if node.getValue() == v:
            return 1
        elif v < node.getValue():
            if not node.getLeft():
                return 1
            else:
                node = node.getLeft()
                return 1 + node.nodeDepth(v)
        elif v > node.getValue():
            if not node.getRight():
                return 1
            else:
                node = node.getRight()
                return 1 + node.nodeDepth(v)


class BinarySearchTree(BinaryTree):
    """Extends BinaryTree """

    def __init__(self):
        BinaryTree.__init__(self)

    def inTreeAux(node, value):
        if node.getValue() == value:
            comparisins = node.nodeDepth(value)
            return (True, node.nodeDepth(value))
        elif node.getValue() > value:
            node.nodeDepth(value)
            if not node.getLeft():
                return False
            else:
                return BinarySearchTree.inTreeAux(node.getLeft(), value)
        else:
            node.nodeDepth(value)
            if not node.getRight():
                return False
            else:
                return BinarySearchTree.inTreeAux(node.getRight(), value)

    def inTree(self, item):
        if self.isEmpty():
            return False
        else:
            return BinarySearchTree.inTreeAux(self.getRoot(), item)

    def insertAux(self, node, item):
        if node.getValue() > item:
            if not node.getLeft():
                newNode = BinaryTreeNode(item)
                node.setLeft(newNode)
            else:
                BinarySearchTree().insertAux(node.getLeft(), item)
        else:
            if not node.getRight():
                newNode = BinaryTreeNode(item)
                node.setRight(newNode)
            else:
                BinarySearchTree().insertAux(node.getRight(), item)

    def insert(tree, item):
        if tree.isEmpty():
            tree.setRoot(BinaryTreeNode(item))
        else:
            BinarySearchTree().insertAux(tree.getRoot(), item)