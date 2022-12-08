import datetime


class Task:
    def __init__(self, content):
        self.__content = content

    def __repr__(self):
        return f'{self.__content} (создано {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})'

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.__content == other.__content
        return NotImplemented

    def __hash__(self):
        return hash(self.__content)

    def __len__(self):
        return len(self.__content)

    def __bool__(self):
        if len(self.__content) > 0:
            return True
        else:
            return False


todo_list = []
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))

non_empty_tasks = [item for item in todo_list if item]
print(non_empty_tasks)
print(len([item for item in todo_list if not item]))
