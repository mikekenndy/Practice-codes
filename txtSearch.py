# !python3
# txtSearch.py - searches all .txt files in a given folder for a word or phrase

import re, os

def getPhrase():
    print('Enter phrase to search for: ', end='')
    phrase = input()
    return phrase

def setSearchFolder():
    try:
        os.chdir('D:\\Programming\\Python\\text_search')
        directory = os.getcwd()
    except:
        return None
    return directory

# phrase = getPhrase()
# print('Searching for \'' + phrase + '\'')

folder = setSearchFolder()
print('cwd: ' + str(folder))

re_txt_files = re.compile(r'[a-zA-Z0-9.\-_\ ]+.txt')
txtFileList = re_txt_files.findall(str(os.listdir(folder)))

phrase = getPhrase()
re_searchPhrase = re.compile(phrase)

# search files for phrase
print('Searching files in \'' + folder + '\'')
if len(txtFileList) > 0:
    for file in txtFileList:
        searchFile = open(folder + '\\' + file)
        lineNum = 0
        print(file + ':')
        for line in searchFile.read().split('\n'):
            lineNum += 1
            if line.__contains__(phrase):
                print('line ' + str(lineNum) + ': "' + line + '"')
        print()