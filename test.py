import os


def delete_files_in_directory(directory):
    # Define the files you want to delete
    files_to_delete = ['solution.py', 'nodes.txt', 'notes.txt']

    # Check if the directory contains the files and delete them
    for file_name in files_to_delete:
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {file_name} from {directory}")


def traverse_and_delete_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Delete solution.py and nodes.txt in each directory
        delete_files_in_directory(dirpath)


if __name__ == "__main__":
    # Set the root directory (current directory in this case)
    root_directory = os.getcwd()

    # Traverse through all directories and delete files
    traverse_and_delete_files(root_directory)