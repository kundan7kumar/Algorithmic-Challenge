class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
