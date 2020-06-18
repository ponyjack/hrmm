from django.db import models

# Create your models here.


class Resume(models.Model):
    name = models.CharField(max_length=255)  # 人名，比如“姚明”
    surname = models.CharField(max_length=255)  # 姓氏，比如“姚”
    gender = models.CharField(max_length=255)  # 男、女、male、female
    age = models.CharField(max_length=255)  # 年龄，比如“25”
    height = models.CharField(max_length=255, blank=True, null=True)  # 180cm
    weight = models.CharField(max_length=255, blank=True, null=True)  # 75kg
    marital_status = models.CharField(max_length=255)  # 已婚、未婚、已结婚、未结婚、保密
    birthday = models.DateField()  # 比如：2019.10.01或者2019.10
    hukou_address = models.CharField(max_length=255, blank=True, null=True)  # 用户填写的地址，比如“上海市虹口区广粤路xx弄x号xxx室”
    hukou_address_norm = models.CharField(max_length=255, blank=True, null=True)  # 规范化到“区县”一级，比如“中国-上海市-虹口区”
    hometown_address = models.CharField(max_length=255, blank=True, null=True)  # 用户填写的地址，比如“上海市虹口区广粤路xx弄x号xxx室”
    hometown_address_norm = models.CharField(max_length=255, blank=True, null=True)  # 规范化到“区县”一级，比如“中国-上海市-虹口区”
    id_card = models.CharField(max_length=255, blank=True, null=True)  # 身份证号
    race = models.CharField(max_length=255, blank=True, null=True)  # 比如：汉、汉族
    nationality = models.CharField(max_length=255, blank=True, null=True)  # 比如：中国、越南、美国
    polit_status = models.CharField(max_length=255, blank=True, null=True)  # 比如：党员、团员、共青团员、共产党员、无党派人士、共产党党员
    languages = models.CharField(max_length=255, blank=True, null=True)  # 英语、日语等，多个语言间用逗号分隔
    english_level = models.CharField(max_length=255, blank=True, null=True)  # 比如：大学英语6级、专业英语8级
    computer_level = models.CharField(max_length=255, blank=True, null=True)  # 计算机水平
    blog = models.CharField(max_length=255, blank=True, null=True)  # 博客/主页地址
    work_year = models.CharField(max_length=255, blank=True, null=True)  # 4种取值：“8”、“3.5”、“10~15”、“应届生”
    work_year_norm = models.CharField(max_length=255, blank=True, null=True)  # 4种取值对应的规范化：“8”、“3.5”、“10”、“0”
    work_year_inf = models.CharField(max_length=255, blank=True, null=True)  # 2种取值：“8”、“3.5”
    work_start_time = models.DateField(blank=True, null=True)  # 比如：2019.10.01、2019.10
    work_position = models.CharField(max_length=255, blank=True, null=True)  # 比如：java开发、产品总监
    work_company = models.CharField(max_length=255, blank=True, null=True)  # 单位名称
    work_industry = models.CharField(max_length=255, blank=True, null=True)  # 行业名称
    work_status = models.CharField(max_length=255, blank=True, null=True)  # 用户填写的内容
    work_salary = models.CharField(
        max_length=255, blank=True, null=True
    )  # 取值类型：135000元/年”13500元/月”80000~120000元/年”8000~12000元/月”
    work_salary_min = models.IntegerField(blank=True, null=True)  # 比如：“8000”
    work_salary_max = models.IntegerField(blank=True, null=True)  # 比如：“12000”
    work_location = models.CharField(max_length=255, blank=True, null=True)  # 工作地点
    work_location_norm = models.CharField(max_length=255, blank=True, null=True)  # 同city_norm
    work_job_nature = models.CharField(max_length=255, blank=True, null=True)  # 全职、兼职、实习
    has_oversea_edu = models.BooleanField(default=False)  # 0:否，1:是；默认为无
    has_oversea_exp = models.BooleanField(default=False)  # 0:否，1:是；默认为无
    grad_time = models.DateField()  # 2019.10.01、2019.10
    college = models.CharField(max_length=255)  # 学校名称
    college_type = models.CharField(
        max_length=255, blank=True, null=True
    )  # 取值0~7：0:普通院校 1:985 2:211 3:港澳台院校4:海外院校5:中学6:职业教育7:培训机构
    college_rank = models.CharField(max_length=255, blank=True, null=True)  # 取值1~1000
    college_dept = models.CharField(max_length=255, blank=True, null=True)  # 院系名称
    major = models.CharField(max_length=255)  # 专业名称
    degree = models.CharField(max_length=255)  # 小学、初中、高中、中专、大专、本科、硕士研究生、博士研究生、博士后、mba
    recruit = models.CharField(max_length=255, blank=True, null=True)  # 统招、自考、在职、成教、函授等

    resume_type = models.CharField(max_length=250, blank=True, null=True)  # 取值0~4： 0:中文 1:英文 2:中英（前中后英） 3:英中（前英后中） 4:空
    resume_source = models.CharField(max_length=250, blank=True, null=True)  # 智联、智联卓聘、前程无忧、51精英、猎聘、boss直聘、拉勾
    resume_id = models.CharField(max_length=250, blank=True, null=True)  # 智联/51job等网站里的简历id
    resume_name = models.CharField(max_length=250, blank=True, null=True)  # 输入的简历文件名
    resume_parse_time = models.DateTimeField(auto_now_add=True)  # YYYY-MM-DD HH-MM-SS
    resume_update_time = models.DateTimeField(blank=True, null=True)  # 更新时间
    resume_integrity = models.IntegerField(blank=True, null=True)  # 取值0~100

    expect_job = models.CharField(max_length=250, blank=True, null=True)  # 职位名称
    expect_cpy = models.CharField(max_length=250, blank=True, null=True)  # 单位名称
    expect_salary = models.CharField(max_length=250, blank=True, null=True)  # 同work_salary
    expect_salary_min = models.IntegerField(blank=True, null=True)  # 同work_salary_min
    expect_salary_max = models.IntegerField(blank=True, null=True)  # 同work_salary_max
    expect_industry = models.CharField(max_length=250, blank=True, null=True)  # 行业名称
    expect_duty_time = models.DateField(blank=True, null=True)  # 到岗时间
    expect_jnature = models.CharField(max_length=250, blank=True, null=True)  # 期望工作性质
    expect_jstatus = models.CharField(max_length=250, blank=True, null=True)  # 当前离职/在职状态
    expect_jlocation = models.CharField(max_length=250, blank=True, null=True)  # 期望工作地址
    expect_jlocation_norm = models.CharField(max_length=250, blank=True, null=True)  # 同city_norm，多个地址以逗号分隔。

    self_evaluation= models.CharField(max_length=1024, blank=True, null=True)  # 自我评价



