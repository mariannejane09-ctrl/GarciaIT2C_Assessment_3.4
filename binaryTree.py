
# BINARY TREE - GARCIA

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the binary tree
root = Node("G")

root.left = Node("A")
root.right = Node("R")

root.left.left = Node("C")
root.left.right = Node("I")

root.right.left = Node("A")


# BFS - Breadth-First Search
def bfs(root):
    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result


# DFS - Depth-First Search
def dfs(root):
    if root is None:
        return []

    return [root.data] + dfs(root.left) + dfs(root.right)


# Display results
print("BINARY TREE - GARCIA")
print("BFS:", " - ".join(bfs(root)))
print("DFS:", " - ".join(dfs(root)))
