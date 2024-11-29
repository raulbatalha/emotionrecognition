import cv2
import numpy as np

class EmotionProcessor:
    def __init__(self, face_classifier, emotion_classifier, emotion_labels):
        self.face_classifier = face_classifier
        self.emotion_classifier = emotion_classifier
        self.emotion_labels = emotion_labels

    def process_frame(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray_frame[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            roi_gray = roi_gray.astype("float") / 255.0
            roi_gray = np.expand_dims(roi_gray, axis=[0, -1])

            prediction = self.emotion_classifier.predict(roi_gray)[0]
            emotion = self.emotion_labels[np.argmax(prediction)]

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.9, (255, 255, 255), 2)

        return frame
