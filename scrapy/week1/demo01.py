#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-12-26 16:02
# @Author  : yuguo
# 小猪之家

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
xiaozhu = client['xiaozhu']
bnb_info = xiaozhu['info']

# 如何批量获取链接 http://bj.xiaozhu.com/search-duanzufang-p1-0/

page_link = []  # <- 每个详情页的链接都存在这里，解析详情的时候就遍历这个列表然后访问就好啦~

def get_page_link(page_number):
    for i in range(1, page_number):  # 每页24个链接,这里输入的是页码
        print(i)
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i)
        print(full_url)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        for link in soup.select('a.resule_img_a'):  # 找到这个 class 样为resule_img_a 的 a 标签即可
            page_link.append(link)
            get_info(link.get('href'))
            time.sleep(2)

info = []
#获取信息 url = 'http://bj.xiaozhu.com/fangzi/1508951935.html'
def get_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)

    title = soup.title.text
    address = soup.select('div.pho_info > p > span.pr5')[0].text.strip()
    price = soup.select('#pricePart > div.day_l > span')[0].text
    pic = soup.select('#curBigImage')[0].get('src')

    host_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text
    host_gender = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')[0].get('class')[0]

    # print(title,price,pic,host_name,host_gender)

    def get_host_gender(host_gender):
        if host_gender == 'member_girl_ico':
            return 'female'
        else:
            return 'male'

    info = {
        'title': title,
        'address':address,
        'price':int(price),
        'pic':pic,
        'host_name':host_name,
        'host_gender':get_host_gender(host_gender)
    }
    bnb_info.insert_one(info)

# get_page_link(12)
# -------------------补充------------------
# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
for i in bnb_info.find():
        if i['price'] <200:
            print(i)
print('====================')
for item in bnb_info.find({'price': {'$lt': 250}}):
    print(item)
# uurl = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'
# wb_data2 = requests.get(uurl)
# soup2 = BeautifulSoup(wb_data2.text, 'lxml')
# print(soup2.select('a.resule_img_a'))
# ---------------------