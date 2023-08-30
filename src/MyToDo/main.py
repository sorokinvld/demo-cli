import typer
from rich.console import Console
from rich.table import Table
from .utils import TodoList, Task  # Update import for the new structure

app = typer.Typer()
console = Console()
todo_list = TodoList()

@app.command()
def add(task_description: str):  # Update parameter name
    """
    Add a task to the ToDo list.
    
    Args:
        task_description (str): The description of the task to add.
    """
    todo_list.add_task(task_description)
    console.print(f"Task [bold green]'{task_description}'[/bold green] added to the ToDo list.")

@app.command()
def list():
    """
    List all tasks in the ToDo list.
    """
    tasks = todo_list.get_tasks()
    if tasks:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Index")
        table.add_column("Task")
        for idx, task in enumerate(tasks, start=1):
            table.add_row(str(idx), task.description)  # Use task.description
        console.print(table)
    else:
        console.print("[italic]ToDo list is empty.[/italic]")

@app.command()
def remove(index: int):
    """
    Remove a task from the ToDo list.
    
    Args:
        index (int): The index of the task to remove.
    """
    removed_task = todo_list.remove_task(index)
    if removed_task is not None:
        console.print(f"Task [bold red]'{removed_task.description}'[/bold red] removed from the ToDo list.")
    else:
        console.print("[italic]Invalid index or ToDo list is empty.[/italic]")

if __name__ == "__main__":
    app()
