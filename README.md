# Python Development Environment Setup

This project contains everything you need to set up a Python development environment in Visual Studio Code on Ubuntu (WSL), with support for running Python scripts and Jupyter notebooks.

> **Important**: If you're using VS Code on Windows with Ubuntu through WSL, please refer to the [WSL Setup Guide](wsl_setup_guide.md) for specific instructions.

## Files in this Project

- `docs/wsl_setup_guide.md` - Specific instructions for using VS Code with WSL (Windows Subsystem for Linux)
- `docs/python_environment_setup.md` - Detailed instructions for setting up your Python environment
- `setup_environment.py` - Helper script to set up a Python virtual environment
- `setup_jupyter.py` - Helper script to set up Jupyter notebook support
- `number_game.py` - A simple number guessing game to test Python script execution
- `python_basics.ipynb` - A sample Jupyter notebook to test notebook functionality
- `requirements.txt` - List of Python packages required for this project:
  - `ipykernel` and `jupyter` - Required for Jupyter notebook functionality
  - `numpy`, `pandas`, `matplotlib` - Used in the sample notebook for data manipulation and visualization
  - `pylint` and `autopep8` - Code linting and formatting tools for better code quality
- `.vscode/settings.json` - VS Code settings for Python development
- `.vscode/launch.json` - VS Code launch configurations for running Python scripts

## Quick Start Guide

1. **Install VS Code Extensions**

   - Open VS Code on Windows
   - Go to Extensions (Ctrl+Shift+X)
   - Search for and install:
     - Remote - WSL (by Microsoft)
     - Python (by Microsoft)
     - Jupyter (by Microsoft)
     - Pylance (by Microsoft)
     - IntelliCode (by Microsoft)

2. **Set Up Python Environment** (One-time Setup)

   - Open a terminal in VS Code connected to WSL (Terminal > New Terminal)
   - The terminal should show that you're in your Ubuntu WSL environment
   - Run the setup script:
     ```bash
     # Run in VS Code's WSL terminal (one-time setup)
     python3 setup_environment.py
     ```
   - This script will:
     1. Create a Python virtual environment
     2. Ask you to activate the virtual environment
     3. Install required packages
     4. Register a Jupyter kernel
   - When prompted, activate your virtual environment:
     ```bash
     # Run this when the script prompts you
     source .venv/bin/activate
     ```
   - After activation, the script will continue automatically
   - Note: You only need to run setup_environment.py once for initial setup, but you'll need to activate the virtual environment (source .venv/bin/activate) each time you open a new terminal

3. **Optional: Additional Jupyter Setup**

   - The setup_environment.py script already sets up Jupyter support
   - If you need to set up Jupyter separately, you can run:
     ```bash
     # Only needed if you want to set up Jupyter separately
     # Run in VS Code's WSL terminal with virtual environment activated
     python setup_jupyter.py
     ```
   - This script will install Jupyter packages and register your kernel for use with VS Code

4. **Test Python Script Execution**

   - Open `number_game.py` in VS Code connected to WSL
   - Run it by clicking the play button in the top-right corner or pressing F5
   - Follow the prompts in the VS Code terminal to play the number guessing game

5. **Test Jupyter Notebook**
   - Open `python_basics.ipynb` in VS Code connected to WSL
   - When prompted, select the Python kernel you registered
   - Run the cells by clicking the play button or pressing Shift+Enter

## Troubleshooting

If you encounter any issues:

1. **Python Interpreter Not Found**

   - Press Ctrl+Shift+P
   - Type "Python: Select Interpreter"
   - Choose the Python interpreter in your virtual environment

2. **Jupyter Notebook Not Working**

   - Make sure you've installed the Jupyter extension
   - Ensure your virtual environment is activated
   - Try running `setup_jupyter.py` again

3. **Virtual Environment Issues**
   - If the virtual environment isn't working, try creating it manually in your Ubuntu WSL terminal:
     ```bash
     # Run these commands in your Ubuntu WSL terminal
     python3 -m venv .venv
     source .venv/bin/activate
     ```

## Daily Workflow After Setup

Once you've completed the initial setup, here's your typical workflow for Python development:

1. **Start VS Code and Connect to WSL**

   - Open VS Code on Windows
   - Click the green button in the bottom-left corner
   - Select "Connect to WSL" (or open VS Code directly from your Ubuntu terminal with `code .`)

2. **Activate Your Virtual Environment**

   - Open a terminal in VS Code (Terminal > New Terminal)
   - Activate the virtual environment:
     ```bash
     # Run this each time you open a new VS Code WSL terminal
     source .venv/bin/activate
     ```
   - You'll see `(.venv)` at the beginning of your terminal prompt when it's activated

3. **Work on Python Files**

   - Open Python files in VS Code
   - Run scripts with the play button or F5
   - Debug with breakpoints as needed

4. **Work with Jupyter Notebooks**
   - Open .ipynb files in VS Code
   - Select your registered kernel if prompted
   - Run cells with the play button or Shift+Enter

## Additional Resources

For more detailed information, refer to the `python_environment_setup_plan.md` and `wsl_setup_guide.md` files, which contain comprehensive instructions for setting up your Python development environment.
