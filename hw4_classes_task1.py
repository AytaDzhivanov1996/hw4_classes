import datetime


class Task:
    def __init__(self, content):
        self.__content = content

    def __str__(self):
        return f'{self.__content} (создано {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})'

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.__content == other.__content
        return NotImplemented

    def __hash__(self):
        return hash(self.__content)


todo_list = set()
todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))

for item in todo_list:
    print(item)
