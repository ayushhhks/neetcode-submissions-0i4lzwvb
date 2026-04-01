# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
     def validate(root,low=float('-inf'), high=float('inf')):
        if root is None:
            return True
        if not(low<root.val<high):
            return False
        return (validate(root.left, low,  root.val) and validate(root.right, root.val, high))
     return validate(root)

        

        
#         8
#        / \
#       7   10
#      / \  / \
#     6  7.5 9  11


#     class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def is_valid_bst(root):
#     def validate(node, low=float('-inf'), high=float('inf')):
#         if not node:
#             return True
#         # Current node must be within bounds
#         if not (low < node.val < high):
#             return False
#         # Left subtree: upper bound is current node value
#         # Right subtree: lower bound is current node value
#         return (validate(node.left, low, node.val) and
#                 validate(node.right, node.val, high))
    
#     return validate(root)