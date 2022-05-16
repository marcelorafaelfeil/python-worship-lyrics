import cv2 as cv


class VideoCapture:
    def __init__(self, camera: int):
        self.camera = camera

        self.video_capture = cv.VideoCapture(camera)

        if not self.video_capture.isOpened():
            print('It was not possible to open the camera')
            exit()

    def start(self):
        while True:
            ret, frame = self.video_capture.read()

            if not ret:
                print("Can't receive frame. Exiting...")
                break

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            cv.imshow('Original', gray)

            if cv.waitKey(1) == ord('q'):
                break

        self.close()

    def close(self):
        self.video_capture.release()
        cv.destroyAllWindows()
