from employee import Manager, Agent, Worker


def company():
    manager_1 = Manager('Bob', 'Patterson', 27, 7500)
    manager_2 = Manager('John', '', 30, 3210)
    manager_3 = Manager('Jack', '', 28, 5000)

    agent_1 = Agent('Alice', '', 40, 12000, 50000)
    agent_2 = Agent('Anna', '', 41, 23000, 80000)
    agent_3 = Agent('Maria', '', 42, 22000, 75000)

    worker_1 = Worker('Tom', '', 24, 12000, 20)
    worker_2 = Worker('Andrey', '', 25, 11000, 18)
    worker_3 = Worker('Carl', '', 26, 11500, 19)

    employees_list = [manager_1, manager_2, manager_3, agent_1, agent_2, agent_3, worker_1, worker_2, worker_3]

    for employee in employees_list:
        print(employee.get_name(), 'salary is', employee.get_salary())




company()
