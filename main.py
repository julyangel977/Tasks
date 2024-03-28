# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, description, due_date, status=False):
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"{self.description}, Выполнить до: {self.due_date}, {'Done' if self.status else 'Not Done'}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, status=False):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status]
        if current_tasks:
            print("Невыполненные задачи: ")
            for task in current_tasks:
                print(task)
        else:
            print("Все задачи выполнены.")


    description = input("Введите задачу: ")
    due_date = input("Введите срок выполнения: ")
    status = False
    add_task(description, due_date, status)

task_manager = TaskManager()

task_manager.add_task("Послушать урок", "2024-03-27")
task_manager.add_task("Выполнить ДЗ", "2024-03-28")

task_manager.show_current_tasks()

task_manager.mark_task_done("Послушать урок")

task_manager.show_current_tasks()

#     def add_task(self):
#         print(f"Введите новую задачу: {self.description}, срок выполнения: {self.due_date},статус: {self.status}")
#
#
#     def list_tasks(self):
#         if self.status == 'done':
#             None
#         else:
#             print(f'Список невыполненных задач: list[{self.description}, {self.due_date}]')
#
# task1 = Task('Задача 1', 'Поездка к клиенту', '2024-03-23', 'high', 'undone')
# task1.add_task()
# task1.mark_as_done()
# task1.list_tasks()
