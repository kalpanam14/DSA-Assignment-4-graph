from collections import deque

def count_nodes_at_level(tree, level):
    if level < 1:
        return 0

    queue = deque([(tree, 1)])  # Queue for BFS traversal
    count = 0

    while queue:
        node, current_level = queue.popleft()

        if current_level == level:
            count += 1

        if current_level > level:
            break

        for child in node.children:
            queue.append((child, current_level + 1))

    return count
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Create a sample tree
root = TreeNode('A')
node1 = TreeNode('B')
node2 = TreeNode('C')
node3 = TreeNode('D')
node4 = TreeNode('E')
node5 = TreeNode('F')

root.children = [node1, node2]
node1.children = [node3, node4]
node2.children = [node5]

level = 2
count = count_nodes_at_level(root, level)
print(f"Number of nodes at level {level}: {count}")