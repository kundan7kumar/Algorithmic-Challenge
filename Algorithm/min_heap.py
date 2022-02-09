# create a heap
# Insert element in a heap
# get a top element in heap
# delete the top element in a heap
# get size of heap

import heapq

# create empty array
minheap=[]
# Heapify the array into a Min Heap
heapq.heapify(minheap)
# Inserting element in heap
heapq.heappush(minheap,3)
heapq.heappush(minheap,2)
heapq.heappush(minheap,1)

print("minheap:" ,minheap)


# Get top element
peekNum =minheap[0]
print("peekNum:",peekNum)

# Delete the top element in minHeap
popNum=heapq.heappop(minheap)
print("pop number: ", popNum)

print("peek number: ", minheap[0])
print("minHeap: ", minheap)

size = len(minheap)
print("minHeap size: ", size)
