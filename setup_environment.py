#!/usr/bin/env python3
"""
Python Environment Setup Helper Script

This script helps set up a Python virtual environment and install required packages
for development in VS Code, including support for Jupyter notebooks.
"""

import os
import sys
import subprocess
import platform

def print_step(step_num, description):
    """Print a formatted step header."""
    print(f"\n{'='*80}")
    print(f"Step {step_num}: {description}")
    print(f"{'='*80}\n")

def run_command(command, error_message=None):
    """Run a shell command and handle errors."""
    try:
        print(f"Running: {' '.join(command)}")
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        if error_message:
            print(f"Error: {error_message}")
        print(f"Command failed: {' '.join(command)}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main function to set up the Python environment."""
    # Check Python version
    print_step(1, "Checking Python version")
    python_version = platform.python_version()
    print(f"Python version: {python_version}")
    
    if sys.version_info < (3, 6):
        print("Error: Python 3.6 or higher is required.")
        sys.exit(1)
    
    # Create virtual environment
    print_step(2, "Creating virtual environment")
    venv_name = ".venv"
    
    if os.path.exists(venv_name):
        print(f"Virtual environment '{venv_name}' already exists.")
        recreate = input("Do you want to recreate it? (y/n): ").lower()
        if recreate == 'y':
            import shutil
            shutil.rmtree(venv_name)
        else:
            print("Using existing virtual environment.")
            goto_activation = input("Skip to activation step? (y/n): ").lower()
            if goto_activation == 'y':
                goto_step = 3
            else:
                goto_step = 2
            if goto_step > 2:
                goto_packages = True
    
    if not os.path.exists(venv_name):
        success = run_command([sys.executable, "-m", "venv", venv_name],
                             "Failed to create virtual environment.")
        if not success:
            sys.exit(1)
    
    # Activate virtual environment (note: can't be done from within Python)
    print_step(3, "Activating virtual environment")
    if platform.system() == "Windows":
        activate_cmd = f"{venv_name}\\Scripts\\activate"
    else:
        activate_cmd = f"source {venv_name}/bin/activate"
    
    print(f"To activate the virtual environment, run:\n{activate_cmd}")
    print("\nAfter activating, your terminal prompt should change to indicate")
    print("that the virtual environment is active.")
    print("\nIMPORTANT: You need to manually run the activation command above")
    print("before continuing with the next steps.")
    
    # Ask user to confirm activation
    confirm = input("\nHave you activated the virtual environment? (y/n): ").lower()
    if confirm != 'y':
        print("Please activate the virtual environment and run this script again.")
        sys.exit(0)
    
    # Install required packages
    print_step(4, "Installing required packages")
    packages = ["ipykernel", "numpy", "pandas", "matplotlib", "jupyter"]
    
    print(f"Installing packages: {', '.join(packages)}")
    success = run_command([sys.executable, "-m", "pip", "install"] + packages,
                         "Failed to install required packages.")
    
    if not success:
        print("Installation failed. You can try installing manually with:")
        print(f"{sys.executable} -m pip install {' '.join(packages)}")
        sys.exit(1)
    
    # Register kernel for Jupyter
    print_step(5, "Registering Jupyter kernel")
    kernel_name = "python_env"
    
    success = run_command([sys.executable, "-m", "ipykernel", "install", "--user", f"--name={kernel_name}"],
                         "Failed to register Jupyter kernel.")
    
    if not success:
        print("Kernel registration failed. You can try registering manually with:")
        print(f"{sys.executable} -m ipykernel install --user --name={kernel_name}")
        sys.exit(1)
    
    # Verify installation
    print_step(6, "Verifying installation")
    try:
        import ipykernel
        import numpy
        import pandas
        import matplotlib
        import jupyter
        
        print("All required packages are installed:")
        print(f"- jupyter: {jupyter.__version__}")
        print(f"- ipykernel: {ipykernel.__version__}")
        print(f"- numpy: {numpy.__version__}")
        print(f"- pandas: {pandas.__version__}")
        print(f"- matplotlib: {matplotlib.__version__}")
    except ImportError as e:
        print(f"Warning: Not all packages are properly installed: {e}")
    
    # Final instructions
    print_step(7, "Final steps")
    print("1. In VS Code, ensure the Python and Jupyter extensions are installed")
    print("2. Open VS Code settings (Ctrl+Shift+P, then 'Preferences: Open Settings (UI)')")
    print("3. Search for 'Python: Default Interpreter Path'")
    print("4. Set it to the Python executable in your virtual environment:")
    
    if platform.system() == "Windows":
        interpreter_path = os.path.abspath(f"{venv_name}\\Scripts\\python.exe")
    else:
        interpreter_path = os.path.abspath(f"{venv_name}/bin/python")
    
    print(f"   {interpreter_path}")
    
    print("\nSetup complete! You can now:")
    print("1. Open number_game.py and run it (F5 or Run button)")
    print("2. Open python_basics.ipynb to test Jupyter functionality")

if __name__ == "__main__":
    main()