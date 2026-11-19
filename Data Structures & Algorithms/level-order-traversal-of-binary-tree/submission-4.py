# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        stack=[]
        q=collections.deque()
        q.append(root)

        while q or stack:
            level=[]
            qlen=len(q)

            for _ in range(qlen):
                cur = q.popleft()
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                    stack.append(cur.val)
            
                while stack:
                    level.append(stack.pop())
            
            if level:
                res.append(level)
            
        return res
        