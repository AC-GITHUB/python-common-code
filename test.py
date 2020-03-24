# -*- coding: UTF-8 -*-
import os
import datetime
import mysql
import pandas
import subprocess
import re
import PIL.Image
import chardet
import configparser
import optparse
# for root, dirs, files in os.walk('E:\\project\\yiqing\\data'):
#     for file in files:
#       print(os.path.join(root,file))

# data=pandas.read_excel("E:\\project\\yiqing\\data\\重庆各区县确诊历史数据.xlsx")
# print(data.to_json())

task={}
p = subprocess.Popen("tasklist /FO table /N",shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
for line in p.stdout.readlines():
    strs= re.split(r'[\s]\s*',str(line,encoding="gbk"))
    task[strs[1]]=strs[0] 
print(strs)
print(p.returncode)
# im =PIL.Image.open(r"E:\test.png")
# print(im.save(r"E:\test.ico"))
# f=open(r"E:\数据库wiki.txt",encoding="utf-8")
# for text in f.readlines():
#   print(text)
# config = configparser.ConfigParser()
# config.read(r"E:\test.ini")
# print(config.get("database","user"))
# parser=optparse.OptionParser()
# parser.add_option("-s", "--server", dest="server", help="ftp server ip_address")
# parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
# parser.add_option("-u", "--username", dest="username", help="username info")
# parser.add_option("-p", "--password", dest="password", help="password info")
# #解析参数
# print(type(parser.parse_args()))
# pattern=re.compile("[0-9]+")
# match=re.findall("([0-9]+)","123essdsd45dssd6")
# print(pattern.match("123456"))
# print(match)
