class Gesture:
    def __init__(self):
        pass

    def fingers(self, lm):
        """
        Returns finger state as:
        [thumb, index, middle, ring, pinky]
        1 = open, 0 = closed
        """
        if not lm:
            return []

        fingers = []

        # Thumb (x-axis comparison)
        fingers.append(1 if lm[4][1] > lm[3][1] else 0)

        # Other fingers (y-axis comparison)
        tips = [8, 12, 16, 20]
        pips = [6, 10, 14, 18]

        for tip, pip in zip(tips, pips):
            fingers.append(1 if lm[tip][2] < lm[pip][2] else 0)

        return fingers

    def get(self, fingers):
        """
        Returns action name based on finger pattern
        """

        # ---------------- MOUSE MOVE ----------------
        if fingers == [0, 1, 0, 0, 0]:
            return "MOVE"

        # ---------------- LEFT CLICK ----------------
        elif fingers == [0, 1, 1, 0, 0]:
            return "LEFT_CLICK"

        # ---------------- RIGHT CLICK ----------------
        elif fingers == [0, 1, 1, 1, 0]:
            return "RIGHT_CLICK"


        # ---------------- PLAY / PAUSE ----------------
        elif fingers == [1, 1, 1, 1, 1]:
            return "PLAY_PAUSE"

        # ---------------- OPEN APPS ----------------
        elif fingers == [0,0,1,0,0]:
            return "OPEN_BROWSER"

        elif fingers == [1, 1, 0, 0, 1]:
            return "OPEN_YouTube"

        # ================= VOLUME CONTROL =================
        # 👍 Thumbs up → Volume UP
        elif fingers == [1, 0, 0, 0, 0]:
            return "VOL_UP"

        # ✋ Four fingers (no thumb) → Volume DOWN
        elif fingers == [0, 1, 1, 1, 1]:
            return "VOL_DOWN"

        return None
