# Setting Up Python in VS Code with WSL (Windows Subsystem for Linux)

This guide explains how to set up Python development in VS Code when you have VS Code installed on Windows but want to use Ubuntu through WSL.

## Prerequisites

1. Windows 11 with WSL (Windows Subsystem for Linux) and Ubuntu installed
2. Visual Studio Code installed on Windows (not on Ubuntu)
3. Python installed on your Ubuntu WSL environment

## Step 1: Install VS Code Extensions for WSL

The key to using VS Code with Ubuntu WSL is the Remote - WSL extension. This allows VS Code (installed on Windows) to connect to your Ubuntu environment without installing VS Code in Ubuntu.

1. Open VS Code on Windows
2. Go to Extensions view (click the Extensions icon in the Activity Bar or press Ctrl+Shift+X)
3. Install the following extensions:
   - **Remote - WSL** (by Microsoft) - This is critical for connecting VS Code to your Ubuntu environment
   - **Python** (by Microsoft)
   - **Jupyter** (by Microsoft)
   - **Pylance** (by Microsoft)

> **Important Note**: We are NOT installing VS Code on Ubuntu. Instead, we're using the VS Code Remote - WSL extension to connect your Windows VS Code installation to the Ubuntu WSL environment. All extensions should be installed directly in VS Code on Windows, not through scripts in Ubuntu.

1. Open VS Code on Windows
2. Install the following extensions:
   - **Remote - WSL** (by Microsoft) - This is critical for connecting VS Code to your Ubuntu environment
   - **Python** (by Microsoft)
   - **Jupyter** (by Microsoft)
   - **Pylance** (by Microsoft)

## Step 2: Connect VS Code to Ubuntu WSL

### Method 1: From VS Code

1. Click on the green button in the bottom-left corner of VS Code
2. Select "Connect to WSL" from the menu
3. VS Code will reopen connected to your Ubuntu WSL environment
4. You'll know you're connected to WSL when the bottom-left corner shows "WSL: Ubuntu"

### Method 2: From Ubuntu Terminal

1. Open your Ubuntu terminal (from Windows Start menu)
2. Navigate to your project directory:
   ```bash
   cd /path/to/your/project
   ```
3. Launch VS Code from the terminal with:
   ```bash
   code .
   ```
   - This opens VS Code with the current directory as the workspace
   - If this command doesn't work, you need to install the VS Code CLI:
     ```bash
     # In Ubuntu terminal
     cat << EOF >> ~/.bashrc
     # Add Visual Studio Code to PATH
     export PATH="\$PATH:/mnt/c/Users/$USER/AppData/Local/Programs/Microsoft VS Code/bin"
     EOF
     source ~/.bashrc
     ```
   - Note: Adjust the path if VS Code is installed in a different location

## Step 3: Open Your Project Folder in WSL

1. In VS Code (connected to WSL), go to File > Open Folder
2. Navigate to your project folder in the WSL filesystem
   - Note: Your Windows drives are mounted under `/mnt/` in WSL (e.g., `C:` is at `/mnt/c/`)
3. Select the folder and click "OK"

## Step 4: Set Up Python Environment in WSL

1. Open a terminal in VS Code (Terminal > New Terminal)
   - This terminal will be running in your Ubuntu environment
2. Run the setup script:
   ```bash
   python3 setup_environment.py
   ```
3. Follow the instructions to activate your virtual environment:
   ```bash
   source .venv/bin/activate
   ```
4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Step 5: Set Up Jupyter Support

1. With your virtual environment activated in the WSL terminal, run:
   ```bash
   python setup_jupyter.py
   ```
2. This will install Jupyter packages and register your kernel

## Step 6: Test Your Setup

1. **Test Python Script:**

   - Open `number_game.py` in VS Code
   - Run it by clicking the play button in the top-right corner or pressing F5
   - Follow the prompts in the terminal to play the game

2. **Test Jupyter Notebook:**
   - Open `python_basics.ipynb` in VS Code
   - When prompted, select the Python kernel you registered
   - Run the cells by clicking the play button or pressing Shift+Enter

## Troubleshooting WSL-Specific Issues

1. **VS Code Can't Connect to WSL:**

   - Make sure WSL is running (open Ubuntu from the Start menu)
   - Try restarting VS Code
   - Check that the Remote - WSL extension is installed

2. **Python Not Found in WSL:**

   - In your WSL terminal, check if Python is installed: `python3 --version`
   - If not installed, run: `sudo apt update && sudo apt install python3 python3-pip python3-venv`

3. **File Permission Issues:**

   - WSL files should be modified through VS Code connected to WSL or through the WSL terminal
   - Avoid editing WSL files directly from Windows applications

4. **Terminal Shows Windows Command Prompt Instead of Bash:**
   - Make sure you're connected to WSL (check bottom-left corner)
   - Open a new terminal (Terminal > New Terminal)
   - Or select the dropdown in the terminal and choose "Ubuntu (WSL)"

Remember that when working with WSL, you're essentially working in two separate environments: Windows and Linux. VS Code bridges these environments, but it's important to understand which environment you're working in at any given time.
