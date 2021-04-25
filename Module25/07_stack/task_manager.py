class TaskManager:
    priority_list = list()
    tasks = dict()

    def add_task(self, task, priority):
        if priority in self.priority_list:
            self.tasks[priority].append(task)
        else:
            self.priority_list.append(priority)
            self.tasks[priority] = [task]

    def check_the_same(self, task, priority):
        del_item = False
        add_item = True

        for key, values in self.tasks.items():
            for value in values:
                if value == task:
                    if key < priority:
                        print('\nЗадача уже есть в списке с более высоким приоритетом')
                        add_item = False
                    elif key == priority:
                        print('\nЗадача уже есть в списке с таким же приоритетом')
                        add_item = False
                    else:
                        del_item = True
        if del_item:
            self.delete_task(task)
        if add_item:
            self.add_task(task, priority)

    def new_task(self, task, priority):
        self.check_the_same(task, priority)

    def print(self):
        for key, values in sorted(self.tasks.items()):
            print('\nЗадачи с приоритетом {}:'.format(key))
            for value in values:
                print(value, end=' ')

    def delete_task(self, task):
        empty_list = False
        del_key = 0
        for key, values in self.tasks.items():
            for value in values:
                if value == task:
                    values.remove(value)
                    if len(self.tasks[key]) == 0:
                        empty_list = True
                        del_key = key
        if empty_list:
            self.tasks.pop(del_key)
            self.priority_list.remove(del_key)
