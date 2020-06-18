from htmltotree import html_to_tree, tree_to_list,GetDataMap

from anytree.iterators import PreOrderIter
import re
root  = html_to_tree("/Users/zhoucheng/Documents/GitHub/HRM/doc/智联/智联招聘_胡茜_商务经理-主管_中文_20180615_1529047915690.docx.html")



resumeinfo={}

pattern = r"(?P<gender>\w+)\s+\w+\s+\((?P<year>\d+)\w(?P<month>\d+)\w\)\s+\w+\s+(?P<degree>\w+)"

salaryp = r"(?P<min>\d+)-(?P<max>\d+)"

def ParserBaseinfo(node):
    infos={}
    allcontent = tree_to_list(node)

    infos['name'] = allcontent[0][0]

    texts = []
    for v in allcontent:
        texts.extend(v[1])
    
    keyvalues =GetDataMap(texts)

    for  v in texts:
        match  = re.match(pattern, v)
        if match:
            infos['gender'] = match['gender']
            infos['birthday'] = match['year'] + "-"+  match["month"]
            infos['degree'] = match['degree']
        if v.find("|")!=-1:
            items = [t.strip() for t in v.split("|")]
            values =GetDataMap(items)
            keyvalues.extend(values)
    
    for data in keyvalues:
        for k,v in data.items():
            if k =="手机":
                infos["phone"]=v
            elif k =="现居住地":
                infos["living_address"]=v
            elif k =="身份证":
                infos["id_card"]=v
            elif k =="E-mail":
                infos["email"]=v
            elif k =="户口":
                infos["hukou_address"]=v
    return infos


def ParserExpectJob(node):
    infos={}
    allcontent = tree_to_list(node)

    texts = []
    for v in allcontent:
        texts.extend(v[1])

    keyvalues =GetDataMap(texts)

    for data in keyvalues:
        for k,v in data.items():
            if k =="期望工作地区":
                infos["expect_jlocation"]=v
            elif k =="期望月薪":
                infos["expect_salary"]=v
                match = re.match(salaryp, v)
                if match:
                    infos["expect_salary_min"]=match['min']
                    infos["expect_salary_max"]=match['max']
            elif k =="期望工作性质":
                infos["expect_jnature"]=v
            elif k =="期望从事职业":
                infos["expect_job"]=v
            elif k =="期望从事行业":
                infos["expect_industry"]=v
    
    return infos

def ParserSelfEvaluation(node):
    infos={}
    allcontent = tree_to_list(node)

    texts = []
    for v in allcontent:
        texts.extend(v[1])

    infos['self_evaluation'] = '\n'.join(texts)
    return infos

jobdatep= r"(?P<st>\S+)\s+-\s+(?P<et>\S+)\s+(?P<cpy>\w+)"
position__salary_p= r"(?P<p>\w+)\s+\|\s+(?P<s>\S+)"
industry__nature_size= r"(?P<i>\S+)\s+\|\s+\w+\S(?P<n>\w+)\s+\|\s+\w+\S(?P<s>\S+)"
def ParserJob(node,treeiter):
    infos={}
    allcontent = tree_to_list(node,treeiter)
    
    # print(allcontent)
    texts = []
    for v in allcontent:
        texts.append(v[1])
    match  = re.match(jobdatep, texts[0][0])
    if match:
        infos["start_date"]= match['st'].replace('.','-')
        infos["end_date"]= match['st'].replace('.','-')
        infos["cpy"]= match['cpy']
    match  = re.match(position__salary_p, texts[1][0])
    if match:
        infos["position"]= match['p']
        infos["salary"]= match['s']
    match  = re.match(industry__nature_size, texts[2][0])
    if match:
        infos["cpy_nature"]= match['n']
        infos["cpy_size"]= match['s']
        infos["industry"]= match['i']

    infos["content"] = "\n".join(texts[4])

    # print(infos)
    # infos['self_evaluation'] = '\n'.join(texts)
    return infos




