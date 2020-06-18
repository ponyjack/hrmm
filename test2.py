from test3 import html_to_tree


import glob 
import subprocess
import pprint
from collections import OrderedDict
from anytree.exporter import DictExporter
from anytree.exporter import JsonExporter
import json
exporter = JsonExporter(ensure_ascii=False)

from bs4 import BeautifulSoup


# for p in glob.glob("/Users/zhoucheng/Documents/GitHub/HRM/doc/智联/*.docx"):
#     subprocess.call(["mammoth",p,p+".html"])
#     root = html_to_tree(p+".html")
    

    # exporter.write(root,open(p+".html"+".json","w"))


# html = open("/Users/zhoucheng/Documents/GitHub/HRM/doc/智联/智联招聘_曹哲军_中文_20180606_40264.docx.html","r").read()
# soup = BeautifulSoup(html)


root = html_to_tree("/Users/zhoucheng/Documents/GitHub/HRM/doc/智联/智联招聘_曹哲军_中文_20180606_40264.docx.html")
from anytree import Node, RenderTree, AsciiStyle, PreOrderIter

for v in PreOrderIter(root):
    print(v)