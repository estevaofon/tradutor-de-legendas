# -*- coding: utf-8 -*-
from googletrans import Translator
import glob
translator = Translator()
import os

srt_files = glob.glob('*.srt')
english_srt = ''
for i in srt_files:
    if "PORTUGUES" in i:
        os.remove(i)
    else:
        english_srt = i

f_traduzido = english_srt.split('.')
base = os.path.basename(english_srt)
base = os.path.splitext(base)[0]
new_f = base+'-PORTUGUES'+'.srt'

transleted_list = []

with open(english_srt, 'r', encoding='utf-8') as data:
    srt_list = data.readlines()
    chunks = [srt_list[x:x+100] for x in range(0, len(srt_list), 100)]
    for chunk in chunks:
        big_txt = ''.join(chunk)
        translations = translator.translate(big_txt, dest='pt')
        translations.text = translations.text.replace('->', '-->')
        translations.text = translations.text.replace(': ', ':')
        transleted_list.append(translations.text+"\n")

with open(new_f, 'w', encoding='utf-8', newline='\r\n') as data:
    srt_list = []
    for item in transleted_list:
        for i in item.splitlines(keepends=True):
            srt_list.append(i)
    without_backspace = []
    for line in srt_list:
        if line.strip():
            without_backspace.append(line)

    formated_list = []
    for i, item in enumerate(without_backspace):
        formated_list.append(item)
        if '-->' in item:
            formated_list.insert(-2,"\n")
    formated_list.pop(0)
    data.writelines(formated_list)
