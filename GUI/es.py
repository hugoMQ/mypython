#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-11 14:41
# @Author  : yuguo

import tkinter as tk
from os import path
from tkinter import END
from tkinter import filedialog as fd
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter import ttk
import pandas as pd


class OOP():

    def __init__(self): #self指的是类实例对象本身
        self.win = tk.Tk()
        self.win.title("小工具")
        self.win.geometry('900x500')

        self.create_widgets()           #初始化组件
        self.dict = {}

    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)

        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1,text="mq")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text="es")

        tabControl.pack(expand=1, fill="both")

        #table as parent
        mighty3 = ttk.LabelFrame(tab2)
        mighty3.grid(row=0,column=0)



        model_label = ttk.Label(mighty3, text="模板名")
        model_label.grid(row=0,column=0, sticky='W')

        split_label = ttk.Label(mighty3, text="分片数")
        split_label.grid(row=1,column=0, sticky='W')

        copy_label = ttk.Label(mighty3, text="副本数")
        copy_label.grid(row=2, column=0, sticky='W')

        # insert_label = ttk.Label(mighty3, text="导入")
        # insert_label.grid(row=3, column=0, sticky='W')

        # Adding a Textbox Entry widget
        self.model = tk.StringVar()
        self.model_entered = ttk.Entry(mighty3, width=20, textvariable=self.model)
        self.model_entered.grid(row=0, column=1, sticky='W')

        self.splitNum = tk.StringVar()
        self.split_entered = ttk.Entry(mighty3, width=20, textvariable=self.splitNum)
        self.split_entered.grid(row=1, column=1, sticky='W')

        self.copyNum = tk.StringVar()
        self.copy_entered = ttk.Entry(mighty3, width=20, textvariable=self.copyNum)
        self.copy_entered.grid(row=2, column=1, sticky='W')

        self.insertPath = tk.StringVar()
        self.insertPath_entered = ttk.Entry(mighty3, width=20, textvariable=self.insertPath)
        self.insertPath_entered.grid(row=3, column=1, sticky='W')

        #ScrolledText  topic
        scrol_w = 40
        scrol_h = 15
        self.fieldText = scrolledtext.ScrolledText(mighty3, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.fieldText.grid(row=4, column=0, sticky='W',columnspan=2) #self.topicText.get(1.0,tk.END) #获取 文本内容

        scrol_w1 = 70
        scrol_h1 = 30
        self.esShellText = scrolledtext.ScrolledText(mighty3, width=scrol_w1, height=scrol_h1, wrap=tk.WORD)
        # columnspan选项可以指定控件跨越多列显示
        self.esShellText.grid(row=0, column=2, sticky='W',  rowspan=5)  # self.topicText.get(1.0,tk.END) #获取 文本内容


        intsert_button = ttk.Button(mighty3,text='导入',command=self.get_file).grid(row=3, column=0,sticky='W')
        runES_button = ttk.Button(mighty3,text='run',command=self.run_es_shell).grid(row=5, column=0,sticky='W')
        clearES_button = ttk.Button(mighty3, text='clear',command=self.clear_es_all).grid(row=5, column=1, sticky='E')
        copyES_button = ttk.Button(mighty3, text='copy',command=self.copy_es_shell).grid(row=5, column=2, sticky='E')

    #run
    def run_es_shell(self):
        #先清空操作
        self.esShellText.delete(1.0, END)
        templateName = self.model.get()
        spliteNumber = self.splitNum.get()
        copyNumber = self.copyNum.get()
        if templateName and spliteNumber and copyNumber and self.dict: #{},[],()，等都等价于False
            mapping = self.getMapping()

            esShell = "{\t\"" + self.model.get() + "_template\":{\n" + \
                      "\t\t\"order\": 0,\n" + \
                      "\t\t\"template\": \"" + templateName + "_*\",\n" + \
                      "\t\t\"settings\": {\n" + \
                      "\t\t  \"index\": {\n" + \
                      "\t\t\t\"number_of_shards\": \"" + spliteNumber + "\",\n" + \
                      "\t\t\t\"number_of_replicas\": \"" + copyNumber + "\",\n" + \
                      "\t\t\t\"refresh_interval\":\"60s\"\n" + \
                      "\t\t  }\n" + \
                      "\t\t},\n" + mapping + \
                      "\n\t\t\"aliases\": {}\n" + \
                      "\t}\n" + \
                      "}"

            self.esShellText.insert(tk.INSERT, esShell)
        else:
            self.error_msgBox()


    #清空所有
    def clear_es_all(self):
        self.model_entered.delete(0,END)
        self.split_entered.delete(0,END)
        self.copy_entered.delete(0,END)
        self.fieldText.delete(1.0, END)  #必须用1.0 ,END,記得引入 END
        self.esShellText.delete(1.0,END)


    #复制
    def copy_es_shell(self):
        result = self.esShellText.get(1.0, tk.END)
        #剪切板操作
        self.win.clipboard_append(result)
        self._msgBox()

    def _msgBox(self):
        msg.showinfo('提示','复制成功')
    def error_msgBox(self):
        msg.showerror('错误','输入有空值，请仔细检查')

    #getFile
    def get_file(self):
        print('hello from getFileName')
        filePath = fd.askopenfilename()
        self.insertPath_entered.delete(0, END)
        self.insertPath_entered.insert(0,filePath)
        #知道文件路径，可以使用pandas处理
        df = pd.read_excel(filePath)
        df = df.iloc[:,[0,2]]
        self.fieldText.insert(tk.INSERT, df)
        self.dict = df.set_index("字段名称").to_dict()['类型'] #转化为字典
        print(self.dict)

    # 命令拼接
    def getMapping(self):
        str1 = ''
        for key,value in self.dict.items():
            s = ''
            if(value != 'date'):
                s = "\t\t\t  \"" + key + "\": {\n" +\
                "\t\t\t\t\"type\": \"" + value + "\"\n" +\
                "\t\t\t  },\n"
            else:
                s = "\t\t\t  \"" + key + "\": {\n" +\
                "\t\t\t\t\"format\":\"yyyy-MM-dd HH:mm:ss\",\n" +\
                "\t\t\t\t\"type\": \"date\"\n" +\
                "\t\t\t  },\n"
            str1 = str1 + s

        str1 = str1[0:-2] #最后一条json 不要 （, \n） \n后面再加上
        str2 = "\t\t\"mappings\": {\n" +\
        "\t\t  \"" + self.model.get() + "\": {\n" +\
        "\t\t\t\"dynamic\": false,\n" +\
        "\t\t\t\"properties\": {\n" + str1 +\
        "\n\t\t\t},\n" + "\t\t\t  \"_all\": {\n" +\
        "\t\t\t\t\"enabled\": false\n" +\
        "\t\t\t}\n" +\
        "\t\t  }\n" +\
        "\t\t},"

        print(str2)
        return str2


    #执行

if __name__ == '__main__':
    oop = OOP()
    oop.win.mainloop()
