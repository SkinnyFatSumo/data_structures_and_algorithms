class BinaryTreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

    def hasLeft(node):
        if node.left == None:
            return False
        return True
    
    def hasRight(node):
        if node.right == None:
            return False
        return True

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root

    def hasLeft(self):
        if self.left == None:
            return False
        return True
    
    def hasRight(self):
        if self.right == None:
            return False
        return True

    def insertIterative(self, val):
        newNode = BinaryTreeNode(val)
        curNode = self.root

        if self.isEmpty():
            self.root = newNode
            return
        while curNode != None:
            if newNode.val < curNode.val:
                if not curNode.hasLeft(): 
                    curNode.left = newNode
                    return
                curNode = curNode.left

            if newNode.val > curNode.val:
                if not curNode.hasRight(): 
                    curNode.right = newNode
                    return
                curNode = curNode.right

            
    def isEmpty(self):
        if self.root == None:
            return True
        return False

tree = BinarySearchTree()

for number in [10, 4, 2, 9, 1, 21, 14, 19, 8]:
    tree.insertIterative(number)

def printTreeLevels(root):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)




printTreeLevels(tree.root)



