from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class EulerTraversal:
    def __init__(self):
        self.euler_tour = []
        self.depth = []
        self.first_occurence = {}
        self.last_occurence = {}

    def dfs(self, node: Optional[TreeNode], depth: int):
        if not node:
            return

        if node.val not in self.first_occurence:
            self.first_occurence[node.val] = len(self.euler_tour)

        self.euler_tour.append(node.val)
        self.depth.append(depth)
        self.last_occurence[node.val] = len(self.euler_tour) - 1

        if node.left:
            self.dfs(node.left, depth + 1)
            self.euler_tour.append(node.val)
            self.depth.append(depth)
            self.last_occurence[node.val] = len(self.euler_tour) - 1

        if node.right:
            self.dfs(node.right, depth + 1)
            self.euler_tour.append(node.val)
            self.depth.append(depth)
            self.last_occurence[node.val] = len(self.euler_tour) - 1

    def display(self, root: Optional[TreeNode]) -> list:
        self.dfs(root, 0)
        return self.euler_tour

    def treeToArray(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        """Converts the tree into array format."""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)  # Add left child or None if missing
                queue.append(node.right)  # Add right child or None if missing
            else:
                result.append(None)

        # Trim trailing Nones for a cleaner output (to simulate a complete tree representation)
        while result and result[-1] is None:
            result.pop()

        return result

    def printTreeArray(self, root: Optional[TreeNode]):
        """Prints the tree in array format."""
        array_representation = self.treeToArray(root)
        print("Tree in Array Format:", array_representation)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = EulerTraversal()
print(solution.printTreeArray(root))
print(solution.display(root))
print(solution.first_occurence)
print(solution.last_occurence)
