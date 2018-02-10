class DoublyLinkedList:

    start = None
    end = None
    current = None

    def __init__(self):
        self.start = Node("Start")
        self.current = self.start
        self.end = Node('end')
        self.end.set_previous(self.start)
        self.start.set_next(self.end)

    def get_last_node(self):
        return self.end.get_previous()

    def get_first_node(self):
        return self.start.get_next()

    def add(self, node):
        last_node = self.get_last_node()
        node.set_previous(last_node)
        node.set_next(self.end)
        last_node.set_next(node)
        self.end.set_previous(node)

    def __str__(self):
        str = ""
        self.current = self.get_first_node()
        while self.current.has_next():
            str = str + self.current.text + "\n"
            self.current = self.current.get_next()

        str = str + self.current.text + "\n"
        return str

    def print_back_to_front(self):
        str = ""
        self.current = self.get_last_node()
        while self.current.get_previous():
            str = str + self.current.text + "\n"
            self.current = self.current.get_previous()

        str = str + self.current.text + "\n"
        return str

    def iterate_over_nodes_to_position(self, position):
        self.current = self.get_first_node()
        for x in range(0, position):
            if self.current.has_next():
                self.current = self.current.get_next()
            else:
                raise Exception("%s element not in list" % position)
        return self.current

    def insert(self, position, node):
        next_node = self.iterate_over_nodes_to_position(position=position)
        previous_node = next_node.get_previous()
        node.set_next(node=next_node)
        node.set_previous(node=previous_node)
        next_node.set_previous(node=node)
        previous_node.set_next(node=node)

    def remove(self, position):
        node = self.iterate_over_nodes_to_position(position=position)
        previous_node = node.get_previous()
        next_node = node.get_next()
        next_node.set_previous(node=previous_node)
        previous_node.set_next(node=next_node)


class Node:

    text = ""

    next = None
    previous = None

    def __init__(self, text):
        self.text = text

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def get_previous(self):
        return self.previous

    def set_previous(self, node):
        self.previous = node

    def set_next(self, node):
        self.next = node

double_list = DoublyLinkedList()
for x in range(0, 12):
    new_node = Node(text="Test %s" % x)
    double_list.add(node=new_node)

print(double_list)

# Print from back to front
print(double_list.print_back_to_front())

#Insert at position
double_list.insert(5, Node("Inserted node"))
print(double_list)

# Remove the 3th node
double_list.remove(3)
print(double_list)