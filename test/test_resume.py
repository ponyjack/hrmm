import requests
from .const import *
import uuid
import json
# from .data import templteresume

API_URL = HOST_URL + "/resume/"
RESUME_API_URL= API_URL+"resumes/"
UPLOAD_API_URL= API_URL+"upload/"


templteresume = json.load(open("data.json"))


def InsertOneResume(**kw):
    data = templteresume.copy()
    name = uuid.uuid4().hex[:6]
    data["name"] = name

    for k, v in kw.items():
        data[k] = v

    respond = requests.post(RESUME_API_URL, json=data)
    assert respond.status_code == 201, respond.text
    return name


def testCreateResume():
    name = uuid.uuid4().hex[:6]
    data = {
        "name": name,
        "surname": "kkkkk",
        "gender": "kkkkk",
        "age": "kkkkk",
        "height": "kkkkk",
        "weight": "kkkkk",
        "marital_status": "kkkkk",
        "birthday": "kkkkk",
        "hukou_address": "kkkkk",
        "hukou_address_norm": "kkkkk",
        "hometown_address": "kkkkk",
        "hometown_address_norm": "kkkkk",
        "id_card": "kkkkk",
        "race": "kkkkk",
        "nationality": "kkkkk",
        "polit_status": "kkkkk",
        "languages": "kkkkk",
        "english_level": "kkkkk",
        "computer_level": "kkkkk",
        "blog": "kkkkk",
        "work_year": "kkkkk",
        "work_year_norm": "kkkkk",
        "work_year_inf": "kkkkk",
        "work_start_time": "2019-09-02",
        "work_position": "kkkkk",
        "work_company": "kkkkk",
        "work_industry": "kkkkk",
        "work_status": "kkkkk",
        "work_location": "kkkkk",
        "work_location_norm": "kkkkk",
        "work_job_nature": "kkkkk",
        "grad_time": "2019-09-02",
        "college": "kkkkk",
        "college_type": "kkkkk",
        "max_length": "kkkkk",
        "college_rank": "kkkkk",
        "college_dept": "kkkkk",
        "major": "kkkkk",
        "degree": "kkkkk",
        "recruit": "kkkkk",
        "resume_type": "kkkkk",
        "resume_source": "kkkkk",
        "resume_id": "kkkkk",
        "resume_name": "kkkkk",
        "resume_parse_time": "kkkkk",
        "resume_update_time": "2019-09-02 12:30",
    }
    respond = requests.post(RESUME_API_URL, data)
    assert respond.status_code == 201, respond.text
    assert respond.json()["name"] == name

    respond = requests.get(RESUME_API_URL)
    assert respond.status_code == 201, respond.text
    assert len(respond.json()) >= 1


def testResumePage():
    name = InsertOneResume()
    assert name != None
    name2 = InsertOneResume()
    assert name2 != None

    respond = requests.get(RESUME_API_URL)
    assert respond.status_code == 200, respond.text
    result = respond.json()
    assert result["count"] >= 2

    respond = requests.get(RESUME_API_URL, params={"page": 1, "page_size": 1})
    assert respond.status_code == 200, respond.text
    result = respond.json()
    assert len(result["results"]) == 1

    respond = requests.get(RESUME_API_URL, params={"page": 1, "page_size": 2})
    assert respond.status_code == 200, respond.text
    result = respond.json()
    assert len(result["results"]) == 2


def testCreateAllData():
    data = {
        "first_name": "zhou",
        "last_name": "cheng",
        "email": "zhoucheng@kingsoft.com",
        "middle_name": "middle",
        "designation": "sdfsdfsdf",
        "career_goal": "career_goal",
        "city": "city",
        "address": "address",
        "phone_number": "123234123",
        "email": "chengz.com@gmail.com",
        "website": "http://aa.com",
        "linkedin_url": "http://aa.com",
        "twitter_url": "http://aa.com",
        "facebook_url": "http://aa.com",
        "summary": "summary",
        "jobs": [
            {
                "company": "company",
                "location": "location",
                "title": "title",
                "company_url": "http://aa.com",
                "description": "description",
                "start_date": "2017-09-20",
                "end_date": "2017-09-20",
                "is_current": "false",
                "is_public": "true",
            }
        ],
    }
    respond = requests.post(RESUME_API_URL, json=data)
    assert respond.status_code == 201, respond.text
    result = respond.json()
    for k, v in data.items():
        assert result[k] == v, result[k]


def testFilter():
    name = InsertOneResume()
    filter = {"name": name}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.text
    assert respond.json()["results"][0]["name"] == name

    name2 = InsertOneResume()
    filter = {"name__in": ",".join([name, name2])}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.text
    assert respond.json()["results"][0]["name"] == name
    assert respond.json()["results"][1]["name"] == name2


