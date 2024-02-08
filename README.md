# combine-txt
This Python script automates the process of combining multiple .txt files from a specified folder into a single .txt file.

### Running the Script:
1. place all `.txt` files you want to combine in the `txt_files/` folder inside `txt_combine/`.
2. Open a terminal or command prompt.
3. Navigate to the `txt_combine/` directory.
4. Execute the script by typing `python script.py` or `python3 script.py`.

After executing the script, you will find a new file named `combined_texts.txt` in the `txt_combine/` directory. This file will contain the combined contents of all `.txt` files from the `txt_files/` folder, with each file's content separated by "---".

### Requirements
Python 3.x installed on your system

### Script.py

```
# Import the os module to interact with the operating system
import os

# Define the path to the folder containing the .txt files
# Replace 'path/to/your/folder' with the actual path to your folder
source_folder = 'txt_files'

# Define the name of the destination file where the combined text will be stored
destination_file = 'combined_texts.txt'

# Create a list of all .txt files in the specified folder
txt_files = [file for file in os.listdir(source_folder) if file.endswith('.txt')]

# Open the destination file in write mode
with open(destination_file, 'w') as outfile:
    # Iterate over each .txt file in the list
    for filename in txt_files:
        # Open the current file in read mode
        with open(os.path.join(source_folder, filename), 'r') as infile:
            # Read the content of the file and write it to the destination file
            outfile.write(infile.read() + "\n---\n")
```
### Folder Structure
Here's the revised folder structure with the `txt_combine` as the main directory and `script.py` as the Python script file name, illustrated using Markdown format:

```
txt_combine/
│
├── script.py            # This is your Python script for combining text files
│
└── txt_files/           # Folder containing all .txt files to be combined
    ├── document1.txt
    ├── document2.txt
    ├── document3.txt
    ...
```

### Explanation:
- **`txt_combine/`**: The root directory where your script and the folder containing `.txt` files are located.
- **`script.py`**: The Python script that combines `.txt` files. It should be placed in the `txt_combine` directory.
- **`txt_files/`**: The folder where you should place all the `.txt` files you wish to combine. This folder is located within the `txt_combine` directory. If you choose a different folder name or path for your text files, update the `source_folder` variable in `script.py` accordingly.
