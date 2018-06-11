import json
import requests


def test_userinfoget():
    url = "http://10.1.1.166:8080/xzrs/User/Sync"
    # url = "http://10.1.1.19/xzrs/User/Sync"
    response = requests.get(url=url)
    userget_data = json.loads(response.text)

    # 使用参数让 JSON 数据格式化输出,树形打印json
    data = json.dumps(userget_data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
    # data = json.dumps(userget_data, indent=4, sort_keys=True, separators=(',', ': '))
    # print(response.text)
    print(response.status_code)
    print(data)


if __name__ == "__main__":
    test_userinfoget()