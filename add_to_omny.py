from data.variables import notionData, INSTALL_PATH
from data.task import Task


def take_rows():
    page = notionData['tasks_database']
    with open(f'{INSTALL_PATH}/data/tmp/data.txt', 'w') as f:
        for row in page.collection.get_rows():
            title, num = row.Task.split(' | ')
            task = Task(
                title,
                row.Person,
                num,
                60 * (row.Time or 0),
                1 if row.Сompleted else 0
            )
            f.write(str(task) + '\n')


if __name__ == "__main__":
    take_rows()
