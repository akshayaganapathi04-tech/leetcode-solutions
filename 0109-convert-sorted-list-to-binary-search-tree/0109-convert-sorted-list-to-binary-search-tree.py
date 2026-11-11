class Solution:
    def sortedListToBST(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next

        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(a[m])
            root.left = build(l, m-1)
            root.right = build(m+1, r)
            return root

        return build(0, len(a)-1)       