# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums=[]

        def dfs(node):
            if not node:
                return 
            nums.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        nums.sort()
        return nums[k-1]

        

        