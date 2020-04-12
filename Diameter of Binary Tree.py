# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def calc(self, node):
        # Returns (height, best) where height is the height of the tree rooted at the node
        # best is the furthest distance between 2 nodes
        height = best = 0
        if node.left == None:
            if node.right == None:
                height = 1
                best = 0

        lh = lb = 0
        if node.left != None:
            lh, lb = self.calc(node.left)

        rh = rb = 0
        if node.right != None:
            rh, rb = self.calc(node.right)

        height = max(lh, rh) + 1
        best = max(lb, rb, lh + rh + 1)

        return height, best

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.calc(root)[1] - 1





        
