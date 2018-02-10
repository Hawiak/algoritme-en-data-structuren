class SingleListList:
    start = None
    current = None

    def __init__(self):
        self.start = Node("Start")
        self.current = self.start

    def get_first_node(self):
        return self.start.get_next()

    def get_last_node(self):
        while self.current.has_next():
            self.current = self.current.get_next()
        return self.current

    def get_node_at_position(self, position):
        return self.iterate_over_nodes_to_position(position)

    def get_node_before_position(self, position):
        return self.iterate_over_nodes_to_position(position - 1)

    def get_node_after_position(self, position):
        return self.iterate_over_nodes_to_position(position + 1)

    def iterate_over_nodes_to_position(self, position):
        self.current = self.get_first_node()
        for x in range(0, position):
            if self.current.has_next():
                self.current = self.current.get_next()
            else:
                raise Exception("%s element not in list" % position)
        return self.current

    def add(self, node):
        last_node = self.get_last_node()
        last_node.set_next(node)

    def remove(self, position):
        node = self.get_node_before_position(position=position)
        node.set_next(self.get_node_after_position(position=position))

    def insert(self, position, node):
        current_node = self.get_node_at_position(position=position)
        before_node = self.get_node_before_position(position=position)
        node.set_next(current_node)
        before_node.set_next(node)

    def __str__(self):
        str = ""
        self.current = self.get_first_node()
        while self.current.has_next():
            str = str + self.current.text + "\n"
            self.current = self.current.get_next()

        str = str + self.current.text + "\n"
        return str


class Node:
    text = ""
    next = None

    def __init__(self, text):
        self.text = text

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def has_next(self):
        if self.next is not None:
            return True
        return False


single_list = SingleListList()
for x in range(0, 12):
    new_node = Node(text="Test %s" % x)
    single_list.add(node=new_node)

print(single_list)

# remove the 8th element
single_list.remove(8)
print(single_list)


# Insert at 6
single_list.insert(6, Node("Test node"))
print(single_list)