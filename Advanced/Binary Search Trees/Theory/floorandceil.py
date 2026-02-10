# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        #your code goes here
        floor = -1
        ceil = -1
        while root:
            if key == root.data:
                return [key,key]
            elif key>root.data:
                floor = root.data
                root = root.right
            elif key<root.data:
                ceil = root.data
                root = root.left
        return [floor,ceil]
