


class TwoWayNode():
    def __init__(self,data=None,next=None,previous=None) -> None:
        self.data = data
        self.next = next
        self.previous = previous


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = TwoWayNode(data,None,None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data

"""

from node_based_queue import Queue

food = Queue()
food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')

print(food.head.data)
print(food.head.next.data)
print(food.tail.data)
print(food.tail.previous.data)
print(food.count)

print(food.dequeue())
print(food.head.data)
"""