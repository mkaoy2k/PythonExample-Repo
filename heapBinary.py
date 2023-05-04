class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2*i + 1

    def rightChild(self, i):
        return 2*i + 2

    def getMin(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)

    def deleteMin(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return min_value

    def heapifyUp(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapifyDown(self, i):
        while self.leftChild(i) < len(self.heap):
            min_child = self.leftChild(i)
            if self.rightChild(i) < len(self.heap) and self.heap[self.rightChild(i)] < self.heap[min_child]:
                min_child = self.rightChild(i)
            if self.heap[i] <= self.heap[min_child]:
                break
            self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child
