from pathlib import Path
import sys
from collections import  defaultdict
import hashlib

def main():
    print("Duplicate  File Finder")
    print("-----------------------")
    folder_input = input("Folder to scan (Enter = current):").strip()
    if not folder_input:
          folder_input = "."
    folder = Path(folder_input).resolve()
    if not folder.is_dir():
        print(f"Error:'{folder}' is not a directory.")
        sys.exit(1)
    print(f"\n Scanning: {folder}")
    print("This may take a while downloading on folder size..")



def  get_file_hash(path:Path) -> str:
    """ Compute SHA-256 hash of file content."""
    sha256 = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(65536)
            if not chunk: 
                break
            sha256.update(chunk)
if __name__ == "__main__":
     main()
