'''
Date:2018.01.03
Author:Ranxf
'''

import json
import requests
import unittest
from common.logger import Log

class Interface(unittest.TestCase):
    log = Log()

    def test_heartbeatget(self):
        url = "http://10.1.1.166:8080/xzrs/System/HeartBeat"

        heartbeatget = requests.get(url=url)
        sendVerifycode_data = json.loads(heartbeatget.text)
        print(heartbeatget.text)
        print(sendVerifycode_data)
        return sendVerifycode_data

        # print(heartbeatget.status_code)
        # print(type(sendVerifycode_data))

if __name__ == "__main__":
    unittest.main()