# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree_queue = deque([(p,q)])
        while tree_queue:

            node1, node2 = tree_queue.popleft()
            if node1 == None and node2 == None:
                continue
            
            if node1 == None or node2 == None:
                return False
            
            if node1.val != node2.val:
                return False
            
            tree_queue.append((node1.left,node2.left))
            tree_queue.append((node1.right,node2.right))
        
        return True
        
        