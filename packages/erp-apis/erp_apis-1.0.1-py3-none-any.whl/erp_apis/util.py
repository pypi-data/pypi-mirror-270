# coding: utf-8
# Project：erp_out_of_stock
# File：util.py
# Author：李福成
# Date ：2024-04-29 9:35
# IDE：PyCharm
import json
import time

from requests import Response


def dumps(obj, **kwargs):
    return json.dumps(obj, **kwargs, separators=(',', ':'), ensure_ascii=False)


def getDefaultParams(params: dict = None) -> dict:
    rand_params = {
        '_c': lambda: 'jst-epaas',
        '_t': lambda: int(time.time() * 1000),
        '_float': lambda: True,
        'ts___': lambda: int(time.time() * 1000),
        'am___': lambda: 'LoadDataToJSON',
    }
    if params.get('defaultParams'):
        for k in params.get('defaultParams'):
            params.update({k: rand_params.get(k)()})
    del params['defaultParams']
    return params


def JTable1(res: Response):
    res_data = json.loads(res.text[2:])
    if res_data.get('ReturnValue') and isinstance(res_data.get('ReturnValue'), dict):
        res_data['ReturnValue'] = json.loads(res_data.get('ReturnValue'))
    res._content = json.dumps(res_data).encode('utf-8')
    return res
