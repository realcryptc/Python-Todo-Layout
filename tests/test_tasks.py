import os
import json
import pytest
from todo_app.tasks import load_tasks, save_tasks, add_task, list_tasks, complete_task

@pytest.fixture
def temp_tasks_file(monkeypatch):
    temp_file = "test_tasks.json"
    monkeypatch.setattr("todo_app.tasks.TASKS_FILE", temp_file)
    yield temp_file
    if os.path.exists(temp_file):
        os.remove(temp_file)

def test_add_task(temp_tasks_file):
    add_task("Test Task")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test Task"
    assert not tasks[0]["completed"]

def test_complete_task(temp_tasks_file):
    add_task("Test Task")
    complete_task(0)
    tasks = load_tasks()
    assert tasks[0]["completed"]
