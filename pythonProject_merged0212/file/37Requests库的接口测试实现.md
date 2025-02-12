# Requests库的接口测试实现

## Requests库环境搭建

requests库，继承于request库。目前主流的HTTP网络协议的接口测试，基本都是基于requests库来实现的。整体而言，接口测试的实现，其实就是基于requests实现对请求的模拟发送以及对响应结果的接收与解析。即可完成。

requests属于第三方库。所以需要提前安装

安装指令： pip install requests

类似于java中httpclient库。

## 请求的模拟

所有的接口都是基于请求的下发才会产生运算和响应结果的生成。所以接口测试的核心其实就是模拟请求的下发。

接口测试其实就是三个步骤：

1. 准备测试数据
2. 模拟请求下发
3. 获取响应并解析断言。

json是一种数据格式。而非数据类型。所有的key和value都是基于双引号括起来的string数据内容。

## 响应的获取与解析

请参考源码

## 课后作业

部署requests环境，基于fecmall来熟悉requests库的基本应用