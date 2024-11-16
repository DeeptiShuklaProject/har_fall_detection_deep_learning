import tensorflow as tf

def build_rnn_classifier(input_shape=(10, 2048)):  # Sequence length x feature size
    """
    Build an RNN classifier for activity recognition.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(128, return_sequences=True, input_shape=input_shape),
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')  # 10 classes for example
    ])
    return model
