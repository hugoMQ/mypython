#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-11 14:41
# @Author  : yuguo

import csv
# 处理表格文件
import json
import os
import tkinter as tk
from tkinter import END
from tkinter import filedialog as fd
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter import ttk

import pandas as pd
from xlsxwriter.workbook import Workbook


class OOP():
    def __init__(self): #self指的是类实例对象本身
        self.win = tk.Tk()
        self.win.title("小工具")
        #self.win.iconbitmap("D:\\pythonTool\\mq_s.ico")
        self.win.geometry('850x500')

        self.create_widgets()           #初始化组件

    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1,text="mq")
        # tab2 = ttk.Frame(tabControl)
        # tabControl.add(tab2, text="es")

        tabControl.pack(expand=1, fill="both")

        #table as parent
        mighty = ttk.LabelFrame(tab1)
        mighty.grid(row=0,column=0)
        #第二个母版
        mighty2 = ttk.LabelFrame(tab1)
        mighty2.grid(row=1, column=0,sticky='W')



        namesrv_label = ttk.Label(mighty, text="namesrv")
        namesrv_label.grid(row=0,column=0, sticky='W')

        cluster_label = ttk.Label(mighty, text="clusterName")
        cluster_label.grid(row=1,column=0, sticky='W')

        topic_label = ttk.Label(mighty, text="topic")
        topic_label.grid(row=2, column=0, sticky='W')

        # Adding a Textbox Entry widget
        self.namesrv = tk.StringVar()
        self.namesrv_entered = ttk.Entry(mighty, width=20, textvariable=self.namesrv)
        self.namesrv_entered.grid(row=0, column=1, sticky='W')

        self.clusterName = tk.StringVar()
        self.clusterName_entered = ttk.Entry(mighty, width=20, textvariable=self.clusterName)
        self.clusterName_entered.grid(row=1, column=1, sticky='W')

        #ScrolledText  topic
        scrol_w = 30
        scrol_h = 15
        self.topicText = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.topicText.grid(row=2, column=1, sticky='W') #self.topicText.get(1.0,tk.END) #获取 文本内容

        scrol_w1 = 60
        scrol_h1 = 20
        self.shellText = scrolledtext.ScrolledText(mighty, width=scrol_w1, height=scrol_h1, wrap=tk.WORD)
        # columnspan选项可以指定控件跨越多列显示
        self.shellText.grid(row=0, column=2, sticky='W',  rowspan=3)  # self.topicText.get(1.0,tk.END) #获取 文本内容

        run_button = ttk.Button(mighty,text='run',command=self.run_topic).grid(row=3, column=0,sticky='W')
        clear_button = ttk.Button(mighty, text='clear',command=self.clear_all).grid(row=3, column=1, sticky='E')
        copy_button = ttk.Button(mighty, text='copy',command=self.copyShell).grid(row=3, column=2, sticky='E')

        #topic导入导出
        intsert_topic_button = ttk.Button(mighty2, text='topic.json导入',command=self.get_file).grid(row=0, column=0, sticky='W')
        out_topic_button = ttk.Button(mighty2, text='topic导出',command=self.deal_file).grid(row=1, column=0, sticky='W')

        self.file_topic_in = tk.StringVar()
        self.file_topic_in_entered = ttk.Entry(mighty2, width=25, textvariable=self.file_topic_in)
        self.file_topic_in_entered.grid(row=0, column=1, sticky='W')

        self.file_topic_out = tk.StringVar()
        self.file_topic_out_entered = ttk.Entry(mighty2, width=25, textvariable=self.file_topic_out)
        self.file_topic_out_entered.grid(row=1, column=1, sticky='W')

        # group导入导出
        intsert_group_button = ttk.Button(mighty2, text='group.json导入', command=self.get_file2).grid(row=0, column=2,sticky='W')
        out_group_button = ttk.Button(mighty2, text='group导出', command=self.deal_file2).grid(row=1, column=2, sticky='W')

        self.file_group_in = tk.StringVar()
        self.file_group_in_entered = ttk.Entry(mighty2, width=25, textvariable=self.file_group_in)
        self.file_group_in_entered.grid(row=0, column=3, sticky='W')

        self.file_group_out = tk.StringVar()
        self.file_group_out_entered = ttk.Entry(mighty2, width=25, textvariable=self.file_group_out)
        self.file_group_out_entered.grid(row=1, column=3, sticky='W')

    #run
    def run_topic(self):
        namesrv = self.namesrv.get()
        clusterName = self.clusterName.get()
        topics = self.topicText.get(1.0,tk.END)
        topicSplit = topics.split("\n")

        #清空面板与剪切板
        self.shellText.delete(1.0, END)
        self.win.clipboard_clear()
        self.shellText.insert(tk.INSERT,'#!/bin/bash'+'\n'*2)

        for t in topicSplit:
            if t=="" or t==None:
               return
            topic,group = self.getShell(namesrv,clusterName,t)
            self.shellText.insert(tk.INSERT, topic+'\n' + group+'\n'+'sleep 2'+'\n')  #  必须加上tk.INSERT,





    #清空所有
    def clear_all(self):
        self.namesrv_entered.delete(0,END)
        self.clusterName_entered.delete(0,END)
        self.topicText.delete(1.0, END)  #必须用1.0 ,END,記得引入 END
        self.shellText.delete(1.0,END)

    #命令拼接
    def  getShell(self,namesrv,clusterName,t):
        topic = 'sh mqadmin updateTopic -n '+ namesrv + ' -c '+clusterName +' -t '+t+' -r 10 -w 10'
        group = 'sh mqadmin updateSubGroup -n '+ namesrv + ' -c '+clusterName +' -g CONSUMER_'+t+'_GROUP -r 1'
        return topic,group

    #复制
    def copyShell(self):
        result = self.shellText.get(1.0, tk.END)
        #剪切板操作
        self.win.clipboard_append(result)
        self._msgBox()

    def _msgBox(self):
        msg.showinfo('提示','复制成功')

    #导入文件
    # getFile
    def get_file(self):
        print('hello from getFileName')
        filePath = fd.askopenfilename()
        self.file_topic_in_entered.delete(0, END) #清除操作
        self.file_topic_in_entered.insert(0, filePath)
        # entry state  'readonly'  'normal' 'disabled'
        # 想要实现只写内部写入，外部不可操作，插入、删除的时候把状态变为normal，完成插入、删除后再改回disabled/readonly
        self.file_topic_in_entered.config(state='readonly')

    # getFile2
    def get_file2(self):
        print('hello from getFileName')
        filePath = fd.askopenfilename()
        self.file_group_in_entered.delete(0, END)#清除操作
        self.file_group_in_entered.insert(0, filePath)
        self.file_group_in_entered.config(state='readonly')

    #处理文件
    def deal_file(self):
        print('hello from dealFile')
        savePath=fd.asksaveasfilename()
        self.file_topic_out_entered.delete(0, END)#清除操作
        self.file_topic_out_entered.insert(0, savePath)
        self.file_topic_out_entered.config(state='readonly')
        intfile = self.file_topic_in.get()
        self.get_out_file(json.loads(self.file2json(intfile)), 'tem_g.csv', savePath)
        self.out_msgBox()
    def deal_file2(self):
        print('hello from dealFile')
        savePath=fd.asksaveasfilename()
        self.file_group_out_entered.delete(0, END)#清除操作
        self.file_group_out_entered.insert(0, savePath)
        self.file_group_out_entered.config(state='readonly')
        intfile = self.file_group_in.get()
        self.get_out_file2(json.loads(self.file2json(intfile)), 'tem_g.csv', savePath)
        self.out_msgBox()

    def out_msgBox(self):
        msg.showinfo('提示', '导出成功')

