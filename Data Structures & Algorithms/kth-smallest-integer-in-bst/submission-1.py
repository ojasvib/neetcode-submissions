# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return
        ans = 0
        def inorder(node):
            if node.left:
                inorder(node.left)
            #inorder(node)
            nonlocal k
            k -= 1
            if k == 0:
                nonlocal ans
                ans = node.val
                return
            if node.right:
                inorder(node.right)
        inorder(root)
        return ans
