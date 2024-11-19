# This is a sample Python script.
import os
import shutil
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Bezugsordner
bezugs_ordner = "./asd/"

# Zielordner
ziel_ordner = "./ordnerneu/"

def copy_file(file):
    """
        Copies a file from the source to the destination.

        """
    fileWithJpeg = file + ".jpeg"
    try:
        shutil.copy(bezugs_ordner + fileWithJpeg, ziel_ordner + file)  # Copies the file
    except FileNotFoundError:
        print(f"The source file or destination path does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_folder(folder_name):
    """
    Creates a folder with the specified name.
    If the folder already exists, it does nothing.

    Args:
        folder_name (str): The name or path of the folder to create.
    """
    try:
        os.makedirs(folder_name, exist_ok=True)  # Creates the folder and any parent directories
        print(f"Folder '{folder_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
def get_pictures(folder_name):
    """
        Returns a list of all .jpeg files in the specified folder.
        Args:
            folder_name (str): The path to the folder.
        Returns:
            list: A list of file names with the .jpeg extension in the folder.
        """

    try:
        # List all files in the directory and filter .jpeg files
        jpegs = [file for file in os.listdir(folder_name) if file.lower().endswith('.jpeg')]
        return jpegs
    except FileNotFoundError:
        print(f"The folder '{folder_name}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def work_on_file(file):
    create_folder(ziel_ordner + file)
    copy_file(file)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pictures = get_pictures("./asd")

    for picture in pictures:
        picture = picture.removesuffix(".jpeg")
        work_on_file(picture)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
