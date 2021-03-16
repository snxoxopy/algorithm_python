class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        # index.next = new_node
        # new_node.next = next_node
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            #head를 없앤다는 의미
            self.head = self.head.next

        node = self.get_node(index - 1)
        node.next = node.next.next
        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!

#print(linked_list.get_node(1).data)
linked_list.add_node(1, 6)
linked_list.print_all()