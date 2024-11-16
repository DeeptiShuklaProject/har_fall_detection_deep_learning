import tensorflow as tf
from tensorflow.keras.applications import ResNet50

def build_cnn_feature_extractor(input_shape=(224, 224, 3)):
    """
    Build a CNN model (e.g., ResNet50) for feature extraction.
    """
    base_model = ResNet50(weights="imagenet", include_top=False, input_shape=input_shape)
    model = tf.keras.models.Model(inputs=base_model.input, outputs=base_model.output)
    return model
