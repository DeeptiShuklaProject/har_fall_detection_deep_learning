from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.fall_detection import detect_fall
from app.activity_recognition import recognize_activity
import sys
import os

# Ensure the correct module path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# FastAPI app initialization
app = FastAPI(title="HAR and Fall Detection System", version="1.0")

# Input data model for video processing
class VideoInput(BaseModel):
    video_file: str  # Path to the video file

@app.get("/")
def home():
    """
    Home endpoint for health check.
    """
    return {"message": "Welcome to HAR and Fall Detection System"}

@app.post("/activity")
def activity_endpoint(video: VideoInput):
    """
    Endpoint for recognizing activities in a video.
    """
    try:
        result = recognize_activity(video.video_file)
        return {"video": video.video_file, "activity": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error recognizing activity: {str(e)}")

@app.post("/fall")
def fall_endpoint(video: VideoInput):
    """
    Endpoint for detecting falls in a video.
    """
    try:
        result = detect_fall(video.video_file)
        return {"video": video.video_file, "fall_detected": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error detecting fall: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    print("Starting the FastAPI application...")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
