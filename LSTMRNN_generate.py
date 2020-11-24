from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from lexer import lexer
from lexer import lexerDP
from random import seed
from random import randint
import re


def getValue(c):
    notes = ""
    if c == '1':
        notes = notes + "S"+"\u2193"  # +"-"
    elif c == '2':
        notes = notes + "R"+"\u2193"  # +"-"
    elif c == '3':
        notes = notes + "G"+"\u2193"  # +"-"
    elif c == '4':
        notes = notes + "M"+"\u2193"  # +"-"
    elif c == '5':
        notes = notes + "P"+"\u2193"  # +"-"
    elif c == '6':
        notes = notes + "D"+"\u2193"  # +"-"
    elif c == '7':
        notes = notes + "N"+"\u2193"  # +"-"
    elif c == 's':
        notes = notes + "S"  # +"-"
    elif c == 'r':
        notes = notes + "R"  # +"-"
    elif c == 'g':
        notes = notes + "G"  # +"-"
    elif c == 'm':
        notes = notes + "M"  # +"-"
    elif c == 'p':
        notes = notes + "P"  # +"-"
    elif c == 'd':
        notes = notes + "D"  # +"-"
    elif c == 'n':
        notes = notes + "N"  # +"-"
    elif c == 'S':
        notes = notes + "S"+"\u2191"  # +"-"
    elif c == 'R':
        notes = notes + "R"+"\u2191"  # +"-"
    elif c == 'G':
        notes = notes + "G"+"\u2191"  # +"-"
    elif c == 'M':
        notes = notes + "M"+"\u2191"  # +"-"
    elif c == 'P':
        notes = notes + "P"+"\u2191"  # +"-"
    elif c == 'D':
        notes = notes + "D"+"\u2191"  # +"-"
    elif c == 'N':
        notes = notes + "N"+"\u2191"  # +"-"
    elif c == '-':
        notes = notes + "-"
    elif c == ' ':
        notes = notes + ",-"
    return notes


def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
    result = list()
    in_text = seed_text
    for _ in range(n_words):
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        yhat = model.predict_classes(encoded, verbose=0)
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        in_text += ' ' + out_word
        result.append(out_word)
    return ' '.join(result)


def postprocessing(generated, raga):
    # Making it more lively
    # Random distribution of repetitive notes with commas
    notes = ""
    incPitch = []
    decPitch = []
    if raga == "kalyani":
        incPitch = [('r', 'g'), ('R', 'G'), ('m', 'p'), ('M', 'P'),
                    ('d', 'n'), ('D', 'N'), ('n', 's'), ('N', 'S')]
        decPitch = [('d', 'p'), ('D', 'P')]

    gen_patterns = generated.split()
    generated = ""
    for pat in gen_patterns:
        temp_str = ""
        i = 0
        for c in pat:
            temp_str += c
            i += 1
            if i % 4 == 0:
                temp_str += '-'
        generated = generated+" "+temp_str

    for i in range(len(generated)):
        if i+1 < len(generated) and generated[i+1] == generated[i] and randint(0, 1000) % 3 == 0:
            notes += ','
            continue
        notes = notes + getValue(generated[i])
        if i+1 < len(generated):
            if generated[i+1] == generated[i]:
                notes += '-'
            if (generated[i], generated[i+1]) in incPitch:
                notes += '<'
            if (generated[i], generated[i+1]) in decPitch:
                notes += '>'
    '''
    gen_patterns = generated.split()
    for pat in gen_patterns:
        print(pat)
        print(type(pat))
        lexer(pat, ragam, True)
    '''
    print(generated)
    print()
    print(notes)
    test_string = generated
    test_string = re.sub('-', '', test_string)
    test_string = re.sub(' ', '', test_string)
    print('BEGIN')
    lexer(test_string, ragam, True)  # change later
    print('END')


if __name__ == "__main__":
    ragam = 'kalyani'
    doc = load_doc("LSTMRNN_Saved\\"+ragam+'.txt')
    lines = doc.split('\n')
    seq_length = len(lines[0].split()) - 1

    # load the model
    model = load_model("MODEL_FILES\\" + "LSTMRNN" + ragam+'.h5')

    # load the tokenizer
    tokenizer = load(open("MODEL_FILES\\" + ragam+'LSTMtokenizer.pkl', 'rb'))

    # select a seed text
    seed_text = lines[randint(10, len(lines))]
    print(seed_text + '\n')

    # generate new text
    generated = generate_seq(model, tokenizer, seq_length, seed_text, 100)

    postprocessing(generated, ragam)
