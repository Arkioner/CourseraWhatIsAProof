from unittest import TestCase

from src.InsertSortedDoubleLinkedList import DoublyLinkedList, sortedInsert

data = [
    ("case insert at the end", [5], 10, [5, 10]),
    ("case insert at the beginning", [5, 6, 7], 1, [1, 5, 6, 7]),
    ("case start a new list", [], 100, [100]),
    ("case insert in the middle", [1, 10], 5, [1, 5, 10]),
]

class TestSuite(TestCase):

    def linked_list_node_to_array(self, node):
        out_list = []
        pointer = node
        while pointer:
            out_list.append(pointer.data)
            pointer = pointer.next
        return out_list

    def array_to_linked_list(self, array):
        out_linked_list = DoublyLinkedList()
        for item in array:
            out_linked_list.insert_node(item)
        return out_linked_list

    def test_sorted_insert_x(self):
        given_list = [5]
        given_element = 10
        expected_list = [5, 10]
        current_list = self.linked_list_node_to_array(sortedInsert(self.array_to_linked_list(given_list).head, given_element))
        self.assertEqual(expected_list, current_list)

    def test_sorted_insert_y(self):
        given_list = [1, 3, 4, 10]
        given_element = 5
        expected_list = [1, 3, 4, 5, 10]
        current_list = self.linked_list_node_to_array(sortedInsert(self.array_to_linked_list(given_list).head, given_element))
        self.assertEqual(expected_list, current_list)

def create_test_function(given_list, given_element, expected_list):
    def _test_func(self):
        self.assertEqual(
            expected_list,
            self.linked_list_node_to_array(sortedInsert(self.array_to_linked_list(given_list).head, given_element))
        )
    return _test_func


for i, (test_case_name, given_list, given_element, expected_list) in enumerate(data):
    setattr(
        TestSuite,
        'test_%s'%test_case_name.replace(" ", "_"),
        create_test_function(given_list, given_element, expected_list)
    )
