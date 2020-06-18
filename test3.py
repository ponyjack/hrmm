from bs4 import BeautifulSoup
from bs4 import NavigableString
from anytree import Node, RenderTree
import re

import pprint

def extract_text(node):
    if isinstance(node, NavigableString):
        return
    return  [t.strip() for t in node(text=True, recursive=False) if t.strip()]

def html_to_tree(html):
    html_data = open(html, "r", encoding="utf8").read()

    alldata = []
    soup = BeautifulSoup(html_data, "html5lib")

    invalid_tags = ["strong", "a", "img"]

    for tag in invalid_tags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()

    for v in soup.descendants:
        if v.name == "table":
            pc = len([p for p in v.parents])
            alldata.append((pc, "table")) 
        text = extract_text(v)
        if text and text != "\n":
            pc = len([p for p in v.parents])
            alldata.append((pc, text))


    root = Node("root")
    parent = root
    last_level = 0
    parentlist = []
    parentlist.append((0, parent))

    for level, data in alldata:
        if last_level >= level:
            for p in parentlist:
                if level > p[0]:
                    parent = p[1]
                    break
        c = Node(data, parent=parent)
        parentlist.insert(0, (level, c))

        last_level = level
        parent = c

    return root


pattern = re.compile(r'\s+')

def GetHtmlMap(soup):
    texts = [ re.sub(pattern, ' ', text) for text in soup.stripped_strings]
    key_value =[]

    for i,v in enumerate(texts):
        if i ==0:
            continue
        pretext = texts[i-1]

        for splitchar in ["：",":"]:
            pos = pretext.find(splitchar)
            if pos ==(len(pretext)-1)and len(v)<30:
                key_value.append({pretext.replace(splitchar,""):v})
            if pretext.find(splitchar) !=-1 and pos !=(len(pretext)-1) and len(pretext) <30:
                pretextsplit = pretext.split(splitchar)
                for pi ,pv in enumerate(pretextsplit):
                    if (pi +1)%2 ==0:
                        key_value.append({pretextsplit[pi-1]: pv})
    return key_value

    


