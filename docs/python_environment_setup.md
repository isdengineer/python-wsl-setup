# Python Environment Setup in VS Code on Ubuntu (WSL)

This document provides detailed instructions for setting up a Python development environment in Visual Studio Code on Ubuntu running on Windows, with support for both Python scripts and Jupyter notebooks.

## 1. Install Python Extensions for VS Code

1. Open VS Code
2. Click on the Extensions icon in the Activity Bar (or press `Ctrl+Shift+X`)
3. Search for and install the following extensions:
   - **Python** (by Microsoft) - Main Python extension
   - **Pylance** (by Microsoft) - Language server with rich type information
   - **Jupyter** (by Microsoft) - For Jupyter notebook support
   - **IntelliCode** (by Microsoft) - AI-assisted code completions

## 2. Configure Python Interpreter in VS Code

1. Open VS Code
2. Press `Ctrl+Shift+P` to open the Command Palette
3. Type "Python: Select Interpreter" and select it
4. Choose your installed Python version from the list
   - If you don't see your Python installation, click "Enter interpreter path" and navigate to your Python executable (typically `/usr/bin/python3`)

## 3. Set Up a Virtual Environment for Python Development

Virtual environments keep your project dependencies isolated. Here's how to set one up:

1. Open a terminal in VS Code (Terminal > New Terminal)
2. Navigate to your project directory:
   ```bash
   mkdir -p ~/python_projects/number_game
   cd ~/python_projects/number_game
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
4. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
5. Your terminal prompt should change to indicate the active environment
6. Install basic packages:
   ```bash
   pip install ipykernel numpy pandas matplotlib
   ```

## 4. Configure VS Code for Running Python Scripts

1. Create a new Python file in your project:
   - Click File > New File
   - Save it as `hello.py`
   - Add a simple print statement: `print("Hello, Python in VS Code!")`
2. Run the script:
   - Right-click in the editor and select "Run Python File in Terminal"
   - Alternatively, click the play button in the top-right corner
3. Configure launch settings (optional):
   - Press `Ctrl+Shift+P` and type "Python: Debug Configuration"
   - Select "Python File" to create a basic debug configuration

## 5. Create a Number Guessing Game Script

Create a new file called `number_game.py` with the following content:

```python
import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts_left = 7
    attempts_made = 0
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {attempts_left} attempts.")
    
    while attempts_left > 0:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts_made += 1
            attempts_left -= 1
            
            # Check the guess
            if guess < secret_number:
                print(f"Too low! You have {attempts_left} attempts left.")
            elif guess > secret_number:
                print(f"Too high! You have {attempts_left} attempts left.")
            else:
                print(f"Congratulations! You guessed the number in {attempts_made} attempts!")
                return
                
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Game over! The number was {secret_number}.")

if __name__ == "__main__":
    play_game()
    
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        play_game()
```

To run the game:
1. Right-click in the editor and select "Run Python File in Terminal"
2. Follow the prompts in the terminal to play the game

## 6. Set Up Jupyter Notebook Support in VS Code

1. Ensure you have the Jupyter extension installed
2. Make sure your virtual environment has the necessary packages:
   ```bash
   pip install jupyter ipykernel
   ```
3. Register your virtual environment as a Jupyter kernel:
   ```bash
   python -m ipykernel install --user --name=number_game_env
   ```

## 7. Create a Sample Jupyter Notebook

1. Create a new file with the `.ipynb` extension:
   - Click File > New File
   - Save it as `python_basics.ipynb`
2. VS Code will open it in notebook mode
3. Click the "+ Code" button to add a new code cell
4. Try some basic Python commands:
   ```python
   # Cell 1
   print("Hello from Jupyter in VS Code!")
   ```
   ```python
   # Cell 2
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Generate some data
   x = np.linspace(0, 10, 100)
   y = np.sin(x)
   
   # Create a plot
   plt.figure(figsize=(10, 6))
   plt.plot(x, y)
   plt.title('Sine Wave')
   plt.xlabel('x')
   plt.ylabel('sin(x)')
   plt.grid(True)
   plt.show()
   ```
5. Run cells by clicking the play button or pressing Shift+Enter

## Troubleshooting

### If Python interpreter is not detected:
- Ensure Python is installed: `python3 --version`
- If needed, install Python: `sudo apt update && sudo apt install python3 python3-pip python3-venv`

### If Jupyter notebooks don't work:
- Check if Jupyter is installed: `pip list | grep jupyter`
- Reinstall Jupyter packages: `pip install --force-reinstall jupyter notebook ipykernel`

### If VS Code extensions have issues:
- Try reloading VS Code: Press `Ctrl+Shift+P`, type "Reload Window" and select it

## Additional Tips

1. **Code Linting**: Install and configure linters for code quality
   ```bash
   pip install pylint flake8
   ```

2. **Code Formatting**: Install and configure formatters
   ```bash
   pip install black autopep8
   ```

3. **Git Integration**: Use VS Code's built-in Git features for version control

4. **Keyboard Shortcuts**:
   - `F5`: Start debugging
   - `Ctrl+F5`: Run without debugging
   - `Shift+Enter`: Run current cell in Jupyter notebook
   - `Alt+Enter`: Run cell and insert below in Jupyter notebook