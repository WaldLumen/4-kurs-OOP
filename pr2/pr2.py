class FacultyNode:
    def __init__(self, name, dean, groups, students):
        self.name = name
        self.dean = dean
        self.groups = groups
        self.students = students
        self.next = None


class University:
    def __init__(self):
        self.head = None

    def add_group(self, name, dean, groups, students):
        new_node = FacultyNode(name, dean, groups, students)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def del_group(self, name):
        current = self.head
        prev = None

        while current:
            if current.name == name:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                print(f"Faculty '{name}' deleted.")
                return
            prev = current
            current = current.next

        print(f"Faculty '{name}' not found.")

    def calc_stud(self, name):
        current = self.head
        while current:
            if current.name == name:
                return current.students
            current = current.next
        return None

    def print_all(self):
        current = self.head
        if current is None:
            print("University has no faculties.")
            return

        print("\nFaculties of University:")
        while current:
            print(
                f"Faculty: {current.name}, "
                f"Dean: {current.dean}, "
                f"Groups: {current.groups}, "
                f"Students: {current.students}"
            )
            current = current.next


uni = University()

uni.add_group("Computer Science", "Ivanenko", 10, 320)
uni.add_group("Mathematics", "Petrenko", 7, 210)
uni.add_group("Physics", "Shevchenko", 5, 150)

uni.print_all()

students = uni.calc_stud("Mathematics")
if students is not None:
    print(f"\nNumber of students on Mathematics faculty: {students}")

uni.del_group("Physics")
uni.print_all()
