# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        node = root
        isSubTree = False
        def isSubtreeF(node: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False
            if node.val != subRoot.val:
                return False
            return isSubtreeF(node.left, subRoot.left) and isSubtreeF(node.right, subRoot.right)


        if isSubtreeF(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
