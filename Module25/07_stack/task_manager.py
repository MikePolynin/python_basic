class TaskManager:
    priority_list = list()
    tasks = dict()

    def new_task(self, task, priority):
        if priority in self.priority_list:
            self.tasks[priority].append(task)
        else:
            self.priority_list.append(priority)
            self.tasks[priority] = [task]

    def print(self):
        for key, values in sorted(self.tasks.items()):
            print('\nЗадачи с приоритетом {}:'.format(key))
            for value in values:
                print(value, end=' ')
