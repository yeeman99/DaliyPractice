# Fixture应用_下

请参考源码查看所有的内容

## Fixture实现teardown

## conftest.py文件实现

```
'''
    conftest.py文件主要有两个作用：
        1. 用于管理hook函数。实现pytest的功能增强以及部分内容的修改。
        2. 用于管理整个测试过程中的所有Fixture
            可以让不同的py文件实现对所有Fixture的正常调用。不用担心Fixture只对当前文件有效的作用域问题
            conftest.py的有效范围默认是当前路径及子路径的全覆盖。推荐放在测试用例的路径下。
            conftest.py用于管理所有的Fixture，可以将整个系统的自动化测试的所有Fixture进行统一的管理，全部放在conftest之中
            session级别的Fixture必须要放在conftest之中。
            所有的autouse的fixture都需要在conftest中进行定义。
'''
```

## pytest.ini文件实现

pytest内嵌的logging库，unittest还是用之前的那套log方法

## 课后作业

将之前的fecmall用例内容，提取Fixture到conftest之中。定义pytest.ini，配置好相关内容。重新定义你的测试用例。
