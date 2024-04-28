import json

import requests


class FileDO:
    def __init__(self,_identifier):
        self._identifier = _identifier
        self.service_url = 'http://127.0.0.1:21030/SCIDE/SCManager'

    def downloadFileDO(self):
        """
        获取文件的本地路径。

        参数：
            无。

        返回：
            json{'success': True, 'datas': ['ids:dataset/999a2b6ca6ce8a0d0c88ca99b602613e83d926daf9de1c72bca5db15a399c986']}

        """
        # 参数
        params = {
            'action': 'executeContract',
            'contractID': 'IODIC',
            'operation': "downloadFileDO",
            'arg': {"dpml": f"<dpml><data>{self._identifier}</data></dpml>"}
        }

        # 发送请求
        response = requests.post(self.service_url, json=params)
        parsed_json = json.loads(response.text)
        # 提取 "result" 字段
        result = parsed_json["result"]

        # 打印响应内容
        return result

    def getFileLocalPath(self):
        params = {
            'action': 'executeContract',
            'contractID': 'IODIC',
            'operation': "toLocalPath",
            'arg': {"do": f"{self._identifier}"}
        }
        # 发送请求
        response = requests.post(self.service_url, json=params)
        parsed_json = json.loads(response.text)
        # print(parsed_json)
        # 提取 "result" 字段
        filePath = parsed_json["result"]["filePath"]

        # 返回路径
        return filePath

    def getDownloadProgress(self):
        # 参数
        params = {
            'action': 'executeContract',
            'contractID': 'IODIC',
            'operation': "getDownloadProgress",
            'arg': {"do": f"{self._identifier}"}
        }

        # 发送请求
        response = requests.post(self.service_url, json=params)
        parsed_json = json.loads(response.text)
        # 提取 "result" 字段
        result = parsed_json["result"]

        # 打印响应内容
        return result
