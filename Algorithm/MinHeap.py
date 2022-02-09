class MinHeap:
    def __init__(self,heapSize):
        self.heapsize=heapSize
        self.minheap = [0] * (heapSize + 1)
        self.realSize = 0
