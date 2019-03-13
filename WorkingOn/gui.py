import tkinter as tk
window = tk.Tk()
window.title("金門大學搶課系統 -by BH Workshop")
window.geometry("800x600")

account_E = tk.Entry(window)
account_E.pack()   
password_E = tk.Entry(window)
password_E.pack()   


def hit_me():
    print ("爬蟲程式GO!")

b = tk.Button(window, 
    text='hit me',      # 按鈕文字
    width=15, height=2, 
    command=hit_me)     # 執行命令
b.pack()    # 按钮位置

window.mainloop()