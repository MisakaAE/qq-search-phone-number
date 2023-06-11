import tkinter as tk
from urllib import request
import requests
import os
import time

#API
qqtoph = "https://zy.xywlapi.cc/qqapi?qq="

def searchqq(qq=10000):
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #cmd命令行清屏
    qq = input_text.get()
    full_qqtoph = qqtoph+qq
    #从API获得数据
    out_qqtoph = requests.get(full_qqtoph)
    #将获得的数据转换为字典
    dict_out_qqtoph = out_qqtoph.json()
    #判断状态码是否正常
    statuscode = dict_out_qqtoph['status']
    if statuscode == 200 :
        #从字典中筛选信息
        msg = dict_out_qqtoph['message']
        phone = dict_out_qqtoph['phone']
        area = dict_out_qqtoph['phonediqu']
    else :
        msg = "没有找到或输入错误"
        phone = "NULL"
        area = "NULL"
    #输出结果
    out = (f"当前时间：{nowtime}\n状态：{msg}\nQQ号：{qq}\n手机号：{phone}\n号码归属地：{area}\n*********************************\n")
    return out

 
def print_text():
    text = input_text.get()
    output_text.insert(tk.END,searchqq() ,text + "\n")

window = tk.Tk()
window.geometry("600x250")
window.title("查Q绑")

input_text = tk.Entry(window, width=30)
input_text.pack(pady=20)

button = tk.Button(window, text="Q绑查询", command=print_text)
button.pack()

output_text = tk.Text(window, height=10)
output_text.pack(pady=20)

window.mainloop()
