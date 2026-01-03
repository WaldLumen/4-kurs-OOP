class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        if not self.head:
            self.head = SNode(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = SNode(data)

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def remove_first_even(self):
        prev = None
        cur = self.head
        while cur:
            if cur.data % 2 == 0:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return
            prev = cur
            cur = cur.next

    def clear(self):
        self.head = None


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: float):
        if not self.head:
            self.head = DNode(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        new = DNode(data)
        cur.next = new
        new.prev = cur

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def insert_after(self, target: float, value: float):
        cur = self.head
        while cur:
            if cur.data == target:
                new = DNode(value)
                new.next = cur.next
                new.prev = cur
                if cur.next:
                    cur.next.prev = new
                cur.next = new
                return
            cur = cur.next

    def clear(self):
        self.head = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_balanced_tree(values):
    if not values:
        return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = build_balanced_tree(values[:mid])
    root.right = build_balanced_tree(values[mid + 1:])
    return root


def print_tree(root, level=0):
    if root:
        print_tree(root.right, level + 1)
        print("   " * level + str(root.data))
        print_tree(root.left, level + 1)


def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def tree_to_sorted_list(root, arr):
    if root:
        tree_to_sorted_list(root.left, arr)
        arr.append(root.data)
        tree_to_sorted_list(root.right, arr)


def build_bst_from_tree(root):
    arr = []
    tree_to_sorted_list(root, arr)
    arr.sort()
    return build_balanced_tree(arr)


slist = SinglyLinkedList()
for x in [1, 3, 5, 8, 7, 10]:
    slist.append(x)
slist.print_list()
slist.remove_first_even()
slist.print_list()
slist.clear()

dlist = DoublyLinkedList()
for x in [1.1, 2.2, 3.3, 4.4]:
    dlist.append(x)
dlist.print_list()
dlist.insert_after(2.2, 9.9)
dlist.print_list()
dlist.clear()

values = ["d", "b", "f", "a", "c", "e", "g"]
tree = build_balanced_tree(values)
print_tree(tree)
print("Leaves:", count_leaves(tree))
bst = build_bst_from_tree(tree)
print_tree(bst)
