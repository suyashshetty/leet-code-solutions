class TreeNode:
    def __init__(self, val:int):
        self.val = val
        self.left = None
        self.right = None
        
    def build_tree_from_array(self, arr: [int]):
        def helper(index):
            # Base case: If index is out of bounds or the value is None
            if index >= len(arr) or arr[index] is None:
                return None

            # Create the current node
            node = TreeNode(arr[index])

            # Recursively build left and right children
            node.left = helper(2 * index + 1)
            node.right = helper(2 * index + 2)

            return node

        return helper(0)
        
        
    
def diameterOfBinaryTree(root: TreeNode) -> int:
    maxDiameter = 0
    
    def dfs(node: TreeNode):
        nonlocal maxDiameter
        
        if not node:
            return 0
        
        leftHeight = dfs(node.left)
        rightHeight  = dfs(node.right)
        
        maxDiameter = max(maxDiameter, leftHeight + rightHeight)
        
        return 1 + max(leftHeight, rightHeight)
    
    dfs(root)
    return maxDiameter


def main():
    root = TreeNode(1)
    root = root.build_tree_from_array([3, 9, 2, 1, 4, None, None, None, 5])
    print(diameterOfBinaryTree(root))
    
main()
        