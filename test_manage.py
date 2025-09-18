import pytest
from task_manager import tasks, add_task_logic, remove_task_logic, update_task_logic, get_tasks

# Reset task list before each test
def setup_function():
    tasks.clear()

def test_add_task():
    add_task_logic("Task 1", "Info 1")
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Task 1"
    assert tasks[0]["value"] == "Info 1"

def test_remove_task():
    add_task_logic("Task 1", "Info")
    add_task_logic("Task 2", "Info 2")
    assert remove_task_logic(1) is True
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Task 2"
    # Invalid index
    assert remove_task_logic(5) is False

def test_update_task():
    add_task_logic("Task 1", "Info")
    assert update_task_logic(1, "Updated Info") is True
    assert tasks[0]["value"] == "Updated Info"
    # Invalid index
    assert update_task_logic(5, "Fail") is False

def test_get_tasks():
    add_task_logic("Task 1", "Info")
    copy = get_tasks()
    assert copy == tasks
    copy.append({"name": "Fake", "value": "Fake"})
    assert len(tasks) == 1  # original list unchanged
