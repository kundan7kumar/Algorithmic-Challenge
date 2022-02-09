import heapq

maxheap=[]
heapq.heapify(maxheap)
heapq.heappush(maxheap,1*-1)
heapq.heappush(maxheap,3*-1)
heapq.heappush(maxheap,2*-1)
print(maxheap)
peekNum = maxheap[0]
print("peekNum:", peekNum *-1)
popNum=heapq.heappop(maxheap)
print (popNum*-1)
print(maxheap[0]*-1)
print("maxHeap: ", maxheap)
size=len(maxheap)
print(size)