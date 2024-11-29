import cv2
from config import MODEL_PATH, CASCADE_PATH, EMOTION_LABELS
from core.video_capture import VideoCaptureManager
from core.model_manager import ModelManager
from core.emotion_processor import EmotionProcessor
from utils.helpers import add_text_to_frame

def main():
    model_manager = ModelManager(CASCADE_PATH, MODEL_PATH)
    face_classifier, emotion_classifier = model_manager.get_models()
    processor = EmotionProcessor(face_classifier, emotion_classifier, EMOTION_LABELS)
    video_manager = VideoCaptureManager()

    window_name = 'Detecção de Emoções'
    cv2.namedWindow(window_name)

    try:
        while True:
            frame = video_manager.read_frame()

            if frame is None:
                print("Erro: Não foi possível capturar o frame!")
                break

            processed_frame = processor.process_frame(frame)
            processed_frame = add_text_to_frame(processed_frame, 'Pressione "Q" para sair')
            cv2.imshow(window_name, processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except RuntimeError as e:
        print(f"Erro de execução: {e}")

    finally:
        video_manager.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()