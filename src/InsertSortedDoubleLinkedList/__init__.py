#!/bin/python3


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep):
    if node:
        print(str(node.data)),
        if node.next:
            print(sep),
        print_doubly_linked_list(node.next, sep)


# Given the head of a sorted linked list of nodes put the new node data at the correct position keeping the order.
def sortedInsert(head, new_node_data):
    if head:
        if head.data > new_node_data:
            # case for new element goes first
            new_head = DoublyLinkedListNode(new_node_data)
            new_head.next = head
            head.prev = new_head
            head = new_head
        else:
            # case for element goes between two or at the tail
            pointer = head
            while pointer.next and pointer.next.data <= new_node_data:
                pointer = pointer.next
            insert_node_after(pointer, new_node_data)
    else:
        # case for empty DoubleLinkedList
        head = DoublyLinkedListNode(new_node_data)
    return head


# Function that given the previous node and the new node data generates the new node pointing previous and next nodes
# and modifies both to point to the new node on their respective properties.
def insert_node_after(previous_node, new_node_data):
    node = DoublyLinkedListNode(new_node_data)

    node.prev = previous_node
    node.next = previous_node.next
    previous_node.next = node
    if node.next:
        node.next.prev = node


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        list_count = int(input())

        list = DoublyLinkedList()

        for _ in range(list_count):
            list_item = int(input())
            list.insert_node(list_item)

        data = int(input())

        list_head = sortedInsert(list.head, data)

        print_doubly_linked_list(list_head, ', ')
        print('\n')
