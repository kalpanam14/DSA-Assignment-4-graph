#Count number of trees in a forest
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def count_trees_in_forest(n, edges):
    uf = UnionFind(n)

    for edge in edges:
        uf.union(edge[0], edge[1])

    trees = set()
    for i in range(n):
        trees.add(uf.find(i))

    return len(trees)

n = 7
edges = [(0, 1), (1, 2), (3, 4), (5, 6)]

num_trees = count_trees_in_forest(n, edges)
print(f"Number of trees in the forest: {num_trees}")