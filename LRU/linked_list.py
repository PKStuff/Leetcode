class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    
    def insert_at_last(self, data):
        if self.head == None:
            self.insert_at_first(data)
            return
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.length+=1
    
    def delete_at_first(self):
        data = None
        if self.head == None:
            return None
        elif self.head == self.tail:
            temp_node = self.head
            self.head = self.tail = None
            data = temp_node.data
            del temp_node
        else:
            temp_node = self.head
            self.head = temp_node.next
            data = temp_node.data
            del temp_node
        self.length-=1
        return data
    
    def dequeue(self):
        data = None
        if self.head == None or self.head == self.tail:
            data = self.delete_at_first()
        else:
            temp_node = self.head
            while temp_node.next != self.tail:
                temp_node = temp_node.next
            node_to_delete = self.tail
            self.tail = temp_node
            self.tail.next = None
            data = node_to_delete.data
            del node_to_delete
            self.length-=1
        return data
    
    def delete_from_position(self, position):
        if self.length == 0:
            return -1
        elif position == 1:
            self.delete_at_first()
        else:
            temp_node = self.head
            while position > 2:
                position-=1
                temp_node = temp_node.next
            if not temp_node.next:
                return -1
            node_to_delete = temp_node.next
            if node_to_delete == self.tail:
                self.dequeue()
            else:
                temp_node.next = temp_node.next.next
                del node_to_delete
                self.length-=1
        return True
    
    def delete_item(self, item):
        if self.length == 0:
            return -1
        if self.head == self.tail and self.head.data == item:
            node_to_delete = self.head
            self.head = self.tail = None
            del node_to_delete
            self.length-=1
        elif self.head.data == item:
            self.delete_at_first()
        else:
            temp_node = self.head
            while temp_node.next.data != item:
                temp_node = temp_node.next
            if temp_node.next == self.tail:
                self.dequeue()
            else:
                node_to_delete = temp_node.next
                temp_node.next = temp_node.next.next
                del node_to_delete
                self.length-=1

    def display(self):
        if self.head == None:
            return
        temp_node = self.head
        while temp_node != self.tail:
            print(temp_node.data, end="->")
            temp_node = temp_node.next
        print(self.tail.data)

if __name__ == '__main__':
    l1 = linkedList()
    l1.enqueue(1)
    l1.enqueue(2)
    l1.insert_at_last(3)
    l1.insert_at_last(4)
    l1.display()
    l1.delete_item(2)
    l1.display()
    print(l1.length)