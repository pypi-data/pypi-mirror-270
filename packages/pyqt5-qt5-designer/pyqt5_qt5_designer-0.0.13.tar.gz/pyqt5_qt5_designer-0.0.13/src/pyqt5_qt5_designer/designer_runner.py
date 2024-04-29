import os
import subprocess
import sys
def main_function():
    # Specify the path to the designer executable
    designer_location = os.path.join(os.path.dirname(__file__), "..\\PyQt5\\Qt5\\bin\\designer.exe")


    # Run designer executable with the provided arguments
    #print("Command:", [designer_location] + list(sys.argv))
    subprocess.run([designer_location] + [sys.argv[1]])

if __name__ == "__main__":
    
    # Pass any command-line arguments to the main_function

    print("sys argv:",sys.argv)
    main_function()
    