#==============================================================================================
    #总处理函数
    def get_out_file(self,input_json, csv_file, excel_file):
        self.get_topic(input_json, csv_file)
        self.file2excel(csv_file, excel_file)
        os.remove(csv_file)
        print('process over!!')

    # 总处理函数
    def get_out_file2(self, input_json, csv_file, excel_file):
        self.get_group(input_json, csv_file)
        self.file2excel(csv_file, excel_file)
        os.remove(csv_file)
        print('process over!!')

    #json读取，转换str
    def file2json(self,json_file):
        json_str = ''
        with open(json_file, 'r', encoding='utf-8') as f:
            for line in f:
                json_str += line.strip()
        return json_str

    #转换csv格式（中间格式）
    def get_topic(self,input_json, out_file):
        out_f = open(out_file, 'w', encoding='utf-8')
        tpc_cof_tab = input_json['topicConfigTable']
        out_f.write('TOPIC,ORDER' + '\n')
        for topic in tpc_cof_tab.keys():
            if topic.startswith('%RETRY%'):   #如果是重试topic，则不记录
                pass
            else:
                out_f.write(topic + ',' + str(tpc_cof_tab[topic]['order']) + '\n')

    def get_group(self, input_json, out_file):
        out_f = open(out_file, 'w', encoding='utf-8')
        tpc_cof_tab = input_json['subscriptionGroupTable']
        out_f.write('GROUP,BROADCAST' + '\n')
        for group in tpc_cof_tab.keys():
            out_f.write(group + ',' + str(tpc_cof_tab[group]['consumeBroadcastEnable']) + '\n')

    #转换为excel格式
    def file2excel(self,infile, out_excel):
        workbook = Workbook(out_excel)
        worksheet = workbook.add_worksheet()
        with open(infile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()




#==============================================================================================

if __name__ == '__main__':
    oop = OOP()
    oop.win.mainloop()