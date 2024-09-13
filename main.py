import subprocess
import sys
import os

def main():
    python_executable = sys.executable  # Use the Python interpreter from the current environment

   
    print("Running save_urls.py...")
    subprocess.run([python_executable, "save_urls.py"])

    
    print("Running screenshot_and_ocr.py...")
    subprocess.run([python_executable, "screenshot_and_ocr.py"])

if __name__ == "__main__":
    main()
