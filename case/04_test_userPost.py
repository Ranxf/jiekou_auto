'''
Date:2018.01.03
Author:Ranxf
'''

# !/usr/bin/env python
#
import json
import requests


def test_userinfopost():
    url = "http://10.1.1.61:8080/xzrs/User/Sync"  # 测试的接口url
    data = {
        "type": "create",  # 同步用户消息类型
        "username": "uni_001",  # 用户名（唯一标识，需保存）
        "password": "04875c0fa1cc0113b91a504aaff70208",  # MD5后用户密码（需保存）
        "createTime": "2017-07-17 14:00:10.771",  # 用户创建时间（需保存）
        "lastLoginTime": "2017-07-17 14:00:10.771",  # 最后登陆时间
        "name": "测试人",  # 姓名（需保存）
        "description": "",  # 描述
        "policeNumber": "9257",  # 警号（需保存）
        "phoneNumber": "13700000000",  # 联系方式
        "organizationName": "测试组织",  # 所属组织
        "status": "1",  # 用户状态（0：正常 1：禁用 ，需保存）
        "timeStamp": "2017-07-17 14:00:10.771",  # 操作时间
        # "roles": ["XZ_ADMIN", "XZ_BUSINESS"]  # 角色代码（需保存）
        "roles": ["XZ_ADMIN"]  # 角色代码（需保存）
        }

    # data_str = json.dumps(data, ensure_ascii=False)
    data_str = json.dumps(data)

    r = requests.post(url=url, data=data_str)

    print(r.status_code)
    print(r.text)

    if r.status_code != 200:
        print("API Error" + str(r.status_code))

    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    test_userinfopost()