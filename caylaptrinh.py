# Định nghĩa lớp Node để biểu diễn một nút trong cây
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Hàm duyệt cây theo thứ tự trước
def preOrderTraversal(node):
    if node is not None:
        # Duyệt qua nút gốc
        print(node.val)
        # Duyệt qua tất cả các nút con bên trái của nút gốc
        preOrderTraversal(node.left)
        # Duyệt qua tất cả các nút con bên phải của nút gốc
        preOrderTraversal(node.right)