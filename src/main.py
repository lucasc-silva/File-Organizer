import os

from PySide2.QtWidgets import QApplication, QFileDialog


def main():
    folder_path = show_directory_dialog()


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
