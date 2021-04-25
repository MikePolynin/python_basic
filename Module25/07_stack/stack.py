class Stack:
    new_stack = list()

    def add_elem(self, elem):
        self.new_stack.append(elem)

    def delete_elem(self, elem):
        for i in range(len(self.new_stack), self.new_stack.index(elem), -1):
            self.new_stack.remove(i)

    def show_stack(self):
        for elem in self.new_stack:
            print(elem)
