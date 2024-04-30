# coding: utf-8
# Project：erp_out_of_stock
# File：test.py
# Author：李福成
# Date ：2024-04-28 18:24
# IDE：PyCharm
from apis.inventory import WmsSkuStock
from apis.order import OrderList

from request import Session

if __name__ == '__main__':
    session = Session()

    # 获取分仓库存
    print(session.erpSend(OrderList(queryData=[])).json())
