from googletrans import *
from srtools import cyrillic_to_latin, latin_to_cyrillic
import glob
import os


def filebrowser(word=""):
    """Returns a list with all files with the word/extension in it"""
    file = []
    for f in glob.glob("*"):
        if word in f:
            file.append(f)
    return file

filesList = filebrowser(".srt")
print(filesList)

for files in filesList:
    print("Translating " + str(files))
    translator = Translator()
    a = open(files,'r+')
    finalResult = ""
    while True:
        title = a.read(5000)
        if title == "":
            break
        translated = translator.translate(title ,dest='sr')
        toLatin = cyrillic_to_latin(translated.text)
        finalResult += toLatin
    finalResult = finalResult.replace(': ', ':')
    finalResult = finalResult.replace('->', '-->')
    a.close()
    a = open(files,'w', encoding="utf8")
    a.write(finalResult)


