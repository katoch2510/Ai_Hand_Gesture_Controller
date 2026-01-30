import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.draw = mp.solutions.drawing_utils

    def detect(self, img):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)
        return img

    def landmarks(self, img):
        lm = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]
            h, w, _ = img.shape
            for i, p in enumerate(hand.landmark):
                lm.append((i, int(p.x * w), int(p.y * h)))
            self.draw.draw_landmarks(img, hand, mp.solutions.hands.HAND_CONNECTIONS)
        return lm
