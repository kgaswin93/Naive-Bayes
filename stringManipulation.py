import os
import random
from stop_words import get_stop_words

def getKeyWords(data_instance):
    wordList = data_instance.split(" ")
    return list(set(wordList))

def chooseRandomClass(path):
    fileList = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    fileList = random.sample(fileList, 5)
    return fileList

def removeStopWords(text):
    stop_words = get_stop_words('en')
    words = getKeyWords(text)
    resultwords = [word for word in words if word.lower() not in stop_words]
    result = ' '.join(resultwords)
    result = ''.join(e for e in result if e.isalpha() or e == ' ')
    result = " ".join(result.split())
    return result

def removeHeaders(lines):
    delimiter = 'Lines:'
    i = 0
    for i in range(0,len(lines)):
        if delimiter in lines[i]:
            break
    return ' '.join(lines[i+1:])

def readLinesFromFile(path):
    with open(path, 'r') as myfile:
        text = myfile.read()
    lines = text.split('\n')
    return lines

def getAttributesClasses(dirpath,dirlist):
    attr_list = []
    class_list = []
    for dir_name in dirlist:
        path_name = dirpath + dir_name + '/'
        for file in os.listdir(path_name):
            lines = readLinesFromFile(path_name + '/' + file)
            text = removeHeaders(lines)
            text = removeStopWords(text)
            text = removeStopWords(text)
            attr_list.append(text)
            class_list.append(dir_name)
    return attr_list,class_list