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


class TodoList:
    def __init__(self):
        self.__tasks = [None, None]

    def __repr__(self):
        return f'{self.__tasks}'

    def __setitem__(self, key, value):
        self.__tasks[key] = value

    def __getitem__(self, item):
        return self.__tasks[item]

    def __delitem__(self, key):
        del self.__tasks[key]


todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')
