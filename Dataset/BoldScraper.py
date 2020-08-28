import requests
import re
from bs4 import BeautifulSoup
page = requests.get(
    "http://www.shivkumar.org/music/varnams/evvaribodhana.htm")
soup = BeautifulSoup(page.content, 'html.parser')
lines = soup.find_all('p', class_='MsoNormal')
dictionary = ['S', 'R', 'G', 'M', 'P', 'D', 'N',
              ',', ' ', '|', 's', 'r', 'g', 'm', 'p', 'd', 'n', '\n']
swara_content = ""
cnt = 0
for line in lines:
    while line.find('span', style='mso-spacerun:yes') != None:
        tagged = line.find('span', style='mso-spacerun:yes')
        tagged.replace_with(' ')
    while line.find('b') != None:
        tag = line.b
        temp = str(tag.get_text()).lower()
        tag.replace_with(temp)
    text = str(line.get_text())
    text = text.swapcase()
    text = " ".join(text.split())
    text = re.sub('-', ' ', text)
    text = re.sub('\n', ' ', text)
    text = re.sub(' ', '', text)
    text = re.sub(r'[0-9]', '', text)
    text = re.sub(r'\.', '', text)
    text = re.sub(r',?\(.*\)', '', text)
    text = text.replace("\u00A0", " ")
    text = text.replace("\u00AD", " ")
    text = text.replace("\u2026", " ")
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
