import numpy as np

def recognize_activity(video_file):
    """
    Simulate activity recognition on video.
    """
    # Load pre-trained model and preprocess video
    # Here, you'd use your trained activity recognition model
    activity = np.random.choice(["Walking", "Running", "Sitting", "Standing"])
    return {"video": video_file, "activity": activity}
