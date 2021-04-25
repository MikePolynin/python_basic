from stack import Stack
from task_manager import TaskManager


def stack():
    my_stack = Stack()

    my_stack.add_elem(1)
    my_stack.add_elem(2)
    my_stack.add_elem(3)
    my_stack.add_elem(4)
    my_stack.add_elem(5)

    my_stack.delete_elem(3)

    my_stack.show_stack()


def task_manager():
    manager = TaskManager()

    manager.new_task('wash', 2)
    manager.new_task('make food', 3)
    manager.new_task('eat', 2)
    manager.new_task('buy food', 1)

    manager.print()


stack()
task_manager()
