import cv2
from tensorflow.keras.models import load_model

class ModelManager:
    def __init__(self, face_model_path, emotion_model_path):
        self.face_classifier = self.load_face_model(face_model_path)
        self.emotion_classifier = self.load_emotion_model(emotion_model_path)

    @staticmethod
    def load_face_model(path):
        return cv2.CascadeClassifier(path)

    @staticmethod
    def load_emotion_model(path):
        return load_model(path)

    def get_models(self):
        return self.face_classifier, self.emotion_classifier