class ContactDetail(models.Model):
    resume = models.OneToOneField(Resume, related_name="contactdetail", on_delete=models.CASCADE)
    email = models.CharField(max_length=255)  # 联系邮箱
    phone = models.CharField(max_length=255)  # 手机/电话号码
    qq = models.CharField(max_length=255, blank=True, null=True)  # QQ号
    weixin = models.CharField(max_length=255, blank=True, null=True)  # 微信号
    postal_code = models.CharField(max_length=255, blank=True, null=True)  # 邮编
    city = models.CharField(max_length=255, blank=True, null=True)  # 城市名，比如“重庆”、“广东”、“华容县”
    city_norm = models.CharField(
        max_length=255, blank=True, null=True
    )  # 规范化的城市名，到“区县”一级： 中国-广东省 中国-湖南省-岳阳市 中国-湖南省-岳阳市-华容县 中国-吉林省-长春市-朝阳区
    living_address = models.CharField(max_length=255, blank=True, null=True)  # 用户填写的地址，比如“上海市虹口区广粤路xx弄x号xxx室”
    living_address_norm = models.CharField(max_length=255, blank=True, null=True)  # 规范化到“区县”一级，比如“中国-上海市-虹口区”


class Project(models.Model):
    resume = models.ForeignKey(Resume, related_name="projects", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)  # 日期，比如“2019.09.01”、“2019.09”、“2019”
    end_date = models.DateField(blank=True, null=True)  # 日期，比如“2019.09.01”、“2019.09”、“2019”、“至今”
    name = models.CharField(max_length=255)  # 项目名称
    cpy = models.CharField(max_length=255, blank=True, null=True)  # 公司名称
    position = models.CharField(max_length=255, blank=True, null=True)  # 职位名称
    content = models.CharField(max_length=255, blank=True, null=True)  # 项目内容
    resp = models.CharField(max_length=255, blank=True, null=True)  # 项目职责


