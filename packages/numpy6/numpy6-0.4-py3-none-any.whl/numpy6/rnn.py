from tensorflow.keras.datasets import imdb
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding , Dense , SimpleRNN
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


# Get the word index
word_index = imdb.get_word_index()

# Calculate vocabulary size
vocab_size = len(word_index) + 1  # Add 1 for padding token

print("Vocabulary Size:", vocab_size)


mx_len = 200
max_words = 10000
embending_dims = 128
(X_train , y_train), (X_test, y_test) = imdb.load_data(num_words = max_words)




print(X_train.shape)


X_train = pad_sequences(X_train, maxlen=mx_len)
X_test = pad_sequences(X_test, maxlen=mx_len)


model = Sequential()
model.add(Embedding(input_dim = max_words , output_dim = embending_dims , input_length = mx_len))
model.add(SimpleRNN(128))#dropout=0.2, recurrent_dropout=0.2)
model.add(Dense(1 , activation = 'sigmoid'))


model.summary()


model.compile(optimizer = 'adam' , loss = 'binary_crossentropy' , metrics = ['accuracy'])

model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
