# main.py - simple webcam demo skeleton
import cv2

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # TODO: add face detection + mask classification here
        cv2.imshow("Face Mask Demo", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
