# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            ans.append(q[-1].val)
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans
# q - [1]
# while - 1st exec - curr - 1, q - []. ans- [1], q -[2, 3]
# while - 2nd exec - curr - 2, q-[3], q-[] 
