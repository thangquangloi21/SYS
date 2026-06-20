import keyboard
import pyautogui
import time

is_typing = False  # cờ kiểm tra đang gõ hay không

def insert_text():
    global is_typing
    
    if is_typing:
        print("Đang gõ, bỏ qua hotkey...")
        return
    
    is_typing = True
    print("Bắt đầu gõ...")
    
    time.sleep(0.1)  # đảm bảo focus
    pyautogui.write("https://m365.cloud.microsoft/chat/conversation/ceb9565e-8768-4a8e-9341-defa532d2f20?fromCode=cmcv2&redirectId=6C99D091A7EE4EB6A97CFD946C000D32&internalredirect=CCM&client-request-id=f9fc83dc-7059-4737-bad1-6d0bea2cab7e&origindomain=CCM")
    
    print("Gõ xong ✅")
    is_typing = False

keyboard.add_hotkey("ctrl+tab", insert_text)

print("Đang chạy...")
print("Nhấn ALT + Q để gõ")
print("Nhấn ESC để thoát")

keyboard.wait("esc")




