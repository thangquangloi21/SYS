import tkinter as tk
from tkinter import ttk
import os
from pynput.keyboard import Key, Listener
import pandas as pd
import pygetwindow as gw
import pyautogui
import time
from tkinter import filedialog, messagebox
import win32gui
import datetime
import keyboard  # Thư viện để theo dõi phím


# Tạo class chính cho ứng dụng
class TabViewApp:
    vega32_link = None
    operator_link = None
    master_link = None
    checkdata_link = None
    QADprod_link = None
    QADtest_link = None
    Checkdata_qad_link = None
    Master_data_link = None
    Acc_Managment_link = None
    Quytrinhvanhanh_link = None
    Update_report_link = None
    Manual_link = None
    Recovery_Inventory_link = None
    open_orlace_app_link = None
    QLTKMES_link = None
    QLTKQAD_link = None
    SCDLMES_link = None
    SCDLQAD_Link = None
    QLYC_LINK = None
    username = None
    password = None

    # title app
    VEGA_title = "CIMVisionVEGA for CIMVisionPharms (Remote)"
    OPERATOR_title = "CIMVisionPharms (Remote)"
    QADprod_title = "tvcprod: TVC TVC [USD] > TVC TVC"
    QADtest_title = "tvctest: TVC TVC [USD] > TVC TVC"
    OracleAPP_title = "Oracle App"

    # username = "249533"
    # password = "1"


    def __init__(self, root):
          # Kiểm tra instance khác
        if not self.is_first_instance():
            try:
                self.bring_app_to_front("SYSTEM_OPERATION")
                # self.focus_existing_instance()  # Đã comment, không sử dụng
                # self.root.withdraw()  # Đã comment, không sử dụng
                root.destroy()  # Đóng cửa sổ gốc
                return
            except Exception as error:
                print(f"Đã xảy ra lỗi trong khởi tạo: {error}")
        self.root = root
        ico_path = os.path.join(os.path.dirname(__file__), "img2.ico")
        self.root.title("SYSTEM_OPERATION")
        if os.path.exists(ico_path):
            self.root.iconbitmap(ico_path)
       
        # icon = PhotoImage(file="app_icon.png")
        # root.iconphoto(True, icon)

        self.root.geometry("1000x600")  # Thiết lập kích thước cửa sổ
        self.Load_setting()
        
        # Tạo Notebook (widget chứa các tab)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True, fill="both")
        # Tạo các tab
        # self.create_tab4()
        self.create_tab1()
        # self.create_tab2()
        self.create_tab3()
       
        # Khởi động listener bàn phím trong một luồng riêng
        self.start_keyboard_listener()
        
       
        
    def is_first_instance(self):
        # Tìm cửa sổ với tiêu đề giống nhau
        hwnd = win32gui.FindWindow(None, "SYSTEM_OPERATION")
        return hwnd == 0  # Trả về True nếu không tìm thấy instance khács
        

    def create_tab1(self):
        button_width = 25
        # Tạo frame cho tab 1
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="HOME")
        # Thêm nội dung vào tab 1
        # Tạo 4 nút và sắp xếp chúng vào các ô
        label1 = ttk.Label(tab1, text="MES")
        label1.grid(row=0, column=0, padx=50, pady=5)
        Label2 = ttk.Label(tab1, text="QAD")
        Label2.grid(row=0, column=1, padx=50, pady=5)
        open_file = ttk.Label(tab1, text="Open File")
        open_file.grid(row=0, column=2, padx=50, pady=5)
        open_file = ttk.Label(tab1, text="Tools")
        open_file.grid(row=0, column=3, padx=50, pady=5)

        # Button mes
        vega32_button = ttk.Button(tab1, text="Vega32", width=button_width, 
        command= lambda: self.openapp_btn(path=self.vega32_link,title=self.VEGA_title))
        vega32_button.grid(row=1, column=0, padx=5, pady=5)

        operator_button = ttk.Button(tab1, text="Operator", width=button_width, 
        command= lambda: self.openapp_btn(path=self.operator_link, title=self.OPERATOR_title))
        operator_button.grid(row=2, column=0, padx=5, pady=5)

        master_mes_button = ttk.Button(tab1, text="Master MES", width=button_width, 
        command= lambda: self.openapps_btn(path=self.master_link))
        master_mes_button.grid(row=3, column=0, padx=5, pady=5)

        checkdata_button = ttk.Button(tab1, text="Checkdata", width=button_width,
        command= lambda: self.openapps_btn(path= self.checkdata_link))
        checkdata_button.grid(row=4, column=0, padx=5, pady=5)

        orlaceapp_button = ttk.Button(tab1, text="Orlace APP", width=button_width,
        command= lambda: self.openapp_btn(path= self.open_orlace_app_link, title=self.OracleAPP_title))
        orlaceapp_button.grid(row=5, column=0, padx=5, pady=5)

        Quanlytk_button = ttk.Button(tab1, text="Quản lí tài khoản", width=button_width,
        command= lambda: self.openapps_btn(path= self.QLTKMES_link))
        Quanlytk_button.grid(row=6, column=0, padx=5, pady=5)

        Suachuadl_button = ttk.Button(tab1, text="Sửa chữa dữ liệu", width=button_width,
        command= lambda: self.openapps_btn(path= self.SCDLMES_link))
        Suachuadl_button.grid(row=7, column=0, padx=5, pady=5)

        # Button QAD
        qadprod_button = ttk.Button(tab1, text="QAD Prod", width=button_width, 
        command= lambda: self.openapp_btn(path=self.QADprod_link, title=self.QADprod_title))
        qadprod_button.grid(row=1, column=1, padx=5, pady=5)

        qadtest_button = ttk.Button(tab1, text="QAD Test", width=button_width, 
        command=lambda: self.openapp_btn(path= self.QADtest_link, title=self.QADtest_title))
        qadtest_button.grid(row=2, column=1, padx=5, pady=5)

        qadcheck_button = ttk.Button(tab1, text="Check data", width=button_width,
        command= lambda: self.openapps_btn(path=self.Checkdata_qad_link))
        qadcheck_button.grid(row=3, column=1, padx=5, pady=5)

        QLTKQAD_btn = ttk.Button(tab1, text="Quản lý tài khoản", width=button_width,
        command= lambda: self.openapps_btn(path=self.QLTKQAD_link))
        QLTKQAD_btn.grid(row=4, column=1, padx=5, pady=5)

        SCDLQAD_btn = ttk.Button(tab1, text="Sửa chữa dữ liệu", width=button_width,
        command= lambda: self.openapps_btn(path=self.SCDLQAD_Link))
        SCDLQAD_btn.grid(row=5, column=1, padx=5, pady=5)

        # button Open file
        masterdata_button = ttk.Button(tab1, text="MASTER DATA", width=button_width,
        command= lambda: self.openapps_btn(path= self.Master_data_link))
        masterdata_button.grid(row=1, column=2, padx=5, pady=5)

        accM_button = ttk.Button(tab1, text="Accounts Management", width=button_width, 
        command= lambda: self.openapps_btn(self.Acc_Managment_link))
        accM_button.grid(row=2, column=2, padx=5, pady=5)

        quytrinhvanhanh_button = ttk.Button(tab1, text="Quy trình vận hành", width=button_width, 
        command= lambda: self.openapps_btn(self.Quytrinhvanhanh_link))
        quytrinhvanhanh_button.grid(row=3, column=2, padx=5, pady=5)

        baocaotuan_button = ttk.Button(tab1, text="Update Báo cáo", width=button_width,
        command=lambda: self.openapps_btn(self.Update_report_link))
        baocaotuan_button.grid(row=4, column=2, padx=5, pady=5)

        manuauuser_button = ttk.Button(tab1, text="Hướng dẫn vận hành", width=button_width, 
        command= lambda: self.openapps_btn(self.Manual_link))
        manuauuser_button.grid(row=5, column=2, padx=5, pady=5)

        recovery_button = ttk.Button(tab1, text="Recovery and Inventory", width=button_width, 
        command= lambda: self.openapps_btn(self.Recovery_Inventory_link))
        recovery_button.grid(row=6, column=2, padx=5, pady=5)

        # Quản lý yêu cầu
        recovery_button = ttk.Button(tab1, text="Quản lý yêu cầu", width=button_width, 
        command= lambda: self.openapps_btn(self.QLYC_LINK))
        recovery_button.grid(row=7, column=2, padx=5, pady=5)

        # tools
        recovery_button = ttk.Button(tab1, text="Tắt app nhanh", width=button_width, 
        command= lambda: self.close_all_windows_except_current())
        recovery_button.grid(row=1, column=3, padx=5, pady=5)
        recovery_button = ttk.Button(tab1, text="Setting", width=button_width, 
        command= lambda: self.openapps_btn("setting.txt"))
        recovery_button.grid(row=2, column=3, padx=5, pady=5)
        recovery_button = ttk.Button(tab1, text="Loadsetting", width=button_width, 
        command= lambda: self.Load_setting())
        recovery_button.grid(row=3, column=3, padx=5, pady=5)
        convertdata_button = ttk.Button(tab1, text="Convert data", width=button_width, 
        command= lambda: self.convert_data_to_text())
        convertdata_button.grid(row=4, column=3, padx=5, pady=5)
   
   
    # def create_tab2(self):
    #     # Tạo frame cho tab 2
    #     tab2 = ttk.Frame(self.notebook)
    #     self.notebook.add(tab2, text="Check Tồn kho")

    #     # Tạo nút để tải tệp CSV
    #     self.load_button = tk.Button(tab2, text="Load CSV", command=self.load_csv)
    #     self.load_button.grid(row=0, column=15, padx=10, pady=10)

    #     # Danh sách nhãn và biến để lưu giá trị từ textbox
    #     labels = [
    #         ("Location:", 0), ("Item:", 2), ("Lot:", 4),
    #         ("Qty QAD:", 6), ("Qty MES:", 8),
    #     ]
    #     self.entries = {}  # Từ điển để lưu các Entry widget

    #     # Tạo nhãn và textbox nằm cạnh nhau
    #     for text, col in labels:
    #         # Nhãn
    #         ttk.Label(tab2, text=text).grid(row=0, column=col, padx=5, pady=5, sticky="W")
    #         # Textbox (bên phải nhãn)
    #         entry = tk.Entry(tab2, width=15)
    #         entry.grid(row=0, column=col+1, padx=5, pady=5, sticky="EW")
    #         self.entries[text.strip(":")] = entry  # Lưu Entry vào từ điển

    #         # Tạo bảng để hiển thị dữ liệu
    #     self.tree = ttk.Treeview(tab2)
    #     self.tree.grid(row=1, column=0, columnspan=16, padx=5, pady=5, sticky="nsew")

    #         # Thêm thanh cuộn cho bảng
    #     self.scrollbar = ttk.Scrollbar(tab2, orient="vertical", command=self.tree.yview)
    #     self.scrollbar.grid(row=1, column=16, sticky="ns")
    #     self.tree.configure(yscrollcommand=self.scrollbar.set)

    #         # Cấu hình lưới để tự động điều chỉnh kích thước
    #     tab2.grid_rowconfigure(1, weight=1)  # Hàng chứa Treeview co giãn
    #     for col in range(16):  # Tất cả cột từ 0-16 co giãn
    #         tab2.grid_columnconfigure(col, weight=1)

    #     # Gán sự kiện chọn hàng
    #     self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    def create_tab3(self):
        # Tạo frame cho tab 3
         # Tạo frame cho tab 3
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Auto add")
        # label
        labelsl = ttk.Label(self.tab3, text="Số lượng cần ADD:")
        labelsl.grid(row=0, column=0, padx=5, pady=5)
        trangthai_lab = ttk.Label(self.tab3, text="Trạng thái:")
        trangthai_lab.grid(row=1, column=0, padx=5, pady=5)
        self.trangthai_dp = ttk.Label(self.tab3, text="Dừng")
        self.trangthai_dp.grid(row=1, column=1, padx=5, pady=5)

        count_add = ttk.Label(self.tab3, text="Số Lần ấn:")
        count_add.grid(row=2, column=0, padx=5, pady=5)
        self.count_add_dp = ttk.Label(self.tab3, text="0")
        self.count_add_dp.grid(row=2, column=1, padx=5, pady=5)
         # Nhãn lưu ý
        self.notie = ttk.Label(self.tab3, text="Lưu ý: Khi Đang chạy muốn dừng Ấn Q",
                          foreground="red", font=("Times New Roman", 10, "bold"))
        self.notie.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="w")
        # texbox
        # entry = tk.Entry(tab2, width=15)
        texboxsl = tk.Entry(self.tab3, width = 5)
        texboxsl.grid(row=0, column=1, padx=10, pady=5)
        #checkbox
        Intermediate = tk.IntVar()
        Intermediatecheck = tk.Checkbutton(self.tab3, text = "add Intermediate",
                    variable = Intermediate, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 20) 
        Intermediatecheck.grid(row=0,  column=2, padx=10, pady=10)

        # Tạo nút để auto
        self.load_button = tk.Button(self.tab3, text="Auto", command=lambda: self.Auto_add_row(function=Intermediate.get(), count=texboxsl.get()))
        self.load_button.grid(row=0,  column=4, padx=10, pady=10)

    def Auto_add_row(self, function, count):
        try:
            if count.isdigit() and 0 < int(count) < 500:
               
                # Thiết lập độ trễ giữa các lệnh PyAutoGUI
                pyautogui.PAUSE = 0.01
                # Bật tính năng failsafe (di chuyển chuột đến góc trên trái để dừng)
                pyautogui.FAILSAFE = True
                # print(f"auto auto  {function} + sl {count}")
                print("OK")
                for i in range(int(count) + 1):
                    self.trangthai_dp.config(text="Đang chạy")
                    # Kiểm tra nếu phím 'q' được nhấn
                    if keyboard.is_pressed('q'):
                        print("Đã nhấn 'q'. Dừng chương trình!")
                        self.trangthai_dp.config(text="Dừng bằng Q")
                        self.tab3.update()  # Cập nhật giao diện
                        break
                    # đếm số lần ấn
                    print(f"đang ấn được {i}/{count} lần")
                    self.count_add_dp.config(text=f"{i}/{count}")
                    self.tab3.update()  # Cập nhật giao diện
                    # Click chuột phải tại tọa độ
                    pyautogui.rightClick(x=800, y=369)
                    # Di chuyển đến add và click chuột trái
                    if function == 0:
                        pyautogui.moveTo(x=866, y=385) # thêm dòng mới
                    elif function == 1:
                        pyautogui.moveTo(x=866, y=425)  # thêm dòng mới intermediate
                    pyautogui.click()
                else:
                    # Hoàn thành vòng lặp mà không bị dừng
                    self.trangthai_dp.config(text="Done")
                    self.tab3.update()  # Cập nhật giao diện
            else:
                print("Dữ liệu nhập vào ô phải là số và phải lớn hơn 0 và 500")
                messagebox.showinfo("Thông Báo", "Dữ liệu nhập vào ô phải là số và phải lớn hơn 0 và  nhỏ hơn 500")
        except KeyboardInterrupt:
            print("Chương trình đã bị dừng thủ công!")
            messagebox.showinfo("OK", "Chương trình đã bị dừng thủ công!")
        except Exception as e:
            print(f"Lỗi: {e}")
            messagebox.showinfo("ERROR",f"Lỗi: {e}")
        
        


        

    def on_row_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            row_data = self.tree.item(selected_item)['values']
            if len(row_data) < 7:
                messagebox.showwarning("Thông Báo", "File CSV không đủ cột dữ liệu cần thiết.")
                return
            row_data[1] = str(row_data[1]).zfill(5)
            row_datas = [row_data[1], row_data[2], row_data[3], row_data[4], row_data[6]]
            print("Selected Row Data:", row_data)  # In ra dữ liệu của hàng được chọn

            # Điền dữ liệu vào các Entry
            for i, key in enumerate(self.entries.keys()):
                self.entries[key].delete(0, tk.END)  # Xóa dữ liệu cũ
                self.entries[key].insert(0, row_datas[i])  # Điền dữ liệu mới



    def load_csv(self):
        # Mở hộp thoại để chọn tệp CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            # Đọc tệp CSV vào DataFrame
            try:
                self.df = pd.read_csv(file_path, dtype={"Location": str})
            except Exception as e:
                messagebox.showerror("ERROR", f"Lỗi đọc file CSV: {e}")
                return

            # Xóa các cột cũ trong bảng
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = list(self.df.columns)
            self.tree["show"] = "headings"

            # Tạo tiêu đề cho các cột và căn giữa dữ liệu
            for column in self.df.columns:
                self.tree.heading(column, text=column)
                self.tree.column(column, anchor="center", width=100)  # Đặt chiều rộng cột và căn giữa

            # Thêm dữ liệu vào bảng với hiệu ứng dòng kẻ
            for index, row in self.df.iterrows():
                if index % 2 == 0:
                    self.tree.insert("", "end", values=list(row), tags=("evenrow",))
                else:
                    self.tree.insert("", "end", values=list(row), tags=("oddrow",))

            # Định nghĩa màu cho các dòng
            self.tree.tag_configure("evenrow", background="#f0f0f0")  # Màu nền cho dòng chẵn
            self.tree.tag_configure("oddrow", background="#ffffff")   # Màu nền cho dòng lẻ


    # Mở ứng dụng
    def openapp_btn(self,path,title):
        try:
            self.checkopenapp(title, path)
        except FileNotFoundError:
            messagebox.showinfo("Thông Báo", "Không tìm thấy app(Sai Link)")
            print("Không tìm thấy app(Sai Link)")
        except Exception as e:
            print(f"Lỗi: {e}")

    def timanh08(self, img):
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


    # tự động mở app và login
    def open_and_login(self, app_path, username, password, open_name):
        openappqad = "Login"
        meslogin = "Certification Input (Remote)"
        windows = []

        stop_flag = False  # ✅ cờ dừng

        try:
            if not app_path:
                messagebox.showinfo("Thông Báo", "Chưa cấu hình đường dẫn ứng dụng trong setting.txt")
                return

            os.startfile(app_path)

            while True:
                # ✅ check dừng toàn cục
                if keyboard.is_pressed('q'):
                    print("Dừng ngay")
                    stop_flag = True
                    break

                windows = gw.getAllTitles()

                if meslogin in windows:
                    print("Cửa sổ Login đã mở.")

                    if self.operator_link == app_path:
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('tab')

                    pyautogui.write(username)
                    pyautogui.press('tab')
                    pyautogui.write(password)
                    pyautogui.press('enter')
                    break

                elif openappqad in windows:
                    print("Cửa sổ Login đã mở.")
                    window = gw.getWindowsWithTitle(openappqad)[0]
                    window.activate()

                    pyautogui.write(username)
                    pyautogui.press('tab')
                    pyautogui.write(password)
                    pyautogui.press('enter')
                    break

                elif "Update QAD (3.4.0.41)?" in windows:
                    window = gw.getWindowsWithTitle("Update QAD (3.4.0.41)?")
                    if window:
                        window[0].close()
                        print("Đã đóng Update")

                elif "RemoteApp security warning" in windows:
                    while True:
                        if keyboard.is_pressed('q'):
                            print("Dừng trong vòng con")
                            stop_flag = True
                            break

                        status = self.timanh08(img=r".\img\anhchuatich.png")
                        if not status:
                            self.timanh08(img=r".\img\VAOAPP.png")
                            break

                    if stop_flag:  # ✅ thoát luôn vòng ngoài
                        break

                else:
                    print("Đang chờ...")
                    time.sleep(1)

            # ✅ nếu đã dừng thì thoát luôn hàm
            if stop_flag:
                return

            if open_name in windows:
                print("Khởi động APP Thành công")

        except FileNotFoundError:
            print("Không tìm thấy ứng dụng (Sai Link)")
        except Exception as e:
            print(f"Lỗi: {e}")


    # ẤN nút esc để app hiện ra
    def start_keyboard_listener(self):
        def on_press(key):
            try:
                if key == Key.esc:
                    self.root.lift()  # Đưa cửa sổ lên trên cùng
                    self.root.attributes('-topmost', True)  # Đặt cửa sổ ở chế độ trên cùng
                    self.root.attributes('-topmost', False)  # Đặt lại để không giữ trên cùng
                else:
                    # print(f'Phím {key.char} đã được nhấn')
                    pass
            except AttributeError:
                # print(f'Phím đặc biệt {key} đã được nhấn')
                pass

        def on_release(key):
            if key == Key.esc:  # Thoát khi nhấn phím Esc
                # self.root.attributes('-topmost', False)  # Đặt lại để không giữ trên cùng
                print("esc")

        listener = Listener(on_press=on_press, on_release=on_release)
        listener.start()  # Bắt đầu lắng nghe
    
    # load link app
    def Load_setting(self):
        try:
            with open("setting.txt", 'r', encoding='utf-8') as file:
                for line in file:
                # Xử lý từng dòng
                    line = line.strip()  # Loại bỏ khoảng trắng thừa
                    if not line or ":" not in line:
                        continue

                    key, value = line.split(':', 1)  # Tách theo dấu ":"
                    key = key.strip()  # Loại bỏ khoảng trắng thừa ở key
                    value = value.strip()  # Loại bỏ khoảng trắng thừa ở value
                    # print(f"Key: {key}, Value: {value}")  # In ra key và value
                    # Gán giá trị cho các biến tương ứng
                    if key == "Vega32":
                        self.vega32_link = value
                    elif key == "Operator":
                        self.operator_link = value
                    elif key == "Master_Mes":
                        self.master_link = value
                    elif key == "Check_data":
                        self.checkdata_link = value
                    elif key == "QADprod":
                        self.QADprod_link = value
                    elif key == "QADtest":
                        self.QADtest_link = value
                    elif key == "Checkdata_qad":
                        self.Checkdata_qad_link = value
                    elif key == "Master_data":
                        self.Master_data_link = value
                    elif key == "Acc_Managment":
                        self.Acc_Managment_link = value
                    elif key == "Quytrinhvanhanh":
                        self.Quytrinhvanhanh_link = value
                    elif key == "Update_report":
                        self.Update_report_link = value
                    elif key == "Manual":
                        self.Manual_link = value
                    elif key == "Recovery_Inventory":
                        self.Recovery_Inventory_link = value
                    elif key == "open_orlace_app":
                        self.open_orlace_app_link = value
                    elif key == "QLTKMES_link":
                        self.QLTKMES_link = value
                    elif key == "QLTKQAD_link":
                        self.QLTKQAD_link = value
                    elif key == "SCDLMES_link":
                        self.SCDLMES_link = value
                    elif key == "SCDLQAD_Link":
                        self.SCDLQAD_Link = value
                    elif key == "QLYC_Link":
                        self.QLYC_LINK = value
                    elif key == "username":
                        self.username = value
                    elif key == "password":
                        self.password = value 
                    
        except FileNotFoundError:
            print("Tệp không tìm thấy.")
        except Exception as e:
            print(f"Lỗi: {e}")

    # kiểm tra app đã mở hay chưa?
    def list_open_windows(self):
    # Lấy danh sách tất cả các cửa sổ đang mở
        windows = gw.getAllTitles()
        print("Danh sách các cửa sổ đang mở:")
        for self.title in windows:
            print(f"- {self.title}")

    def is_app_open(self, window_title):
        # Kiểm tra xem ứng dụng có đang mở hay không
        if window_title == self.OPERATOR_title:
            return any(window_title == title for title in gw.getAllTitles())
        else:
            return any(window_title in title for title in gw.getAllTitles())

    # Đẩy lên đầu tiên
    def bring_app_to_front(self, window_title):
        try:
            if window_title == self.OPERATOR_title:
                # Tìm cửa sổ theo tiêu đề
                if any(self.VEGA_title ==  title for title in gw.getAllTitles()):
                    window = gw.getWindowsWithTitle(window_title)[1]
                else:
                    window = gw.getWindowsWithTitle(window_title)[0]

                if window.title == self.OPERATOR_title:
                    # Khôi phục cửa sổ nếu nó đang ở trạng thái minimize
                    if window.isMinimized:
                        window.restore()
                        # Đưa cửa sổ lên trên cùng
                    window.activate()
                    print(f"Cửa sổ '{window_title}' đã được đưa lên trên cùng.")
            else:
                # Tìm cửa sổ theo tiêu đề
                window = gw.getWindowsWithTitle(window_title)[0]
                # Khôi phục cửa sổ nếu nó đang ở trạng thái minimize
                if window.isMinimized:
                    window.restore()
                # Đưa cửa sổ lên trên cùng
                window.activate()
                print(f"Cửa sổ '{window_title}' đã được đưa lên trên cùng.")
        except IndexError:
            print(f"Cửa sổ '{window_title}' không tìm thấy.")

    # Mở Folder
    def openapps_btn(self,path):
            try:
                if not path:
                    messagebox.showinfo("Thông Báo", "Chưa cấu hình đường dẫn trong setting.txt")
                    return
                os.startfile(path)
            except FileNotFoundError:
                print("Không tìm thấy app(Sai Link)")
                messagebox.showinfo("Thông Báo", "Không tìm thấy app(Sai Link)")
            except Exception as e:
                print(f"Lỗi: {e}")

    def get_user_input(self):
        # Chọn thư mục cần đọc
        directory_path = filedialog.askdirectory(title="Chọn thư mục cần đọc")

        # Kiểm tra nếu người dùng hủy
        if not directory_path:
            messagebox.showwarning("Cảnh báo", "Bạn chưa chọn thư mục!")
            return None, None

        # Chọn đường dẫn lưu file đầu ra
        output_file_path = filedialog.asksaveasfilename(
            title="Chọn vị trí lưu file đầu ra",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        # Kiểm tra nếu người dùng hủy
        if not output_file_path:
            messagebox.showwarning("Cảnh báo", "Bạn chưa chọn vị trí lưu file đầu ra!")
            return None, None

        return directory_path, output_file_path

    def convert_data_to_text(self):
        directory_path, output_file = self.get_user_input()
        print(directory_path,output_file)
        # Kiểm tra nếu người dùng không hủy
        if directory_path and output_file:
            result = self.read_files_in_directory(directory_path, output_file)
            # Hiển thị thông báo kết quả
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Kết quả", result)
            root.destroy()
        
    def read_files_in_directory(self,directory_path, output_file):
        """
        Đọc tất cả file trong thư mục và ghi thông tin vào file txt.
        Args:
            directory_path: Đường dẫn đến thư mục cần đọc.
            output_file: Đường dẫn đến file txt đầu ra.
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                # Duyệt qua tất cả file và thư mục con
                for root, dirs, files in os.walk(directory_path):
                    # Ghi thông tin thư mục
                    outfile.write(f"\n=== Thư mục: {root} ===\n")
                    
                    # Nếu không có file trong thư mục
                    if not files:
                        outfile.write("Không có file trong thư mục này.\n")
                    
                    # Duyệt qua từng file
                    for file in files:
                        
                        file_path = os.path.join(root, file)
                        outfile.write(f"\nTên file: {file}\n")
                        outfile.write(f"Đường dẫn: {file_path}\n")
                        # lấy thông tin thời gina và ngày tạo
                        creation_time_stamp = os.path.getmtime(file_path)
                         # Chuyển đổi timestamp thành định dạng ngày giờ dễ đọc
                        # Chuyển timestamp thành đối tượng datetime
                        dt_object = datetime.datetime.fromtimestamp(creation_time_stamp)
                        # Định dạng đối tượng datetime theo chuỗi mong muốn
                        formatted_time = dt_object.strftime("%H:%M:%S %d/%m/%Y")
                        outfile.write(f"Thời gian tạo file : {formatted_time}\n")
                        
                        # Thử đọc nội dung file nếu là file văn bản
                        try:
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                                outfile.write("Nội dung:\n")
                                outfile.write(content + "\n")
                        except (UnicodeDecodeError, PermissionError, IOError):
                            outfile.write("Không thể đọc nội dung (có thể là file không phải văn bản hoặc lỗi quyền truy cập).\n")
                        outfile.write("-" * 50 + "\n")
                        
            return f"Đã ghi thông tin vào {output_file}"
        
        except Exception as e:
            return f"Lỗi: {str(e)}"
    def checkopenapp(self,title, Path):
        try:
            self.list_open_windows()
            # Kiểm tra xem ứng dụng có đang mở hay không
            if self.is_app_open(title): # == True thì call self.bring_app_to_front(title)
                # print(self.is_app_open(title))
                self.bring_app_to_front(title)

            else:
                print(f"Cửa sổ '{title}' không đang mở.")
                if title == self.OracleAPP_title:
                    self.openapps_btn(path=Path)
                else:
                    self.open_and_login(app_path=Path , username=self.username , password=self.password , open_name=title)
        except Exception as e:
                print(f"Lỗi: {e}")


    # Đóng tất cả các app đang mở:
    def get_current_window_title(self):
    # Lấy danh sách tất cả các cửa sổ đang mở
        windows = gw.getAllTitles()
        
        # Tìm cửa sổ hiện tại
        for title in windows:
            try:
                # Tìm cửa sổ theo tiêu đề
                window = gw.getWindowsWithTitle(title)[0]
                # Kiểm tra xem cửa sổ có đang hoạt động không
                if window.isActive:
                    return title
            except Exception as e:
                print(f"Không thể lấy tiêu đề cửa sổ '{title}': {e}")
        return None

    # Đóng tất cả các cửa sổ đang chạy
    def close_all_windows_except_current(self):
        current_program_title = "SYSTEM_OPERATION"
        if current_program_title:
            print("Đang đóng các cửa sổ (trừ cửa sổ chương trình hiện tại):")
            # Lấy danh sách tất cả các cửa sổ đang mở
            windows = gw.getAllTitles()
            
            for title in windows:
                if title != current_program_title:  # Kiểm tra xem tiêu đề có khác với tiêu đề cửa sổ hiện tại không
                    print(f"- Đóng cửa sổ: {title}")
                    try:
                        # Tìm cửa sổ theo tiêu đề
                        window = gw.getWindowsWithTitle(title)[0]
                        # Kích hoạt cửa sổ
                        window.activate()
                        time.sleep(0.1)  # Đợi một chút để đảm bảo cửa sổ được kích hoạt
                        # Gửi phím Alt + F4 để đóng cửa sổ
                        pyautogui.hotkey('alt', 'f4')
                        time.sleep(0.1)  # Đợi một chút giữa các lệnh
                    except Exception as e:
                        print(f"Không thể đóng cửa sổ '{title}': {e}")
                else:
                    print(f"- Giữ lại cửa sổ: {title}")
        else:
            print("Không thể xác định cửa sổ chương trình hiện tại.")

# Hàm main để chạy ứng dụng
def main():
    try:
        root = tk.Tk()
        app = TabViewApp(root)
        if root.winfo_exists():
            root.mainloop()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
