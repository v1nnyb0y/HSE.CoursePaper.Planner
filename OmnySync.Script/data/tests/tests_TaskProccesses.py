import unittest
from task import Task

class TestTaskProcesses(unittest.TestCase):
    def test_Process_AddToNotion(self):
        task = Task('Task1', 'Vadim Zhdanov;Ivan Ivanov', '12', '12', 1)
        task.add_to_notion()
        pass

    def test_Process_ToStr(self):
        task1 = Task('Task1', 'Vadim', '12', '12', 1)
        taskStr = str(task1)
        self.assertEqual(taskStr, 'Task1||12|12|1')

    def test_Process_ToStrWithMultipleExecutors(self):
        task1 = Task('Task1', 'Vadim;Itan', '12', '12', 1)
        taskStr = str(task1)
        self.assertEqual(taskStr, 'Task1||12|12|1')

    def test_Process_AddToNotionWithNotFoundUser(self):
        task = Task('Task1', 'Vadim Zhdanov;Ivan Ivanov;Test', '12', '12', 1)
        task.add_to_notion()    


if __name__ == '__main__':
    unittest.main()
    