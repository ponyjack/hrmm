# Copyright 2015-2020 ResumeSDK inc. All rights reserved. 

# 接口试用介绍

1、目标

通过实际数据测验ResumeSDK解析的接口及效果。


2、方法

2.1 选择熟悉的示例代码：
  1) SaaS服务调用示例/test_parse_api.py：python代码；
  2）SaaS服务调用示例/TestParseApi.java：java代码；
  3）SaaS服务调用示例/TestParserApi.cs：C#代码；
  4）SaaS服务调用示例/TestParserApi.php：php代码；
  5）SaaS服务调用示例/TestParserApi.go：golang代码；

2.2 根据代码提示，使用《测试账号.txt》里提供的uid和pwd替换代码里对应变量，然后运行代码；

2.3 返回结果字段参考《ResumeSDK简历解析接口文档.pdf》的介绍；


3、其他补充

3.1 测试接口使用我们的线上SaaS服务，如购买的是独立部署服务，则到时只需简单替换相关参数即可，其他一致；

3.2 测试用量默认为1000次调用，如需更多，请向我司申请，最多提供2000次调用量。剩余用量可通过以下两种方式查询：
  1）api接口的返回字段usage_remaining；
  2）通过网页端访问http://www.resumesdk.com/api/query_user查询；

3.3 如需感知实际的解析效果，可以访问我们的demo：
  1）简历解析：www.resumesdk.com/demo-parser.html
  2）智能评估：www.resumesdk.com/demo-evaluator.html
  3）人岗匹配：www.resumesdk.com/demo-matcher.html

3.4 更多文档可以访问：
  1）开发文档：http://www.resumesdk.com/docs/rs-parser.html
  2）版本升级记录：http://www.resumesdk.com/docs/rs-changelog.html
