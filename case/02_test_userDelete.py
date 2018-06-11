'''
Date:2018.01.03
Author:Ranxf
'''
import json
import requests


# 删除用户
def test_userinfodelete():
    # url = "http://10.1.1.19/xzrs/User/Sync"
    url = "http://10.1.1.166:8080/xzrs/User/Sync"
    userinfodelete = {
        "type": "delete",  # 同步用户消息类型
        "username": "uni_001",  # 用户名（唯一标识，需保存）
        "password": "04875c0fa1cc0113b91a504aaff70208",  # MD5后用户密码（需保存）
        "createTime": "2017-07-17 14:00:10.771",  # 用户创建时间（需保存）
        "lastLoginTime": "2017-07-17 14:00:10.771",  # 最后登陆时间
        "name": "xiaoxiao",  # 姓名（需保存）
        "description": "",  # 描述
        "policeNumber": "9000",  # 警号（需保存）
        "phoneNumber": "13700000000",  # 联系方式
        "organizationName": "测试组织",  # 所属组织
        "status": "1",  # 用户状态（0：正常 1：禁用 ，需保存）
        "timeStamp": "2017-07-17 14:00:10.771",  # 操作时间
        "roles": ["XZ_ADMIN"]  # 角色代码（需保存）

    }
    r = requests.delete(url=url, data=userinfodelete)

    registeruser_data = json.loads(r.text)
    print(r.status_code)

    print(r.text)
    print(registeruser_data)

if __name__ == "__main__":
    test_userinfodelete()

