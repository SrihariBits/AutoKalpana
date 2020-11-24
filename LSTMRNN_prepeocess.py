import string
import os
from lexer import lexer
from lexer import lexerDP
from inverseDictionary import inv_dictionary


def clean(doc):
    doc = doc.replace('\n', '')
    doc = doc.replace('|', '')
    doc = doc.replace(' ', '')
    return doc


def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()


if __name__ == "__main__":
    ragam = "saveri"
    tokens = []
    for filename in os.listdir(os.path.join(os.getcwd(), "Dataset", ragam)):
        with open(os.path.join(os.getcwd(), "Dataset", ragam, filename), 'r') as f:
            print(filename)
            text = f.read()
            text = clean(text)
            tokenList = lexerDP(text, ragam)
            for grouping in tokenList:
                word = ""
                for num in grouping:
                    if num == -1:
                        continue
                    word = word + inv_dictionary[ragam][num]
                tokens.append(word)
    length = 5
    sequences = list()
    for i in range(length, len(tokens)):
        seq = tokens[i-length:i]
        line = ' '.join(seq)
        sequences.append(line)
    print('Total Sequences: %d' % len(sequences))

    out_filename = "LSTMRNN_Saved\\" + ragam+'.txt'
    save_doc(sequences, out_filename)
