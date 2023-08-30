from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    """
    Represents a task with a description.
    
    Attributes:
        description (str): The description of the task.
    """
    description: str

class TodoList(BaseModel):
    """
    Represents a list of tasks.
    
    Attributes:
        tasks (List[Task]): The list of tasks.
    """
    tasks: List[Task] = []

    def add_task(self, task_description: str):
        """
        Add a task to the ToDo list.

        Args:
            task_description (str): The description of the task to add.
        """
        new_task = Task(description=task_description)
        self.tasks.append(new_task)

    def get_tasks(self):
        """
        Get the list of tasks.

        Returns:
            List[Task]: The list of tasks.
        """
        return self.tasks

    def remove_task(self, index):
        """
        Remove a task from the ToDo list.

        Args:
            index (int): The index of the task to remove.

        Returns:
            Task or None: The removed task or None if index is invalid.
        """
        if 1 <= index <= len(self.tasks):
            return self.tasks.pop(index - 1)
        return None