class Skill(models.Model):
    resume = models.ForeignKey(Resume, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)  # 技能名词，比如“java开发”、“市场调研”等
    level = models.CharField(max_length=255, blank=True, null=True)  # 熟练程度
    time = models.CharField(max_length=255, blank=True, null=True)  # 时长
    train_loc = models.CharField(max_length=255, blank=True, null=True)  # 地点名称


class Training(models.Model):
    resume = models.ForeignKey(Resume, related_name="trainings", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)  # 日期，比如“2019.09.01”、“2019.09”、“2019”
    end_date = models.DateField(blank=True, null=True)  # 日期，比如“2019.09.01”、“2019.09”、“2019”、“至今”
    org = models.CharField(max_length=255, blank=True, null=True)  # 机构名称
    name = models.CharField(max_length=255, blank=True, null=True)  # 培训名称
    loc = models.CharField(max_length=255, blank=True, null=True)  # 地点名称
    cert = models.CharField(max_length=255, blank=True, null=True)  # 证书名称
    cont = models.CharField(max_length=1024, blank=True, null=True)  # 内容描述


class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name="educations", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)  # 日期，比如“2019.09.01”、“2019.09”、“2019”
    end_date = models.DateField(blank=True, null=True)  # 日期，比如“2019.09.01”、“2019.09”、“2019”、“至今”
    college = models.CharField(max_length=255, blank=True, null=True)  # 学校名称
    college_type = models.CharField(max_length=255, blank=True, null=True)  # 参考前面college_type字段
    college_rank = models.CharField(max_length=255, blank=True, null=True)  # 取值1~1000
    college_dept = models.CharField(max_length=255, blank=True, null=True)  # 院系名称
    major = models.CharField(max_length=255, blank=True, null=True)  # 专业名称
    recruit = models.CharField(max_length=255, blank=True, null=True)  # 参考前面recruit字段
    gpa = models.CharField(max_length=255, blank=True, null=True)  # gpa成绩
    degree = models.CharField(max_length=255, blank=True, null=True)  # 学历
    degree_norm = models.CharField(max_length=255, blank=True, null=True)  # 小学、初中、高中、中专、大专、本科、硕士研究生、博士研究生、博士后、mba


class Language(models.Model):
    resume = models.ForeignKey(Resume, related_name="languagedetails", on_delete=models.CASCADE)
    language_name = models.CharField(max_length=255, blank=True, null=True)  # 语言名称，比如“英语”、“俄语”等
    language_level = models.CharField(max_length=255, blank=True, null=True)  # 熟练程度
    language_read_write = models.CharField(max_length=255, blank=True, null=True)  # 比如“熟练”等
    language_listen_speak = models.CharField(max_length=255, blank=True, null=True)  # 比如“熟练”等


class Jobexp(models.Model):
    resume = models.ForeignKey(Resume, related_name="jobs", on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)  # 日期，比如“2019.09.01”、“2019.09”、“2019”
    end_date = models.DateField(blank=True, null=True)  # 日期，比如“2019.09.01”、“2019.09”、“2019”、“至今”
    cpy = models.CharField(max_length=255, blank=True, null=True)  # 公司名称
    cpy_nature = models.CharField(max_length=255, blank=True, null=True)  # 上市、民营、国企、央企、外企、外资、美资、港资等公司或企业
    cpy_size = models.CharField(max_length=255, blank=True, null=True)  # 公司规模
    cpy_desc = models.CharField(max_length=255, blank=True, null=True)  # 公司描述
    industry = models.CharField(max_length=255, blank=True, null=True)  # 行业名称
    position = models.CharField(max_length=255, blank=True, null=True)  # 职位名称
    dept = models.CharField(max_length=255, blank=True, null=True)  # 部门名称
    nature = models.CharField(max_length=255, blank=True, null=True)  # 全职、兼职、实习
    salary = models.CharField(max_length=255, blank=True, null=True)  # 工作薪资
    staff = models.CharField(max_length=255, blank=True, null=True)  # 下属人数
    report_to = models.CharField(max_length=255, blank=True, null=True)  # 汇报对象
    location = models.CharField(max_length=255, blank=True, null=True)  # 工作地点
    why_leave = models.CharField(max_length=255, blank=True, null=True)  # 离职原因
    duaraton = models.CharField(max_length=255, blank=True, null=True)  # 持续时间 比如“1年3个月”、“3年”、“6个月”
    capacity = models.CharField(max_length=255, blank=True, null=True)  # 工作能力
    content = models.CharField(max_length=1024, blank=True, null=True)  # 工作内容
