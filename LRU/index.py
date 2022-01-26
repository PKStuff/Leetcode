from linked_list import linkedList
class leastRecentlyUsed:
    def __init__(self, size):
        self.queue = linkedList()
        self.element_map = {}
        self.size = size
    
    def get(self, element):
        if element not in self.element_map:
            return -1
        if element != self.queue.head.data:
            self.queue.delete_item(element)
            self.queue.enqueue(element)
        return self.element_map[element]

    def put(self, element, value):
        if element in self.element_map:
            if element != self.queue.head.data:
                self.queue.delete_item(element)
        else:
            if self.queue.length < self.size:
                pass
            else:
                data = self.queue.dequeue()
                del self.element_map[data]
            self.queue.enqueue(element)
        self.element_map[element] = value
        return True

if __name__ == '__main__':
    lru = leastRecentlyUsed(4)
    print(lru.get(2))
    print(lru.put(2, 20))
    print(lru.get(2))
    print(lru.put(2, 22))
    print(lru.get(2))
    print(lru.put(3, 30))
    print(lru.put(4, 40))
    print(lru.put(5, 50))
    print(lru.get(2))
    print(lru.put(1, 10))
    lru.queue.display()
    print(lru.element_map)
    
