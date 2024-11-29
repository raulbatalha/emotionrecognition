import cv2

def add_text_to_frame(frame, text, position=(10, 30), color=(128, 0, 255), thickness=2):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness, cv2.LINE_AA)
    return frame
