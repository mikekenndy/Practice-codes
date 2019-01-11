#! python3
# fillGaps.py - finds all numbered files with a certain title
# and renames numbers to create a complete count

import re, os, shutil

def setMoveToFolder(folderName):
    try:
        # make folder if it doesn't already exist
        os.mkdir(folderName)
    except:
        return None

def moveToNewFolder(src, dst):
    try:
        if not src.__contains__(moveTo):
            # Copy to destination if folder doesn't exist
            shutil.copy(src, dst)
    except:
        # Otherwise replace existing file
        os.unlink(src)
        shutil.copy(src, dst)

# Set search directory
os.chdir('D:\\Programming\\Python')
# File name to move
name = 'moveThisFile'
# Create folder to move to
moveTo = os.getcwd() + '\\' + 'move_here'
setMoveToFolder(moveTo)

# Move files to new folder
for folder, subfolder, filenames in os.walk(os.getcwd()):
    for file in filenames:
        if file.__contains__(name):
            # print('folder: ' + folder + '\\' + file)
            moveToNewFolder(folder + '\\' + file, moveTo)

# Rename moved files
reNums = re.compile(r'\d+')
num = []
i = 1
for file in os.listdir('move_here'):
    num.append(reNums.findall(file))
    trailingNum = "%03d" % (i,)
    if file != name + trailingNum + '.txt':
        directory = os.getcwd() + '\\move_here\\'
        shutil.move(directory + file, directory + name + trailingNum + '.txt')
    i += 1

