# har_fall_detection_deep_learning
# Human Activity Recognition and Fall Detection

## Overview
This project recognizes human activities and detects falls in real-time using deep learning.

## How to Use
1. Clone this repository.
2. Install dependencies:


Project Overview
The project aims to:

Classify human activities in group video sequences using deep learning models.
Detect falls in elderly individuals through real-time video classification techniques.
The system leverages popular machine learning frameworks like TensorFlow, Keras, and OpenCV to process and analyze video data for activity recognition and fall detection.

Key Features
Human Activity Recognition: Classify group activities from video sequences (e.g., walking, running, etc.).
Fall Detection: Detect falls in elderly people in real-time from video feeds.
Real-Time Processing: Designed to run efficiently on systems with GPU support for faster video processing.
Dataset
The system uses publicly available datasets for both Human Activity Recognition and Fall Detection:


## Clone the Repository:

First, clone the repository to your local machine:


git clone https://github.com/DeeptiShuklaProject/har_fall_detection_deep_learning.git
cd har_fall_detection_deep_learning
### Install Required Dependencies:

## Use the requirements.txt to install the necessary Python libraries:


pip install -r requirements.txt
## Download the Datasets:

Download Kinetics Dataset (or UCF101 or HMDB51) for human activity recognition.
Download URFD Dataset for fall detection.
After downloading, place the raw video files in data/raw/ directory.

Preprocess the Data:

Convert the raw video files into frames using the preprocess.py script. This script will resize and store the frames for model training.

Example:


python utils/preprocess.py
Train the Models:

After preprocessing, use the cnn_feature_extractor.py and rnn_classifier.py models to train the activity recognition and fall detection models.

## Run the FastAPI Application:

Start the FastAPI application by running the following command:

python -m app.main
Running the Application
Once the system is set up, you can access the application via FastAPI. By default, it will run on http://127.0.0.1:8000.

Open a web browser or use Postman to interact with the API.

## Available Endpoints:

GET /: A welcome message from the API.
POST /activity: Endpoint to send a video file for human activity recognition.
Request: A video file (video_file).
Response: The recognized activity label (e.g., "walking", "running").
POST /fall: Endpoint to send a video file for fall detection.
Request: A video file (video_file).
Response: Detection result, indicating whether a fall was detected or not.
Example usage in Postman:

Activity recognition: POST http://127.0.0.1:8000/activity with video file.
Fall detection: POST http://127.0.0.1:8000/fall with video file.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.

This README.md provides a detailed description of the project, dataset, setup instructions, and how to run the application. It can be customized further based on specific needs, but this should give a solid foundation for understanding and using the system.