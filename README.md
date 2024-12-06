# To-Do App
A simple command-line to-do app to manage your tasks.

## Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/todo_app.git
cd todo_app
```

2. Set up the environment:
```bash
./scripts/setup_env.sh
```

3. Activate the environment:
```bash
Copy code
source .venv/bin/activate
```

## Usage
### Add a Task
```csharp
python -m todo_app.cli add "Buy groceries"
```

### List Tasks
```python
python -m todo_app.cli list
```

### Complete a Task
```python
python -m todo_app.cli complete 0
```

## Testing
Run all tests:

```bash
./scripts/run_tests.sh
```

