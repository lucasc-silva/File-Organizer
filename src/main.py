import os
from typing import List

from PySide2.QtWidgets import QApplication, QFileDialog


def main():
    folder_path = show_directory_dialog()

    files = get_files_from_path(folder_path)
    if not files:
        raise FileNotFoundError("There are no files in this directory!")


def get_files_from_path(path: str) -> List[str]:
    files = []
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            continue
        files.append(filepath)

    return files


def show_directory_dialog() -> str:
    """ Show a directory dialog. """
    folder_path = QFileDialog.getExistingDirectory(
        caption="Choose a directory to sort!", # Dialog title
        dir=os.path.expanduser("~") # Dialog will start in the user's home directory.
    )

    return folder_path


if __name__ == "__main__":
    app = QApplication([])
    main()
