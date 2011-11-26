#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import json
import sys

def Shortened(site):
    url = "http://ux.nu/api/short?"
    short = urllib.urlopen(url + urllib.urlencode({"url": site})).read()
    return json.loads(short)

def Expanded(site):
    url = "http://ux.nu/api/expand?"
    expand = urllib.urlopen(url + urllib.urlencode({"url": site})).read()
    return json.loads(expand)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        site = raw_input(u"短縮または展開したいURLを入力してください。 >>>")
    else:
        site = sys.argv[1]

    if site[7:12] == "ux.nu":
        try:
            print(Expanded(site)["data"]["exp"])
        except KeyError:
            print(u"Error: URLが間違っていませんか？")
    else:
        try:
            print(Shortened(site)["data"]["url"])
        except KeyError:
            print(u"Error: URLが間違っていませんか？")
