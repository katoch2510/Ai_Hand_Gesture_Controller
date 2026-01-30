import os
import shutil
import pyautogui

class FileCtrl:
    def __init__(self, folder="safe_folder"):
        self.folder = folder
        self.files = []
        self.idx = 0
        self.selected = None
        self.refresh_files()

    def refresh_files(self):
        """Reload files from folder"""
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        self.files = [
            f for f in os.listdir(self.folder)
            if os.path.isfile(os.path.join(self.folder, f))
        ]

        if not self.files:
            self.idx = 0
        else:
            self.idx = self.idx % len(self.files)

    def select(self):
        """Select next file safely"""
        self.refresh_files()

        if not self.files:
            print("⚠️ No files found in folder")
            return

        if self.idx >= len(self.files):
            self.idx = 0

        self.selected = self.files[self.idx]
        print(f"📂 Selected file: {self.selected}")

        self.idx += 1

    def copy(self, destination="copied_files"):
        """Copy selected file safely"""
        if not self.selected:
            print("⚠️ No file selected to copy")
            return

        src = os.path.join(self.folder, self.selected)

        if not os.path.exists(src):
            print("⚠️ Selected file no longer exists")
            return

        if not os.path.exists(destination):
            os.makedirs(destination)

        dst = os.path.join(destination, self.selected)
        shutil.copy(src, dst)

        print(f"✅ File copied to {dst}")
    def next(self):
        pyautogui.press("right")   # next file

    def previous(self):
        pyautogui.press("left")    # previous file
