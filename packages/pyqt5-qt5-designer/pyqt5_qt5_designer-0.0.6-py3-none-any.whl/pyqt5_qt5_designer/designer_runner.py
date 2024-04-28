import os
import subprocess

def main_function(*args):
    # Specify the path to the designer executable
    designer_location = os.path.join(os.path.dirname(__file__), "..\\PyQt5\\Qt5\\bin\\designer.exe")

    # Run designer executable with the provided arguments
    subprocess.run([designer_location] + list(args))

if __name__ == "__main__":
    import sys
    # Pass any command-line arguments to the main_function
    main_function(*sys.argv[1:])