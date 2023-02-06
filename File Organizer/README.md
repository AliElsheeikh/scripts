# Description

This code is an Python script for organizing files in a directory. The script checks each file in the directory and moves it to the corresponding subdirectory based on the file extension.

The following file extensions and their corresponding subdirectories are supported:

- Images: .png, .jpg, .webp, .jpeg, .gif, .jfif
- Videos: .mp4, .mov, .webm
- Music: .mp3, .wav, .aac
- Documents: .word, .xls, .xlsx, .pdf, .doc, .txt
- RAR: .rar, .zip
- Apps: .dmg, .exe

# Usage

Save the code to a organize.py file
Open the terminal and navigate to the directory where the organize.py file and the files you want to organize are located.
Run the script by typing `python organize.py` in the terminal.
The script will print messages indicating which files have been organized and moved to the corresponding subdirectories.


 
# Note
The script works on the assumption that the file extensions are correct.

After moving the file, it will be deleted from the original location.