eductionp= r"(?P<st>\S+)\s+-\s+(?P<et>\S+)\s+(?P<college>\w+)\s+(?P<major>\w+)\s+(?P<degree>\w+)"
def ParserEduction(node,treeiter):
    infos={}
    allcontent = tree_to_list(node,treeiter)
    
    # print(allcontent)
    texts = []
    for v in allcontent:
        texts.append(v[1])
    match  = re.match(eductionp, texts[0][0])
    if match:
        infos["start_date"]= match['st'].replace('.','-')
        infos["end_date"]= match['st'].replace('.','-')
        infos["college"]= match['college']
        infos["major"]= match['major']
        infos["degree"]= match['degree']

    return infos




trainingp= r"(?P<st>\S+)\s+-\s+(?P<et>\S+)"
def ParserTraining(node,treeiter):
    infos={}
    allcontent = tree_to_list(node,treeiter)
    
    # print(allcontent)
    texts = []
    for v in allcontent:
        texts.append(v[0])
    
    def One(group):
        infos = {}
        keyvalues =GetDataMap(group)
        match = re.match(trainingp,group[0])
        if match:
            infos['start_date']=match['st'].replace('.','-')
            infos['end_date']=match['et'].replace('.','-')

        for data in keyvalues:
            for k,v in data.items():
                if k =="培训机构":
                    infos["org"]=v
                elif k =="所获证书":
                    infos["cert"]=v
                elif k =="培训描述":
                    infos["cont"]=v
        return infos
               
    
    group =[]
    last = 0
    for i,v in enumerate(texts):
        if re.match(trainingp,v):
            if i:
                group.append(texts[last:i])
            last = i
    group.append(texts[last:])

    infos['trainings'] = [One(g) for g in group]
    return infos


def ParserLanguage(node,treeiter):
    infos={}
    allcontent = tree_to_list(node)

    texts = []
    for v in allcontent:
        texts.append(v[0])
    languages=[]
    for v in texts:
        l = {}
        datas = v.replace("："," ").split(" ")
        l['language_name'] = datas[0]
        for t in datas:
            if t.find("读写能力")!=-1:
                l["language_read_write"] = t[t.find("读写能力"):]
            elif t.find("听说能力")!=-1:
                l["language_listen_speak"] = t[t.find("听说能力"):]
        languages.append(l)
    if languages:
        infos["languagedetails"]=languages
    return infos



def ParserSkill(node,treeiter):
    infos={}
    allcontent = tree_to_list(node)

    texts = []
    for v in allcontent:
        texts.append(v[0])
    skills=[]
    for v in texts:
        s = {}
        datas = v.replace("："," ").split(" ")
        skills.append({'name':datas[0],"level":datas[1]})
    if skills:
        infos['skills']=skills
    return infos


treeiter = PreOrderIter(root)
# print(next(treeiter))
for v in treeiter:
    if v.name.find("ID：") !=-1:
        ParserBaseinfo(next(treeiter))
    if v.name.find("求职意向") !=-1:
        ParserExpectJob(next(treeiter))
    if v.name.find("自我评价") !=-1:
        ParserSelfEvaluation(next(treeiter))
    if v.name.find("工作经历") !=-1:
        for v in treeiter:
            # print(v)
            if v.name !="tag_table":
                break
            ParserJob(v,treeiter)
    if v.name.find("教育经历") !=-1:
        for v in treeiter:
            # print(v)
            if v.name !="tag_table":
                print(v)
                break
            ParserEduction(v,treeiter)
            
    if v.name.find("培训经历") !=-1:
        for v in treeiter:
            if v.name !="tag_table":
                print(v.name)
                break
            ParserTraining(v,treeiter)

    if v.name.find("语言能力") !=-1:
        print(v.name)
        for v in treeiter:
            if v.name !="tag_table":
                break
            print(ParserLanguage(v,treeiter))
    
    if v.name.find("专业技能") !=-1:
        print(v.name)
        for v in treeiter:
            if v.name !="tag_table":
                break
            print(ParserSkill(v,treeiter))
    
