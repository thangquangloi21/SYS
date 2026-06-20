import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import pandas as pd
import pygetwindow as gw
import pyautogui
import time
from pynput.keyboard import Key, Listener
import keyboard
import datetime


class TabViewApp:
    APP_TITLE = "SYSTEM_OPERATION"

    WINDOW_TITLES = {
        "vega": "CIMVisionVEGA for CIMVisionPharms (Remote)",
        "operator": "CIMVisionPharms (Remote)",
        "qad_prod": "tvcprod: TVC TVC [USD] > TVC TVC",
        "qad_test": "tvctest: TVC TVC [USD] > TVC TVC",
        "oracle": "Oracle App"
    }

    def __init__(self, root):
        self.root = root

        if not self.is_first_instance():
            self.bring_app_to_front(self.APP_TITLE)
            root.destroy()
            return

        self.root.title(self.APP_TITLE)
        self.root.geometry("1000x600")

        self.links = {}
        self.username = ""
        self.password = ""

        self.load_settings()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        self.create_tab_home()
        self.create_tab_csv()
        self.create_tab_auto()

        self.start_keyboard_listener()

    # ================= CORE =================

    def is_first_instance(self):
        return not any(self.APP_TITLE in title for title in gw.getAllTitles())

    def bring_app_to_front(self, title):
        try:
            window = gw.getWindowsWithTitle(title)[0]
            if window.isMinimized:
                window.restore()
            window.activate()
        except:
            pass

    # ================= SETTINGS =================

    def load_settings(self):
        if not os.path.exists("setting.txt"):
            print("Không tìm thấy setting.txt")
            return

        with open("setting.txt", encoding="utf-8") as f:
            for line in f:
                if ":" not in line:
                    continue
                key, value = map(str.strip, line.split(":", 1))

                if key in ["username", "password"]:
                    setattr(self, key, value)
                else:
                    self.links[key] = value

    # ================= TAB 1 =================

    def create_button(self, parent, text, cmd, r, c):
        ttk.Button(parent, text=text, width=25, command=cmd).grid(row=r, column=c, padx=5, pady=5)

    def create_tab_home(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="HOME")

        ttk.Label(tab, text="MES").grid(row=0, column=0)
        ttk.Label(tab, text="QAD").grid(row=0, column=1)

        # MES buttons
        self.create_button(tab, "Vega32",
            lambda: self.open_app("Vega32", "vega"), 1, 0)

        self.create_button(tab, "Operator",
            lambda: self.open_app("Operator", "operator"), 2, 0)

        # QAD
        self.create_button(tab, "QAD Prod",
            lambda: self.open_app("QADprod", "qad_prod"), 1, 1)

        self.create_button(tab, "QAD Test",
            lambda: self.open_app("QADtest", "qad_test"), 2, 1)

    # ================= TAB CSV =================

    def create_tab_csv(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="CSV")

        ttk.Button(tab, text="Load CSV", command=self.load_csv).pack()

        self.tree = ttk.Treeview(tab)
        self.tree.pack(expand=True, fill="both")

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if not path:
            return

        df = pd.read_csv(path, dtype=str)

        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    # ================= TAB AUTO =================

    def create_tab_auto(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="AUTO")

        ttk.Label(tab, text="Số lượng:").grid(row=0, column=0)
        self.entry_count = tk.Entry(tab, width=10)
        self.entry_count.grid(row=0, column=1)

        ttk.Button(tab, text="Start", command=self.auto_click).grid(row=0, column=2)

        self.status = ttk.Label(tab, text="Dừng")
        self.status.grid(row=1, column=0)

    def auto_click(self):
        count = self.entry_count.get()

        if not count.isdigit():
            messagebox.showerror("Lỗi", "Phải nhập số")
            return

        count = int(count)

        for i in range(count):
            if keyboard.is_pressed("q"):
                self.status.config(text="Đã dừng")
                return

            self.status.config(text=f"Running {i}/{count}")
            self.root.update()

            pyautogui.rightClick(800, 369)
            pyautogui.click(866, 385)

    # ================= APP CONTROL =================

    def open_app(self, key, title_key):
        try:
            path = self.links.get(key)
            title = self.WINDOW_TITLES[title_key]

            if not path:
                messagebox.showerror("Lỗi", f"Chưa cấu hình {key}")
                return

            if any(title in w for w in gw.getAllTitles()):
                self.bring_app_to_front(title)
            else:
                self.open_and_login(path, title)

        except Exception as e:
            print("Error:", e)

    def open_and_login(self, path, title):
        os.startfile(path)

        while True:
            if keyboard.is_pressed('q'):
                return

            windows = gw.getAllTitles()

            if "Login" in windows:
                pyautogui.write(self.username)
                pyautogui.press("tab")
                pyautogui.write(self.password)
                pyautogui.press("enter")
                break

            time.sleep(1)

    # ================= SHORTCUT =================

    def start_keyboard_listener(self):
        def on_press(key):
            if key == Key.esc:
                self.root.lift()
                self.root.attributes('-topmost', True)
                self.root.attributes('-topmost', False)

        Listener(on_press=on_press).start()


# ================= RUN =================

def main():
    root = tk.Tk()
    app = TabViewApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
