import unittest
from task import Task

class TestTaskCreationProcess(unittest.TestCase):
    def test_TaskCreationProcess_WithoutTitle(self):
        with self.assertRaises(TypeError):
            task = Task()

    def test_TaskCreationProcess_WithoutExecutor(self):
        with self.assertRaises(TypeError):
            task = Task('Task1')

    def test_TaskCreationProcess_WithoutNum(self):
        with self.assertRaises(TypeError):
            task = Task('Task1', 'Vadim Zhdanov')

    def test_TaskCreationProcess_MinAvailableCreation(self):
        task = Task('Task1', 'Vadim Zhdanov', 12)
        self.assertEqual(task.title, 'Task1')
        self.assertEqual(task.num, 12)

    def test_TaskCreationProcess_FullCreation(self):
        task = Task('Task1', 'Vadim Zhdanov', 12, 12, 1)
        self.assertEqual(task.title, 'Task1')
        self.assertEqual(task.num, 12)
        self.assertEqual(task.time, 12)
        self.assertEqual(task.complete, 1)

    def test_TaskCreationProcess_MultipleExecutors(self):
        task = Task('Task1', 'Vadim Zhdanov;Ivan Ivanov', 12, 12, 1)
        self.assertEqual(task.title, 'Task1')
        self.assertEqual(task.num, 12)
        self.assertEqual(task.time, 12)
        self.assertEqual(task.complete, 1)

    def test_TaskCreationProcess_ExecutorNotFound(self):
        task = Task('Task1', 'Vadim Zhdanov;Ivan Ivanov;Test', 12, 12, 1)
        self.assertEqual(task.title, 'Task1')
        self.assertEqual(task.num, 12)
        self.assertEqual(task.time, 12)
        self.assertEqual(task.complete, 1)

if __name__ == '__main__':
    unittest.main()