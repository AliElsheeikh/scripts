
## This code provides an implementation to change the names of all files in a specified folder.


# Usage
- ### Provide the path of the folder you want to modify 
by setting the `folder_path` variable.   
add your folder path or use `os.path.realpath(__file__)` and drag the file.py in your folder.  

```
folder_path="C:\\Users\\HP\\Downloads\\ex"
```

- ###  Modify the format of the new file name if desired.
You can change the format of the new file name by modifying the `new_file_name` line.
```
new_file_name = f"name {i}{file_extension}"
```



# Note
- The path of the folder must be specified in the format "C:\\Users\\HP\\Downloads\\new" as shown in the example.  
- The code will check if the folder exists and if it does, it will change the current working directory to the specified folder.   
- The code then iterates over all the files in the folder and renames them according to the format specified in the new_file_name line.  
- Hidden files are skipped in the renaming process.  

