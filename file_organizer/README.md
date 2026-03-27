🖤 File Organizer (Python Project)

---

📌 Project Overview

This is a simple Python File Organizer that automatically sorts files in a given folder into categorized subfolders based on their file types.

---

🎯 Features

- ✔ Organizes files by type (Images, Audio, Documents)
- ✔ Creates folders automatically
- ✔ Handles unknown files using an Others folder
- ✔ Prevents overwriting using duplicate handling
- ✔ Works dynamically using user input (CLI)

---

🧠 How It Works (Logic Flow)

1. Take folder path from user
2. Read all files in the folder
3. Skip directories
4. Identify file extension
5. Match file type with predefined categories
6. Create destination folder (if not exists)
7. Check for duplicate file names
8. Rename file if needed (a_1, a_2, ...)
9. Move file to destination folder

---

🗂️ File Type Mapping

file_types = {
    "Images": [".jpg", ".png"],
    "Audio": [".mp3"],
    "Documents": [".pdf", ".txt"]
}

---

📁 Example

Before:

test_folder/
  a.pdf
  song.mp3
  image.jpg
  notes.txt

---

After:

test_folder/
  Documents/
    a.pdf
    notes.txt
  Audio/
    song.mp3
  Images/
    image.jpg

---

🔁 Duplicate Handling

If a file already exists in the destination folder:

a.pdf → a_1.pdf → a_2.pdf

Logic:

if os.path.exists(dest_path):
    counter = 1
    while os.path.exists(dest_path):
        new_name = f"{name}_{counter}{ext}"
        dest_path = os.path.join(dest_folder, new_name)
        counter += 1

---

⚙️ Requirements

- Python 3.x
- Standard libraries:
  - "os"
  - "shutil"

(No external libraries required)

---

▶️ How to Run

python -m app.main

Then enter the folder path:

Enter folder path: test_folder

---

🧠 Key Concepts Used

- File Handling
- OS Module ("os")
- File Movement ("shutil")
- Loops & Conditions
- Dictionary Mapping
- Path Handling

---

🔥 One-Line Summary

Automates file sorting by detecting file types and organizing them into structured folders safely.

---