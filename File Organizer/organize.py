import os
import shutil

current_dir =os.path.dirname(os.path.realpath(__file__))

print ('Welcome =)')
for filename in os.listdir(current_dir):
## image handling
    if filename.endswith((".png", ".jpg", ".webp")):
        if not os.path.exists("Image"):
            os.mkdir('Image')
        shutil.copy(filename,"Image")
        os.remove(filename)
        print('Image Is Done')

    if filename.endswith(( ".jpeg", ".gif",".jfif")):
        if not os.path.exists("Image"):
            os.mkdir('Image')
        shutil.copy(filename,"Image")
        os.remove(filename)
        print('Image Is Done')
        break


## video handling
    if filename.endswith((".mp4" ,".mov",".webm")):
        if not os.path.exists("Video"):
            os.mkdir('Video')
        shutil.copy(filename,"Video")
        os.remove(filename)
        print('Video Is Done')
        break

## Music handling
    if filename.endswith((".mp3", ".wav", ".aac")):
        if not os.path.exists("Music"):
            os.mkdir('Music')
        shutil.copy(filename, "Music")
        os.remove(filename)
        print('Music is Done')


## Documents handling
    if filename.endswith((".word", ".xls", ".xlsx")):
        if not os.path.exists("Documents"):
            os.mkdir('Documents')
        shutil.copy(filename,"Documents")
        os.remove(filename)
        print('Documents Is Done')

    if filename.endswith(( ".pdf", ".doc", ".txt")):
        if not os.path.exists("Documents"):
            os.mkdir('Documents')
        shutil.copy(filename,"Documents")
        os.remove(filename)
        print('Documents Is Done')
        break



## RAR handling
    if filename.endswith((".rar",".zip")):
        if not os.path.exists("RAR"):
            os.mkdir('RAR')
        shutil.copy(filename,"RAR")
        os.remove(filename)
        print('RAR Is Done')
        break


## app handling
    if filename.endswith((".dmg" ,".exe")):
        if not os.path.exists("Apps"):
            os.mkdir('Apps')
        shutil.copy(filename,"Apps")
        os.remove(filename)
        print('Apps Is Done')
        break


print ('Don Organizing This Folder')