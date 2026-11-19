class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if root is None:                    
            return root

        self.invertTree(root.left)          
        self.invertTree(root.right)         
        root.right, root.left = root.left, root.right   
        return root