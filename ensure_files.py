import os

skip_whole_folders = ['China', '.git', '.idea']
skip_folder = ['Easy', 'Hard', 'Medium']


def create_files_in_directory(directory):
    files_to_create = ['solution.py', 'notes.txt', 'task.md']

    for file_name in files_to_create:
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                if file_name == 'solution.py':
                    f.write("# Solution script\n")
                elif file_name == 'notes.txt':
                    f.write("# Notes for solution\n")
            print(f"Created {file_name} in {directory}")


def traverse_and_create_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        folder_name = os.path.basename(dirpath)

        if any(skip in dirpath for skip in skip_whole_folders):
            continue

        if folder_name in skip_folder:
            continue

        create_files_in_directory(dirpath)


if __name__ == '__main__':
    root_directory = os.getcwd()

    traverse_and_create_files(root_directory)

    os.remove('solution.py')
    os.remove('notes.txt')
    os.remove('task.md')
