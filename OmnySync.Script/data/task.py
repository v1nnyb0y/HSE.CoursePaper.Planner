from .variables import users, notionData
from notion.collection import Collection


class Task:
    def __init__(self, title, executor, num, time=None, complete=False):
        self.title = title
        self.num = num
        self.time = time
        self.complete = complete
        if isinstance(executor, str):
            self.executor = list(map(
                lambda x: users[x],
                filter(lambda x: x in list(users.keys()),
                       executor.split(';'))
            ))
        else:
            self.executor = executor

    def add_to_notion(self):
        title = f"{self.title} | {self.num}"
        for row in notionData['page'].collection.get_rows():
            if row.Task == title and (len(self.executor) <= 0 or
               row.Person in self.executor):
                return False

        row = notionData['tasks_database'].collection.add_row()
        row.Task = title
        row.Person = self.executor[0] if len(self.executor) > 0 else []
        row.Time = self.time
        row.Complete = self.complete
        return True

    def __str__(self):
        names = []
        for i, u in users.items():
            if u[0] in self.executor:
                names.append(i)

        return f"{self.title}|{';'.join(names)}|" + \
               f"{self.num}|{self.time}|{self.complete}"
