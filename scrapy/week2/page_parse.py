#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-12-26 20:23
# @Author  : yuguo

from bs4 import BeautifulSoup
import requests
import time
import pymongo


#得到总渠道
def get_channel(url_host,start_url,channel_link):
    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#ymenu-side > ul > li > ul > li > b > a')
    for link in links:
        # if link in 'tongxunyw':
        #     pass
        page_url = url_host + link.get('href')
        channel_link.append(page_url)
    return channel_link


client = pymongo.MongoClient('localhost',27017)
mongo_db = client['tongcheng']
url_list = mongo_db['url_list']
url_info = mongo_db['url_info']

#spyder1 得到每个物品的链接
'''
channel
https://bj.58.com/shouji/
url_link
https://bj.58.com/shouji/0/pn2/
item_link
https://bj.58.com/shouji/40607376578578x.shtml?link_abtest=&psid=170549718206748361030747430&entinfo=40607376578578_p&slot=-1
'''
def get_links_from(channel,pages,who_sells=0):
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    web_data = requests.get(list_view)
    soup = BeautifulSoup(web_data.text,'lxml')

    # time.sleep(1)

    links = soup.select(' tr.ac_item > td.t > a')
    for link in links:
        item_link = link.get('href').split('?')[0]
        url_list.insert_one({'url':item_link})
        print(item_link)
        get_info_from(item_link)

# channel = 'https://bj.58.com/shouji/'
# get_links_from(channel,2)

#spyder2  得到每个物品的详细信息
'''
info_url = https://bj.58.com/shouji/40608178173717x.shtml
title
date
price
area
'''
def get_info_from(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    # time.sleep()

    title = soup.title.text
    date = soup.select('div.detail-title__info__text')[0].text.split()[0]
    price = soup.select('span.infocard__container__item__main__text--price')[0].text.split()[0]
    area_tmp = soup.select('div.infocard__container__item__main > a')
    area = area_tmp[0].text + '-' + area_tmp[1].text
    info = {}
    info = {
        'title':title,
        'date':date,
        'price':int(price) if price!='面议' else 0,
        'area':area,
        'url':url
    }
    print(info)
    url_info.insert_one(info)


# url = 'https://bj.58.com/shouji/40596595961496x.shtml'
# get_info_from(url)


start_url = 'https://bj.58.com/sale.shtml'
url_host = 'https://bj.58.com'
channel_links = []
channel_links = get_channel(url_host,start_url,channel_links)
print(channel_links)
for channel in channel_links:
    print(channel)
    for i in range(1,50):
        get_links_from(channel,i)
