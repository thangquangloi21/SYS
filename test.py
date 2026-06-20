import pyautogui
import time
import os
import pygetwindow as gw


# tự động mở app và login

def getallwindow():
    windows = gw.getAllTitles()
    print("Danh sách các cửa sổ đang mở:")
    for title in windows:
        if title == "":
            continue
        else:
            print(f"- {title}")
        

def timanh08(img):
            try:
                button_location = pyautogui.locateOnScreen(img, confidence=0.8)
                # print(button_location)
                pyautogui.moveTo(button_location)
                pyautogui.leftClick(button_location)
                return button_location
            except Exception as e:
                # print("Không tìm thấy nút")
                print(e)
                return False


if __name__ == "__main__":
    getallwindow()
    # while(True):
    #     status = timanh08(r"C:\Users\249533\Downloads\anhchuatich.png")
    #     if not status:
    #         timanh08(r"C:\Users\249533\Downloads\ok.png")
    #         break