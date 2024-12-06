#!/bin/bash
echo "Running To-Do App tests..."

# Activate virtual environment
source .venv/bin/activate

# Run tests
pytest tests/

echo "Tests complete."
