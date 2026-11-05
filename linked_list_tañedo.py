class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(f"[{current.data}]")
            current = current.next
        result.append("NULL")
        return " -> ".join(result)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_head(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        return None


def run_linked_list_program():
    ll = SinglyLinkedList()
    print(f"Step 1: Set head = NULL --> Output: {ll.display()}")
    print("-" * 50)


    print("[Phase 1: Appending Nodes]")
    letters = ['T', 'A', 'Ñ', 'E', 'D', 'O']
    for idx, letter in enumerate(letters, start=2):
        ll.append(letter)
        print(f"Step {idx}: Add '{letter}' --> Output: {ll.display()}")

    print("\n" + "-" * 50)


    print("[Phase 2: Deleting Head Nodes]")
    for idx in range(8, 14):
        removed = ll.delete_head()
        print(f"Step {idx}: Remove '{removed}' --> Output: {ll.display()}")


if __name__ == "__main__":
    run_linked_list_program()