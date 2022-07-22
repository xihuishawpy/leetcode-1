# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p or q:
            return (
                self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
                if p and q and p.val == q.val
                else False
            )

        else: return True
