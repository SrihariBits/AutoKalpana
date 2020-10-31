from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


def getValue(c):
    notes = ""
    if c == '1':
        notes = notes + "S"+"\u2193"+"-"
    elif c == '2':
        notes = notes + "R"+"\u2193"+"-"
    elif c == '3':
        notes = notes + "G"+"\u2193"+"-"
    elif c == '4':
        notes = notes + "M"+"\u2193"+"-"
    elif c == '5':
        notes = notes + "P"+"\u2193"+"-"
    elif c == '6':
        notes = notes + "D"+"\u2193"+"-"
    elif c == '7':
        notes = notes + "N"+"\u2193"+"-"
    elif c == 's':
        notes = notes + "S"+"-"
    elif c == 'r':
        notes = notes + "R"+"-"
    elif c == 'g':
        notes = notes + "G"+"-"
    elif c == 'm':
        notes = notes + "M"+"-"
    elif c == 'p':
        notes = notes + "P"+"-"
    elif c == 'd':
        notes = notes + "D"+"-"
    elif c == 'n':
        notes = notes + "N"+"-"
    elif c == 'S':
        notes = notes + "S"+"\u2191"+"-"
    elif c == 'R':
        notes = notes + "R"+"\u2191"+"-"
    elif c == 'G':
        notes = notes + "G"+"\u2191"+"-"
    elif c == 'M':
        notes = notes + "M"+"\u2191"+"-"
    elif c == 'P':
        notes = notes + "P"+"\u2191"+"-"
    elif c == 'D':
        notes = notes + "D"+"\u2191"+"-"
    elif c == 'N':
        notes = notes + "N"+"\u2191"+"-"
    elif c == ' ':
        notes = notes + ","
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


if __name__ == "__main__":
    ragam = 'kalyani'
    doc = load_doc("LSTMRNN_Saved\\"+ragam+'.txt')
    lines = doc.split('\n')
    seq_length = len(lines[0].split()) - 1

    # load the model
    model = load_model('LSTMRNN.h5')

    # load the tokenizer
    tokenizer = load(open('LSTMtokenizer.pkl', 'rb'))

    # select a seed text
    seed_text = lines[randint(0, len(lines))]
    print(seed_text + '\n')

    # generate new text
    generated = generate_seq(model, tokenizer, seq_length, seed_text, 100)
    notes = ""
    for i in range(len(generated)):
        notes = notes + getValue(generated[i])

    print(generated)
    print(notes)
