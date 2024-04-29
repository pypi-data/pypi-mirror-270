# coding: utf-8
# Project：erp_out_of_stock
# File：order.py
# Author：李福成
# Date ：2024-04-28 18:23
# IDE：PyCharm
# 订单API
from typing import Optional, Union
from request import Request
from util import dumps, getDefaultParams

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
    return Request(
        method='POST',
        url='https://www.erp321.com/app/order/order/list.aspx',
        params=getDefaultParams({'defaultParams': ["ts___", "am___", "_c"]}),
        data={
            '_jt_page_size': page_size,
            '__CALLBACKID': 'JTable1',
            '__CALLBACKPARAM': dumps(
                {
                    "Method": "LoadDataToJSON",
                    "Args": [
                        page_num, dumps(queryData),
                        "{}"
                    ]
                }
            ),
        },
        parseResponse=True
    )



# 修改订单异常类型
def Questions(questionName: str, questionMsg: str, oid: Union[str, int]):
    '''
    修改订单异常类型
    :param questionName: 异常分类名称
    :param questionMsg:  异常信息
    :param oid:  内部订单号
    :return: 执行结果
    '''
    return Request(
        method='POST',
        url='https://www.erp321.com/app/order/order/list.aspx',
        params=getDefaultParams({'defaultParams': ["ts___", "_c"],'am___': 'Questions'}),
        data={
            '__CALLBACKID': 'JTable1',
            '__CALLBACKPARAM': dumps({"Method":"Questions","Args":[questionName,questionMsg, str(oid)],"CallControl":"{page}"}),
        },
        parseResponse=True
    )



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
    return Request(
        method='POST',
        url='https://www.erp321.com/app/order/order/list.aspx',
        params=getDefaultParams({'defaultParams': ["ts___", "_c"],'am___': 'SaveAppendRemarks'}),
        data={
            '__CALLBACKID': 'JTable1',
            '__CALLBACKPARAM': dumps({
                "Method":"SaveAppendRemarks",
                "Args":[
                    'null' if flag is None else str(flag),
                    remarksMsg,
                    str(oid),
                    'true' if isAppendRemarks else 'false'
                ],
                "CallControl":"{page}"
            }),
        },
        parseResponse=True
    )
