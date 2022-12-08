class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prv_node, new_data):
        if prv_node is None:
            raise ValueError
        new_node = Node(new_data)
        new_node.next = prv_node.next
        prv_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def print_list(self):
        item = self.head
        while item:
            print(item.data)
            item = item.next


llist = LinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
llist.head = first
llist.head.next = second
second.next = third
llist.push(0)
llist.insert(second, 9)
llist.append(22)
llist.print_list()
print('*' * 20)
llist.remove(3)
llist.print_list()
