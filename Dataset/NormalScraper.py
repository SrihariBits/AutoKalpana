import requests
import re
from bs4 import BeautifulSoup
import os
path = "http://www.shivkumar.org/music/himadrisuthe.htm"
page = requests.get(path)
soup = BeautifulSoup(page.content, 'html.parser')
lines = soup.find_all('p', class_='MsoNormal')
dictionary = ['S', 'R', 'G', 'M', 'P', 'D', 'N',
              ',', ' ', '|', 's', 'r', 'g', 'm', 'p', 'd', 'n', '\n']
swara_content = ""
cnt = 0
for line in lines:
    text = str(line.get_text())
    text = " ".join(text.split())
    text = re.sub('-', ' ', text)
    text = re.sub(';', ',', text)
    text = re.sub('\n', ' ', text)
    text = re.sub(' ', '', text)
    text = re.sub(r'[0-9]', '', text)
    text = re.sub(r'\.', '', text)
    text = re.sub(r',?\(.*\)', '', text)
    text = text.replace("\u00A0", " ")
    text = text.replace("\u00AD", " ")
    text = text.replace("\u2026", " ")
    text = text.replace("\u00AD", "")
    text = text.replace("\u2013", "")
    text = text.replace("\u002D", "")
    #text = re.sub('\|', '', text)
    flag = False
    # print(text.encode())
    for c in text:
        if c not in dictionary:
            flag = True
            break
    if flag or not any((c.isalpha() or c == ',') for c in text):
        continue
    swara_content += text
    swara_content += '\n'
print(swara_content)
file_name = path.rsplit('/', 1)[-1]
file_name = file_name[:-4]
dir_name = "./Kalyani/"
if file_name+".txt" not in os.listdir(dir_name):
    with open(dir_name + file_name + ".txt", 'w', encoding='utf-8') as f:
        f.write(swara_content)
else:
    print("------ ALREADY EXISTS ------")
