class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        curr = stack.pop()
        result.append(curr.val)

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    return result[::-1]