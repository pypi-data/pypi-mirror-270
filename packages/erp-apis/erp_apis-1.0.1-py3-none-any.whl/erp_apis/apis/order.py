# coding: utf-8
# Project：erp_out_of_stock
# File：order.py
# Author：李福成
# Date ：2024-04-28 18:23
# IDE：PyCharm
# 订单API
from typing import Optional, Union
from request import Request
from util import dumps, getDefaultParams, JTable1

url = 'https://www.erp321.com/app/order/order/list.aspx'


def OrderRequest(data: dict, url: str = url, method: str = 'LoadDataToJSON') -> Request:
    return Request(
        method='POST',
        url=url,
        params=getDefaultParams({'defaultParams': ["ts___", "_c"], 'am___': method}),
        data={
            '__CALLBACKID': 'JTable1',
            **data
        },
        callback = JTable1
    )


# 获取订单
def OrderList(queryData: Optional[list] = None, page_num: int = 1, page_size: int = 500):
    '''
    获取订单
    :param page_num: 页数
    :param page_size:  每页条数
    :param queryData:  查询条件
    :return: 查询结果
    '''
    if queryData is None: queryData = []
    return OrderRequest({
        '_jt_page_size': page_size,
        '__CALLBACKPARAM': dumps(
            {
                "Method": "LoadDataToJSON",
                "Args": [
                    page_num,
                    dumps(queryData),
                    "{}"
                ]
            }
        ),
    },method='LoadDataToJSON')


# 修改订单异常类型
def Questions(questionName: str, questionMsg: str, oid: Union[str, int]):
    '''
    修改订单异常类型
    :param questionName: 异常分类名称
    :param questionMsg:  异常信息
    :param oid:  内部订单号
    :return: 执行结果
    '''
    return OrderRequest({
        '__CALLBACKPARAM': dumps(
            {"Method": "Questions", "Args": [questionName, questionMsg, str(oid)], "CallControl": "{page}"}
        ),
    },
    method='Questions')


# 修改备注
def Remarks(oid: Union[str, int], remarksMsg: str = '', isAppendRemarks: bool = True, flag: str = None):
    '''
    修改备注
    :param oid:  内部订单号
    :param remarksMsg:  备注信息
    :param isAppendRemarks:  是否追加备注
    :param flag:  旗帜类型： 1:红  2:黄  3:绿  4:蓝   5:紫
    :return: 执行结果
    '''
    return OrderRequest({
        '__CALLBACKID': 'JTable1',
        '__CALLBACKPARAM': dumps({
            "Method": "SaveAppendRemarks",
            "Args": [
                'null' if flag is None else str(flag),
                remarksMsg,
                str(oid),
                'true' if isAppendRemarks else 'false'
            ],
            "CallControl": "{page}"
        }),
    },
    method='SaveAppendRemarks')


# 换商品
def ChangeBatchItems(oid: Union[str, int], oldBatchItems: list, newBatchItems: list):
    '''
    换商品
    :param oid:  内部订单号
    :param oldBatchItems:  旧商品
    :param newBatchItems:  新商品
    :return: 执行结果
    '''
    return OrderRequest({
        '__CALLBACKID': 'JTable1',
        '__CALLBACKPARAM': '{"Method":"ChangeBatchItem","Args":["39044577","{"items":[{"sku_id":"M-男女宽松T-白色-光合作用-CP","qty":1,"price":0,"amount":"0.00","is_gift":false,"oi_id":56037011,"is_del":true,"sku_type":"normal","is_new":false},{"sku_id":"M-男女宽松T-福袋","qty":1,"price":-99999,"amount":"-99999.00","is_gift":false,"oi_id":0,"is_del":false,"is_new":true},{"sku_id":"M-女宽松背心-米色-宇宙恒星-CP","qty":1,"price":39.9,"amount":"39.90","is_gift":false,"oi_id":55970466,"is_del":false,"sku_type":"no_deliver","is_new":false},{"sku_id":"M-女宽松背心-米色-樱桃碎-CP","qty":1,"price":39.9,"amount":"39.90","is_gift":false,"oi_id":55970467,"is_del":false,"sku_type":"no_deliver","is_new":false},{"sku_id":"M-女宽松背心-黑色-复古故事书-CP","qty":1,"price":39.9,"amount":"39.90","is_gift":false,"oi_id":55970468,"is_del":false,"sku_type":"no_deliver","is_new":false}]}"],"CallControl":"{page}"}',
    },method='ChangeBatchItem')
