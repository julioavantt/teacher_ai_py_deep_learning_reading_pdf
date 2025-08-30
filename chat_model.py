# chatbot_model.py
# Ejemplo base de entrenamiento local (LSTM) para mapear preguntas a fragmentos/respuestas
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, TimeDistributed

def crear_modelo(vocab_size=10000, embedding_dim=128, max_len=100):
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_len),
        LSTM(128, return_sequences=True),
        TimeDistributed(Dense(vocab_size, activation='softmax'))
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
    return model

if __name__ == "__main__":
    modelo = crear_modelo()
    modelo.summary()
