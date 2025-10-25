#!/usr/bin/env python3
"""
Jupyter Notebook Setup Helper Script

This script helps set up Jupyter notebook support in VS Code by installing
necessary packages and registering the kernel.
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

def check_venv():
    """Check if running in a virtual environment."""
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

def main():
    """Main function to set up Jupyter notebook support."""
    # Check if running in a virtual environment
    print_step(1, "Checking virtual environment")
    if not check_venv():
        print("Warning: You are not running in a virtual environment.")
        print("It's recommended to activate your virtual environment first.")
        proceed = input("Do you want to proceed anyway? (y/n): ").lower()
        if proceed != 'y':
            print("Exiting. Please activate your virtual environment and run this script again.")
            sys.exit(1)
    else:
        print("Virtual environment detected.")
    
    # Install Jupyter packages
    print_step(2, "Installing Jupyter packages")
    packages = ["jupyter", "ipykernel", "numpy", "pandas", "matplotlib"]
    
    print(f"Installing packages: {', '.join(packages)}")
    success = run_command([sys.executable, "-m", "pip", "install"] + packages,
                         "Failed to install Jupyter packages.")
    
    if not success:
        print("Installation failed. You can try installing manually with:")
        print(f"{sys.executable} -m pip install {' '.join(packages)}")
        sys.exit(1)
    
    # Register kernel
    print_step(3, "Registering Jupyter kernel")
    kernel_name = "python_env"
    
    success = run_command([sys.executable, "-m", "ipykernel", "install", "--user", f"--name={kernel_name}"],
                         "Failed to register Jupyter kernel.")
    
    if not success:
        print("Kernel registration failed. You can try registering manually with:")
        print(f"{sys.executable} -m ipykernel install --user --name={kernel_name}")
        sys.exit(1)
    
    # Verify installation
    print_step(4, "Verifying installation")
    try:
        import jupyter
        import ipykernel
        import numpy
        import pandas
        import matplotlib
        
        print("All required packages are installed:")
        print(f"- jupyter: {jupyter.__version__}")
        print(f"- ipykernel: {ipykernel.__version__}")
        print(f"- numpy: {numpy.__version__}")
        print(f"- pandas: {pandas.__version__}")
        print(f"- matplotlib: {matplotlib.__version__}")
    except ImportError as e:
        print(f"Warning: Not all packages are properly installed: {e}")
    
    # Final instructions
    print_step(5, "Final steps")
    print("1. In VS Code, ensure the Jupyter extension is installed")
    print("2. Open the python_basics.ipynb file")
    print("3. When prompted, select the kernel you just registered")
    print("4. Try running the cells to verify everything works")
    
    print("\nJupyter notebook setup is complete!")

if __name__ == "__main__":
    main()