class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

class BinomialHeap:
    def __init__(self):
        self.trees = []
    
    def insert(self, key):
        new_node = Node(key)
        new_heap = BinomialHeap()
        new_heap.trees.append(new_node)
        self.merge(new_heap)
    
    def extract_min(self):
        if not self.trees:
            return None
        min_node = min(self.trees, key=lambda x: x.key)
        self.trees.remove(min_node)
        new_heap = BinomialHeap()
        new_heap.trees = min_node.children[:]
        self.merge(new_heap)
        return min_node.key
    
    def merge(self, other_heap):
        self.trees += other_heap.trees
        self.trees.sort(key=lambda x: len(x.children))
        self.combine_trees()
    
    def combine_trees(self):
        if not self.trees:
            return
        combined = [self.trees.pop(0)]
        for tree in self.trees:
            if tree.key < combined[-1].key:
                combined.append(tree)
            else:
                combined[-1].children.append(tree)
                tree.parent = combined[-1]
        self.trees = combined[:]
