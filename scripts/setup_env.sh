#!/bin/bash
echo "Setting up To-Do App environment..."

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Setup complete. Activate the environment with: source .venv/bin/activate"
