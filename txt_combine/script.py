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
