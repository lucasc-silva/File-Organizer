# File-Organizer
A script that sorts files into folders.

## Why?
The main reason is to save your time. Instead of having to manually create folders and sort files, you can just create a mapping of folders and extensions and let this script do it for you.

## How?
The folders and extensions need to be mapped in a **JSON** file. The folders will be the keys, and the value will be a list of extensions.
* Example:
```json
{
    "Images": [
        ".jpg",
        ".png"
    ],
    "Documents": [
        ".txt",
        ".pdf"
    ],
    "Books": [
        ".epub",
        ".mobi"
    ]
}
```

This means the script will create a folder called **Images** and move all **.jpg** and **.png** file into it.
* Note: Files without extensions will not be moved. If you want to move them, add an entry into your **JSON** file.
```json
{
    "Images": [
        ".jpg",
        ".png"
    ],
    "Documents": [
        ".txt",
        ".pdf"
    ],
    "Books": [
        ".epub",
        ".mobi"
    ],
    "Others": [
        ""
    ]
}
```
* Note 2: In Linux, files don't need to have an extension. This means the chosen folder can contain Appimages, Executables, Text files and etc.

## Dependencies
You only need to install PySide2. It is used to show the directory dialog.
```bash
pip install pyside2
```


## Usage
1. Clone the repository
```sh
git clone https://github.com/lucasc-silva/File-Organizer.git
```

2. Go to the repository folder.
```sh
cd File-Organizer/
```

3. Edit **mapping.json** to fit your needs. This is the default one:
```json
{
    "Images": [
        ".png",
        ".jpg"
    ],
    "Documents": [
        ".txt",
        ".pdf"
    ],
    "Books": [
        ".epub",
        ".mobi"
    ],
    "Executables": [
        ".exe"
    ],
    "Videos": [
        ".mp4",
        ".mkv"
    ],
    "Music": [
        ".mp3"
    ]
}
```

4. Run the script.
```sh
python3 src/main.py
```

When you run the program, a directory dialog will appear, allowing you to choose a directory to sort.

## Preview
