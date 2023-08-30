import pytest
from typer.testing import CliRunner
from MyToDo.main import app
#from .main import app

runner = CliRunner()

@pytest.fixture
def clear_todo_list():
    app.models.todo_list.tasks = []  # Clear tasks before each test
    yield
    app.models.todo_list.tasks = []  # Clear tasks after each test

def test_add_task():
    result = runner.invoke(app, ["add", "Buy groceries"])
    assert result.exit_code == 0
    assert "Task 'Buy groceries' added to the ToDo list." in result.output

def test_list_tasks():
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "Index" in result.output
    assert "Task" in result.output


def test_remove_task():
    runner.invoke(app, ["add", "Do laundry"])
    result = runner.invoke(app, ["remove", "1"])
    assert result.exit_code == 0
    assert "Task 'Do laundry' removed from the ToDo list." in result.output
