from googletrans import *
import glob
import os
import argparse
import googletrans


helpLang = ""

for i in googletrans.LANGUAGES:
    helpLang += i + "=" + googletrans.LANGUAGES[i] + " | "


parser = argparse.ArgumentParser(description='Translate files and titles ')
parser.add_argument(
    '-i',
    dest='filename',
    action='store',
    default=argparse.SUPPRESS,
    type=str,
    required=True)

parser.add_argument(
    '-t', '--translate-to', dest='lang', action='store',required=True,
    choices=googletrans.LANGUAGES.keys(),
    help='Translate file to selected language\n' + helpLang + "example: py-FileTranslator.py -t sr -i filename " )

args = parser.parse_args()

files = args.filename
lang = args.lang

"""for files in filesList:"""
print("Translating " + str(files))
translator = Translator()
a = open(files, 'r+')
finalResult = ""
while True:
    title = a.read(5000)
    if title == "":
        break
    translated = translator.translate(title, dest=lang)
    finalResult += translated.text
finalResult = finalResult.replace(': ', ':')
finalResult = finalResult.replace('->', '-->')
a.close()
a = open(files, 'w', encoding="utf8")
a.write(finalResult)
