import pyautogui

class MouseControl:
    def __init__(self):
        self.prev_x = None
        self.prev_y = None

        # 🔧 CORE SETTINGS (TUNE THESE)
        self.smoothing = 0.10      # LOWER = smoother (0.08–0.18)
        self.sensitivity = 0.5    # LOWER = more control (0.3–0.6)

    def move(self, x, y):
        screen_w, screen_h = pyautogui.size()

        # Clamp to screen
        x = max(0, min(x, screen_w))
        y = max(0, min(y, screen_h))

        # First frame
        if self.prev_x is None:
            self.prev_x, self.prev_y = x, y
            pyautogui.moveTo(x, y)
            return

        # Apply sensitivity (reduces area)
        target_x = self.prev_x + (x - self.prev_x) * self.sensitivity
        target_y = self.prev_y + (y - self.prev_y) * self.sensitivity

        # Exponential smoothing (LOW-PASS FILTER)
        smooth_x = self.prev_x + (target_x - self.prev_x) * self.smoothing
        smooth_y = self.prev_y + (target_y - self.prev_y) * self.smoothing

        pyautogui.moveTo(smooth_x, smooth_y)

        self.prev_x, self.prev_y = smooth_x, smooth_y

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def drag_start(self):
        pyautogui.mouseDown()

    def drag_end(self):
        pyautogui.mouseUp()
