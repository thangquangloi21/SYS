import os
import sys
import win32com.client

def create_shortcut(target_path, shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.save()

if __name__ == "__main__":
    # Đường dẫn đến file .exe của bạn
    exe_path = r"D:\LOIII\DEV\check_wo\check_wo\bin\Debug\check_wo.exe"

    # Đường dẫn đến thư mục Startup
    startup_folder_path = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")

    # Tên lối tắt
    shortcut_name = "YourAppShortcut.lnk"

    # Đường dẫn đầy đủ của lối tắt
    shortcut_path = os.path.join(startup_folder_path, shortcut_name)

    # Tạo lối tắt
    create_shortcut(exe_path, shortcut_path)

    print("Lối tắt đã được tạo trong thư mục Startup.")