def testGetResumeData():
    data = templteresume.copy()
    name = uuid.uuid4().hex[:6]
    data["name"] = name

    respond = requests.post(RESUME_API_URL, json=data)
    assert respond.status_code == 201
    result = respond.json()
    assert result["id"] != None

    respoond = requests.get(RESUME_API_URL + "/" + str(result["id"]) + "/")
    assert respond.json()["name"] == name


def testModiyNestData():
    data = templteresume.copy()
    name = uuid.uuid4().hex[:6]
    data["name"] = name

    respond = requests.post(RESUME_API_URL, json=data)
    assert respond.status_code == 201
    result = respond.json()
    assert result["id"] != None
    ids = result["id"]
    data = {
        "jobs": [
            {
                "end_date": "2017-06-01",
                "content": "工作描述:   " "负责后台代码编写,模块开发,controller层调用上级接口,测试接口有限性",
                "cpy": "apple1",
                "cpy_nature": "民营公司",
                "cpy_size": "150-500人",
                "dept": "java开发部",
                "duration": "8个月",
                "industry": "计算机软件",
                "position": "Java开发工程师",
                "start_date": "2016-10-01",
            },
        ],
    }

    respond = requests.patch(RESUME_API_URL + str(ids) + "/", json=data)
    assert respond.status_code == 200
    result = respond.json()["jobs"]
    assert "apple1" in [v["cpy"] for v in result]

    jids = [v["id"] for v in result]
    data = {
        "jobs": [
            {
                "id": jids[0],
                "end_date": "2017-06-01",
                "cpy": "apple4455",
                "cpy_nature": "民营公司",
                "cpy_size": "150-500人",
                "dept": "java开发部",
                "duration": "8个月",
                "industry": "计算机软件",
                "position": "Java开发工程师",
                "start_date": "2016-10-01",
            }
        ],
    }
    respond = requests.patch(RESUME_API_URL + str(ids) + "/", json=data)
    assert respond.status_code == 200
    result = respond.json()["jobs"]

    for v in result:
        if v["id"] == jids[0]:
            assert v["cpy"] == "apple4455"
    data = {
        "jobs": [
            {
                "id": 1,
                "end_date": "2017-06-01",
                "cpy": "apple4455",
                "cpy_nature": "民营公司",
                "cpy_size": "150-500人",
                "dept": "java开发部",
                "duration": "8个月",
                "industry": "计算机软件",
                "position": "Java开发工程师",
                "start_date": "2016-10-01",
            }
        ],
    }
    respond = requests.patch(RESUME_API_URL + str(ids) + "/", json=data)
    assert respond.status_code == 400, respond.json()


def testFilterWithCondition():
    name = InsertOneResume(birthday="2023-01-06")
    filter = {'birthday':"2023-01-06"}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.text
    assert name in [ v['name'] for v in  respond.json()["results"]]

    filter = {'birthday__gte':"2023-01-06"}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.json()
    assert name in [ v['name'] for v in  respond.json()["results"]]

    filter = {'birthday__gt':"2023-01-06"}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.json()
    assert name  not in [ v['name'] for v in  respond.json()["results"]]


    filter = {'birthday__gt':"2023-01-06"}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.json()
    assert name  not in [ v['name'] for v in  respond.json()["results"]]

    filter = {'birthday__range':["2023-01-04","2023-01-09"]}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.json()
    assert name  not in [ v['name'] for v in  respond.json()["results"]]


    filter = {"name":name,'birthday__range':"2023-01-04,2023-01-09"}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.json()
    assert len(respond.json()["results"]) ==1
    assert name   in [ v['name'] for v in  respond.json()["results"]]


     

    name = InsertOneResume(skills=[{"name": "fuck"},{"name": "fuck2"}])
    filter = {'skills__name':"fuck"}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 200, respond.text
    assert name in [ v['name'] for v in  respond.json()["results"]]

    name = InsertOneResume(skills=[{"name": "fuck"}])
    filter = {'skills__name':"fuck",'name':name}
    respond = requests.get(RESUME_API_URL, params=filter)
    assert respond.status_code == 201, respond.json()['results'][0]['skills']
    assert name not in [ v['name'] for v in  respond.json()["results"]]
    


def testUploadResume():
    files = {'upload_file': open('data.txt','rb')}

    respond = requests.post(UPLOAD_API_URL, files=files)
    assert respond.status_code == 201, respond.json()
    assert respond.json()["id"]!=None