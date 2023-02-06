import os

# # folder path //add your path or 
# # use os.path.realpath(__file__) and drag the file in your folder 
# # on Windows os you must add '\' like this  "C:\\Users\\HP\\Downloads\\new"

folder_path="C:\\Users\\HP\\Downloads\\new"
# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"Error: folder '{folder_path}' does not exist.")

# Change the current working directory to the specified folder
os.chdir(folder_path)

# Counter to keep track of the number of files processed
i = 1

for file in os.listdir(folder_path):
    # Skip hidden files
    if file.startswith("."):
        continue
    # Get the file extension
    file_extension = os.path.splitext(file)[1]
    # Generate the new file name 
    new_file_name = f"name {i}{file_extension}"
    # Rename the file
    os.rename(file, new_file_name)
    i += 1

print(f"Success: {i-1} files in folder '{folder_path}' have been renamed.")
