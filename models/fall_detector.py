import tensorflow as tf

def build_fall_detector(input_shape=(10, 2048)):
    """
    Build a binary classifier for fall detection.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(64, input_shape=input_shape),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')  # Binary output (fall/no fall)
    ])
    return model
