# _*_ coding:UTF-8 _*
import json
import re
import os


p="C:\\Users\\win10\\Desktop\\rss\\"
dirs=os.listdir(p)
dirs.sort()

for dirc in dirs:    
    if dirc.find(".txt")>-1:
        print (p+dirc)
        str=('python jjjjjson.py  '+p+dirc)   
        os.system(str)    ##### 生成标题




  
