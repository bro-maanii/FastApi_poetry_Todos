from fastapi.testclient import TestClient
from fastapi_poetry_todos.main import app


client = TestClient(app)

def test_create_todo():
    todo_data = {"title": "Test Todo2", "description": "This is a test todo2"}
    response = client.post("/api/todos", json=todo_data)
    assert response.status_code == 200
    assert response.json() == "successfully created"

def test_get_todos():
    response = client.get("/api/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_todo():
    todo_id = 5  # Assuming there's a todo with ID 1 in the test database
    response = client.delete(f"/api/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json() == "deleted"

def test_update_todo():
    todo_id = 6  # Assuming there's a todo with ID 1 in the test database
    todo_data = {"title": "Updated Todo", "description": "This is an updated todo"}
    response = client.put(f"/api/todos/{todo_id}", json=todo_data)
    assert response.status_code == 200
    assert response.json() == "updated"
