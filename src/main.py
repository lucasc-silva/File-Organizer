import os
from typing import List, Dict
import json
import shutil

from PySide2.QtWidgets import QApplication, QFileDialog


def main():
    folder_path = show_directory_dialog()

    files = get_files_from_path(folder_path)
    if not files:
        raise FileNotFoundError("There are no files in this directory!")

    mapping = read_json(os.path.join("src", "mapping.json"))
    sort_files(files, mapping)


def get_files_from_path(path: str) -> List[str]:
    """ Get all files from a given path.
    @param path: Directory to scan.
    @return: Returns a list of the files absolute path.
    """
    files = []
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            continue
        files.append(filepath)

    return files


def read_json(path: str) -> json:
    """ Read a JSON file and return its contents.
    @param path: Path to JSON file.
    @return: Returns a JSON object.
    """
    with open(path, "r", encoding="UTF-8") as f:
        return json.loads(f.read())


def show_directory_dialog() -> str:
    """ Show a directory dialog. """
    folder_path = QFileDialog.getExistingDirectory(
        caption="Choose a directory to sort!", # Dialog title
        dir=os.path.expanduser("~") # Dialog will start in the user's home directory.
    )
    if not folder_path:
        quit()

    return folder_path


def sort_files(files: List[str], mapping: Dict[str, List[str]]) -> None:
    """ Move files into folders.
    @param files: A list of file paths.
    @param mapping: A dictionary with Folders as key and a list of extensions as value.
    {
        "Images": [".png", ".jpg"]
    }
    This will move all '.png' and '.jpg' file into a folder called 'Images'.
    """
    directory = os.path.dirname(files[0])
    os.chdir(directory)

    for file in files:
        file_name, file_ext = os.path.splitext(file)
        for folder in mapping:
            if file_ext not in mapping[folder]:
                continue

            if os.path.exists(folder):
                shutil.move(file, folder)
            else:
                os.makedirs(folder)
                shutil.move(file, folder)


if __name__ == "__main__":
    app = QApplication([])
    main()
