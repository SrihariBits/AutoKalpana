import string
import os


def getValue(c):
    notes = ""
    if c == '1':
        notes = notes + "S"+"\u2193" + "-"
    elif c == '2':
        notes = notes + "R"+"\u2193" + "-"
    elif c == '3':
        notes = notes + "G"+"\u2193" + "-"
    elif c == '4':
        notes = notes + "M"+"\u2193" + "-"
    elif c == '5':
        notes = notes + "P"+"\u2193" + "-"
    elif c == '6':
        notes = notes + "D"+"\u2193" + "-"
    elif c == '7':
        notes = notes + "N"+"\u2193" + "-"
    elif c == 's':
        notes = notes + "S" + "-"
    elif c == 'r':
        notes = notes + "R" + "-"
    elif c == 'g':
        notes = notes + "G" + "-"
    elif c == 'm':
        notes = notes + "M" + "-"
    elif c == 'p':
        notes = notes + "P" + "-"
    elif c == 'd':
        notes = notes + "D" + "-"
    elif c == 'n':
        notes = notes + "N" + "-"
    elif c == 'S':
        notes = notes + "S"+"\u2191" + "-"
    elif c == 'R':
        notes = notes + "R"+"\u2191" + "-"
    elif c == 'G':
        notes = notes + "G"+"\u2191" + "-"
    elif c == 'M':
        notes = notes + "M"+"\u2191" + "-"
    elif c == 'P':
        notes = notes + "P"+"\u2191" + "-"
    elif c == 'D':
        notes = notes + "D"+"\u2191" + "-"
    elif c == 'N':
        notes = notes + "N"+"\u2191" + "-"
    elif c == '-':
        notes = notes + "-"
    elif c == ' ':
        notes = notes + ",-"
    elif c == ',':
        notes = notes + ","
    return notes


def fileToGayaka(filename, ragam):
    with open(os.path.join(os.getcwd(), "Dataset", ragam, filename), 'r') as f:
        text = f.read()
        string = ""
        for c in text:
            string += getValue(c)
        print(string)


def gayakaToFile(text, filename, ragam):
    file = open('Dataset\\'+ragam+'\\'+filename, 'w')
    data = ""
    for i in range(len(text)):
        if text[i] == '-' or text[i] == '~':
            continue
        if text[i] == ',':
            data += text[i]
        elif i+1 < len(text) and text[i+1] == '~':
            data += text[i]
        else:
            data += text[i].lower()
    file.write(data)
    file.close()


if __name__ == "__main__":
    ragam = 'kalyani'
    filename = ''
    text = ""
    fileToGayaka(filename, ragam)
    gayakaToFile(text, filename, ragam)
