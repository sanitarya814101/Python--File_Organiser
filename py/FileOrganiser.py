# importing os and shutil
import os
import shutil

# Taking complete path of the folder
path = input("Enter the path here: ")

# Storing all the files present in that folder in fileList variable
fileList = os.listdir(path)

#
for file in fileList:
    # Splitting the file name and storing its name in 'name' variable and its extension in 'ext' variable
    name, ext = os.path.splitext(file)

    # Storing the extension type
    ext = ext[1:]

    # By doing this, it will ignore folders present in that path as the folder doesn't contain any extension
    if ext == '':
        continue

    # It will move the file in their 'ext' folder name if it exists
    if os.path.exists(path + '/' + ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    # else it will create that folder and then it will move the file in their 'ext' folder name
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
