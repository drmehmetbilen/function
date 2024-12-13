import os

import os

def get_folder_details(folder_path):
    """
    Returns a list of file and folder names in the given directory.
    """
    try:
        file_list = os.listdir(folder_path)
        return str(file_list)
    except FileNotFoundError:
        return f"Error: The folder '{folder_path}' does not exist."
    except PermissionError:
        return f"Error: Permission denied to access '{folder_path}'."

def read_text_file(file_path):
    """
    Reads the contents of a text file and returns it as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    except PermissionError:
        return f"Error: Permission denied to read '{file_path}'."

def create_text_file(file_path, text_content):
    """
    Creates a text file at the specified path and writes the provided content to it.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_content)
        return f"File created successfully at '{file_path}'."
    except Exception as e:
        return f"Error: Unable to create the file. {str(e)}"

def delete_file(file_path):
    """
    Deletes the file at the specified path.
    """
    try:
        os.remove(file_path)
        return f"File '{file_path}' deleted successfully."
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    except PermissionError:
        return f"Error: Permission denied to delete '{file_path}'."
    except Exception as e:
        return f"Error: Unable to delete the file. {str(e)}"


if __name__ == '__main__':
    folder_path = 'deneme/new_test.txt'
    print(delete_file(folder_path))