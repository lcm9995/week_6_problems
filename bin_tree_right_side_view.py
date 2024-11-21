class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack = []
        if root is not None:
            stack.append(root.val)
            rightstack = self.rightSideView(root.right)
            leftstack = self.rightSideView(root.left)
            if rightstack and leftstack:
                if len(leftstack) > len(rightstack):
                    stack += rightstack 
                    stack += leftstack[len(rightstack):]
                else:
                    stack+=rightstack
            elif leftstack: 
                stack += leftstack
            elif rightstack:
                stack +=rightstack
        return stack