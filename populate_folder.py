import os
import re

# Folders to skip entirely
skip_whole_folders = ['China', '.git', '.idea']
# Folders to skip for certain actions
skip_folder = ['Easy', 'Hard', 'Medium']

def get_folder_number(folder_name):
    """
    Extracts the leading number from the folder name if present.
    """
    match = re.match(r'(\d+)', folder_name)
    if match:
        return match.group(1)  # Return the number as a string
    return None

def create_files_in_directory(directory):
    """
    Creates the files solution.py, notes.txt, and task.md with the number
    prefix extracted from the folder name.
    """
    folder_name = os.path.basename(directory)
    folder_number = get_folder_number(folder_name)

    if folder_number:
        files_to_create = [f'{folder_number}_solution.py', f'{folder_number}_notes.md', f'{folder_number}_task.md',
                           f'{folder_number}_notes.txt']
    else:
        files_to_create = ['solution.py', 'notes.txt', 'task.md']

    for file_name in files_to_create:
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                if 'solution.py' in file_name:
                    f.write("# Solution script\n")
                elif 'notes.txt' in file_name:
                    f.write("# Notes for solution\n")
                elif 'task.md' in file_name:
                    f.write("# Task description\n")
            print(f"Created {file_name} in {directory}")

def traverse_and_create_files(root_dir):
    """
    Traverses the root directory and creates the necessary files in each subdirectory
    if the folder name does not belong to the skip lists.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        folder_name = os.path.basename(dirpath)

        # Skip whole directories like China, .git, and .idea
        if any(skip in dirpath for skip in skip_whole_folders):
            continue

        # Skip certain folders like Easy, Hard, and Medium
        if folder_name in skip_folder:
            continue

        # Create necessary files in the current directory
        create_files_in_directory(dirpath)

if __name__ == '__main__':
    # Set the root directory (current working directory in this case)
    root_directory = os.getcwd()

    # Traverse and create files
    traverse_and_create_files(root_directory)

    os.remove('solution.py')
    os.remove('notes.txt')
    os.remove('task.md')
    os.remove('notes.md')