# File-Organizer
A script that sorts files into folders.

## Why?
The main reason is to save your time. Instead of having to manually create folders and sort files, you can just create a mapping of folders and extensions and let this script do it for you.

## How?
The folders and extensions need to be mapped in a **JSON** file. The folders will be the keys, and the value will be a list of extensions.
* Example:
```json
{
    "Images": [".jpg", ".png"],
    "Documents": [".txt", ".pdf"],
    "Books": [".epub", ".mobi"]
}
```

This means the script will create a folder called **Images** and move all **.jpg** and **.png** file into it.
* Note: Files without extensions will not be moved. If you want to move them, add an entry into your **JSON** file.
```json
{
    "Images": [".jpg", ".png"],
    "Documents": [".txt", ".pdf"],
    "Books": [".epub", ".mobi"],

    // No extensions are mapped by an empty string.
    "Others": [""]
}
```
* Note 2: In Linux, files don't need to have an extension. This means the chosen folder can contain Appimages, Executables, Text files and etc.

## Usage
Clone the repository
```sh
git clone https://github.com/lucasc-silva/File-Organizer.git
```

Go to the repository folder.
```sh
cd File-Organizer/
```

Then run the script.
```sh
python3 main.py
```

When you run the program, a directory dialog will appear, allowing you to choose a directory to sort. Files will also show, but won't be selectable. If you click in **cancel**, the dialog will close and the program will stop running.
