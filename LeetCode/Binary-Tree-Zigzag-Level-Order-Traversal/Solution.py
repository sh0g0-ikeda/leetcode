# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        def dbs(node,lev):

            if not node:
                return

            if len(ans)==lev:
                ans.append([])

            ans[lev].append(node.val)
            dbs(node.left, lev+1)
            dbs(node.right, lev+1)
        
        
        dbs(root, 0)
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i].reverse()
        return ans

        

            