import subprocess
import sys
import os

# Required libraries
required_libraries = ['openpyxl', 'beautifulsoup4', 'requests']

def setup_environment():
    global required_libraries
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("You are already in a virtual environment. No need to setup a new one.")
        return
    
    venv_dir = 'venv'
    if len(sys.argv) > 1:
        venv_dir = sys.argv[1]

    if not os.path.exists(venv_dir):
        subprocess.run([sys.executable, '-m', 'venv', venv_dir], check=True)
    
    # Update pip
    subprocess.run([os.path.join(venv_dir, 'Scripts' if os.name == 'nt' else 'bin', 'python'), '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
    
    # Path to the python executable in the virtual environment
    venv_python = os.path.join(venv_dir, 'Scripts' if os.name == 'nt' else 'bin', 'python')

    # Install required libraries
    if len(sys.argv) > 2 and sys.argv[2] == 'install':
        required_libraries = sys.argv[3:]
        
    for lib in required_libraries:
        subprocess.run([venv_python, '-m', 'pip', 'install', lib], check=True)

if __name__ == "__main__":
    setup_environment()
