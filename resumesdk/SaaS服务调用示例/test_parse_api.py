# coding: utf-8

import sys
import base64
import requests
import json


def test_parser(url, fname, uid, pwd):
    # 读取文件内容，构造请求
    cont = open(fname, "rb").read()
    base_cont = base64.b64encode(cont)
    base_cont = base_cont.decode("utf-8") if sys.version.startswith("3") else base_cont  # 兼容python2与python3
    data = {
        "uid": uid,
        "pwd": str(pwd),
        "file_name": fname,
        "file_cont": base_cont,
    }

    # 发送请求
    res = requests.post(url, data=json.dumps(data))

    # 解析结果
    res_js = json.loads(res.text)
    print("result:\n%s\n" % (json.dumps(res_js, indent=2, ensure_ascii=False)))

    if "result" in res_js:
        print("name: %s" % (res_js["result"].get("name", "None")))
    f = open("data.txt", "w")
    f.write(res.text)
    return res_js


if __name__ == "__main__":
    url = "http://www.resumesdk.com/api/parse"
    fname = u"/Users/zhoucheng/Documents/GitHub/HRM/doc/前程/51job_高永超_JAVA开发工程师(622666553).doc"  # 替换为你的文件名
    uid = 2005221  # 替换为你的用户名（int格式）
    pwd = "7r6QDj"  # 替换为你的密码（str格式）
    res_js = test_parser(url, fname, uid, pwd)
