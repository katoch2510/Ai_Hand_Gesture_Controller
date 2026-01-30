import pyautogui

class Media:
    # ---------- SYSTEM VOLUME ----------
    def sys_vol_up(self):
        pyautogui.press("volumeup")

    def sys_vol_down(self):
        pyautogui.press("volumedown")

    # ---------- YOUTUBE VOLUME ----------
    def yt_vol_up(self):
        pyautogui.press("up")

    def yt_vol_down(self):
        pyautogui.press("down")

    def play_pause(self):
        pyautogui.press("space")

    def next(self):
        pyautogui.press("right")

    def previous(self):
        pyautogui.press("left")
