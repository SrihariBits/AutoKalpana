from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding


def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


if __name__ == "__main__":
    ragam = 'kalyani'
    doc = load_doc("LSTMRNN_Saved\\"+ragam+'.txt')
    lines = doc.split('\n')

    tokenizer = Tokenizer(lower=False)
    tokenizer.fit_on_texts(lines)
    sequences = tokenizer.texts_to_sequences(lines)
    vocab_size = len(tokenizer.word_index) + 1

    sequences = array(sequences)
    X, y = sequences[:, :-1], sequences[:, -1]
    y = to_categorical(y, num_classes=vocab_size)
    seq_length = X.shape[1]

    model = Sequential()
    model.add(Embedding(vocab_size, 50, input_length=seq_length))
    model.add(LSTM(100, return_sequences=True))
    model.add(LSTM(100))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(vocab_size, activation='softmax'))
    print(model.summary())

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    # fit model
    model.fit(X, y, batch_size=128, epochs=100)

    # save the model to file
    model.save("MODEL_FILES\\" + "LSTMRNN" + ragam+'.h5')
    # save the tokenizer
    dump(tokenizer, open("MODEL_FILES\\" + ragam+'LSTMtokenizer.pkl', 'wb'))
