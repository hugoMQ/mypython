#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-7-17 16:23
# @Author  : yuguo
import json
def Result(msg=None, error=None, skip=None, **kwargs):
    '''
    返回结果转JSON字符串
    {
        "status":1/-1, #状态值 ，成功为1，异常为-1
        "error":"msg", #异常返回信息
        "data":data #返回json数据 
    }
    '''

    r1 = {}
    r1['rtnCode'] = 0 #默认成功
    if msg:
        r1["rtnMsg"] = msg
    elif error:
        r1['rtnCode'] = -9999 #默认失败
        r1['rtnMsg'] = error
    elif skip:
        r1['rtnCode'] = 1
        r1['rtnMsg'] = skip

    r1.update(kwargs)

    return json.dumps(r1,ensure_ascii=False)
