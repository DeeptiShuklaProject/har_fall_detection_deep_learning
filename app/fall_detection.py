import numpy as np

def detect_fall(video_file):
    """
    Simulate fall detection on video.
    """
    # Load pre-trained model and preprocess video
    # Here, you'd use your trained fall detection model
    prediction = np.random.choice(["Fall", "No Fall"])
    return {"video": video_file, "result": prediction}
