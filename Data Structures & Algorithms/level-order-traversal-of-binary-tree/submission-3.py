# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return [] 

        res=[]
        q = collections.deque()
        q.append(root)

        while q:
            level=[]
            qlen=len(q)

            for i in range(qlen):
                
                cur = q.popleft()

                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

                    level.append(cur.val)

            if level:
                res.append(level)

        return res        