# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, description, due_date, status):
        self.description = description
        self.due_date = due_date
        self.status = status

    def add_task(self):
        print(f"Введите новую задачу: {self.description}, срок выполнения: {self.due_date},статус: {self.status}")

    def mark_as_done(self):
        print(f'Задача {self.name} выполнена')
        self.status = 'done'

    def list_tasks(self):
        if self.status == 'done':
            None
        else:
            print(f'Список невыполненных задач: list[{self.description}, {self.due_date}]')

task1 = Task('Задача 1', 'Поездка к клиенту', '2024-03-23', 'high', 'undone')
task1.add_task()
task1.mark_as_done()
task1.list_tasks()
