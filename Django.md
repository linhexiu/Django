### [Django教程]()

#### 1.Django简介

##### 1.1Django版本

不同的Django版本对应不同的Python版本，安装时要注意避免不可兼容的问题，比如：2.1，2.2（Django）—3.5，3.6，3.7(Python)

##### 1.2Django基本介绍

Django本身是基于MVC模型设计模式，它能够支持的架构模式还有MTV模型。

###### 1.2.1MVC模型

该模型将软件系统分为三个基本部分：模型（Model）、视图（View）、控制器（Controller）

模型（M）- 编写程序应有的功能，负责业务对象与数据库的映射（ORM）。

视图（V）- 图形界面，负责与用户的交互。

控制器（C）- 负责转发请求，对请求进行处理。

用户操作流程图：

![image-20211203125004940](Django.assets/image-20211203125004940.png)

###### 1.2.1MTV模型

模型（M）- 编写程序应有的功能，负责业务对象与数据库的映射（ORM）。

模板（Template）:负责如何把页面（html）展示给用户。

视图（V）-负责业务逻辑，并在适当的时候调用Model和Template。

除了以上三层之外，还需要一个URL分发器，作用是将一个个URL的页面分发器发送给不同的View，View再调用相应的model和Template。

简易图：

![image-20211203125844017](Django.assets/image-20211203125844017.png)

用户操作流程图：

![image-20211203131626839](Django.assets/image-20211203131626839.png)

#### 2.Django安装

- 在window中先需要安装python环境，之后安装Django。
- 在pycharm中安装Django，可以在setting中进行添加。

#### 3.创建第一个项目

使用django-admin，在使用之前需要先在系统环境变量中添加python和Django环境变量。

```python
#创建项目
django-admin startproject HelloWorld
进行项目文件夹，开启服务
python3 manage.py runserver 0.0.0.0:8000
之后在浏览器中输入本机地址：127.0.0.1:8000
!!!在这可能会出现的问题：cmd 运行 python3 manage.py runserver 0.0.0.0:8000 无反应
    检查py -m django --version 版本
    若django大于3.0版本
    则开启服务要执行 py manage.py runserver
```

在urls文件中path的用法：

```
path(route, view, kwargs=None, name=None)
route: 表示URL规则， 与之匹配的URL会执行对应的第二个参数
view：用于执行与正则表达式匹配的URL请求
kwargs： 视图使用的字典类型参数
name： 用来反向获取URL
```

![image-20211206085931418](Django.assets/image-20211206085931418.png)

#### 4.Django模板

在第3节中项目的views.py（视图）中将数据和视图混合在一起，不符合MVC思想，因此引出”模板“，模板是一个文本，用于分离文档的表现形式和内容。

##### 4.1 模板应用的基本流程

- 建立模板文件，放在templates目录中， templates目录与manage.py同级

```html
<h1>{{ hello }}</h1>
```

- 向Django说明模板文件的路径，在配置文件（setting.py）中设置

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],#该处修改位置,templates是模板文件所在的文件夹
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 修改视图（views.py），向模板提交数据：runoob.html中的hello对应了context键值的hello

```python
from django.shortcuts import render

def runoob(request):
	context={}
	context['hello']='Hello World!'
	return render(request,'runoob.html',context)
```

- 修改urls.p文件

```python
from django.urls import path
from .  import views

urlpatterns = [
    path('runoob/', views.runoob),
]
```

- 运行

##### 4.2 Django模板标签

###### 4.2.1 变量

```python
views:{"HTML变量名":"views变量名"}
HTML:{{变量名}}
```

实例：

views.py

```python
from django.shortcuts import render

def runoob(request):
	view_name="菜鸟教程"
	return render(request,"runoob.html",{"name":view_name})
```

templates中runoob.html

```html
<h1>{{ name }}</h1>
```

###### 4.2.2 列表

用 **.** 索引下标取出对应的元素

views.py

```python
from django.shortcuts import render

def runoob(request):
	view_list=["菜鸟教程1","菜鸟教程2"]
	return render(request,"runoob.html",{"name":view_list})
```

templates中runoob.html

```html
<h1>{{ name.0 }}</h1>
<h1>{{ name.1 }}</h1>
```

###### 4.2.3 字典

用 **.键** 取出对应的值

views.py

```python
from django.shortcuts import render

def runoob(request):
	view_dict={"name":"菜鸟教程"}
	return render(request,"runoob.html",{"view_dict":view_dict})
```

templates中runoob.html

```html
<h1>{{ view_dict.name }}</h1>
```

###### 4.2.4 过滤器

过滤器是指在变量显示给模板前，对变量先进行操作，比如可以先进行字符串大小写的转换、时间格式的变换……

文档大写转换为小写（lower），views.py

```python
from django.shortcuts import render

def runoob(request):
	name="Lin Hexiu"
	return render(request,"runoob.html",{"name":name})
```

templates中runoob.html

```html
<h1>{{ name }}</h1>
<h1>{{ name|lower }}</h1>
```

说明：

- 过滤管道可以进行“套接”，比如 {{ name|first|upper }} 将第一个元素变成大写并输出
- 其他过滤器：
  - truncatewords:"参数"：显示变量前“参数”个字符
  - addslashes:添加反斜杠到任何反斜杠、单引号、双引号前面
  - date:按指定的格式字符串参数格式化 date 或者 datetime 对象
  - length:返回字符串的长度
  - default:为变量提供一个默认值
  - filesizeformat:以更易读的方式显示文件的大小
  - truncatechars:“参数”:截取参数个字符
  - safe:将字符标记为安全，不需要转义，比如说链接，实例如下

views.py

```python
from django.shortcuts import render

def runoob(request):
	views_str="<a href='https://www.baidu.com'>点击跳转</a>"
	return render(request,"runoob.html",{"views_str":views_str})
```

html

```html
<h1>{{ views_str|safe }}</h1>
```

###### 4.2.5 if/else 标签

views.py

```python
from django.shortcuts import render

def runoob(request):
	views_num=57
	return render(request,"runoob.html",{"num":views_num})
```

templates中runoob.html

```html
{%if num > 90 and num <= 100 %}
优秀
{%elif num > 60 and num <= 90 %}
合格
{% else %}
不合格
{% endif %}
```

###### 4.2.6 for 标签

views.py

```python
from django.shortcuts import render

def runoob(request):
	views_list=["test1","test2","test3"]
	return render(request,"runoob.html",{"views_list":views_list})
```

templates中runoob.html

```html
{% for i in views_list %}
{{ i }}
{% endfor %}
```

###### 4.2.7 ifequal/ifnotequal 标签

比较两个值，当他们相等/不相等时，值显示{%ifelqual%}{%endifequal%}中间

###### 4.2.8 注释标签

```html
{#这是一个注释标签#}
```

###### 4.2.8 include标签

该标签允许在模板中包含其它模板的内容

```html
{%  include "nav.html"%}
```

###### 4.2.9 csrf_token

用于form表单中，作用是跨站请求伪造保护

###### 4.2.10 自定义标签和过滤器

- 在应用目录下创建templatetags目录，与template同级

- 在templatetags目录下创建my_tags.py

- 配置setting.py文件

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
              "libraries":{
                  'my_tags':'templatetags.my_tags'#添加my_tags
              }
          },
      },
  ]
  ```

- my_tags.py文件代码如下

  ```python
  from django import template
  
  register=template.Library() #register的名字是固定的，不可改变的
  #利用装饰器@register.filter自定义过滤器，参数只能有两个
  @register.filter
  def my_filter(v1,v2):
  	return v1*v2
  #用@register.simple_tag自定义标签
  @register.simple_tag
  def my_tag1(v1,v2,v3):
  	return v1*v2*v3
  ```

- 在HTML中使用过滤器和标签

  ```html
  {% load my_tags %} #导入py文件
  {{ 11|my_filter:22 }} #使用过滤器
  {% my_tag1 11 22 33 %} #使用标签
  ```

###### 4.2.11 配置静态文件

在templates同级目录下，建立statics目录，用来存放静态资源

在setting.py中，在最下方加上这些语句

```python
STATIC_URL='/static/'#别名
STATICFILES_DIRS-{
    os.path.join(BASE_DIR, "statics")
}
```

###### 4.2.12 模板继承

可以通过继承的方式来实现复用，减少冗余

#### 5.Django模型

##### 5.1  ORM简介

- Django模型自带ORM，对象关系映射（Object Relational Mapping）用于实现面向对象编程语言里不同类型的数据之间的转换
- ORM在业务逻辑层和数据层之间充当了桥梁作用
- ORM通过使用描述对象和数据库之间的映射的元数据，将程序中的对象自动持久化到数据库中。

##### 5.2 ORM解析过程

- ORM将python代码转换为SQL语句
- SQLy语句通过pymysql传送到数据库服务端
- 在数据库中执行SQL语句并将结果返回

ORM对应关系表如下图：

![image-20211209181920048](Django.assets/image-20211209181920048.png)

##### 5.3 Django操作数Mysql

###### 5.3.1 数据库配置

如果没安装 mysql 驱动，执行以下命令进行驱动安装

```python
pip install pymysql
```

Django不能执行创建数据库操作，只能操作到数据表，因此建库需要在到mysql的可视化软件中进行操作，也可以cmd进行建库

进入到安装mysql的bin目录下

```python
mysql -uroot -p
输入密码，进入mysql界面
create database runoob default charset utf8;#这里末尾的 ; 不能漏
```

建库完，到setting下进行配置

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3', 
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql', #数据库引擎
        'NAME': 'runoob', #数据库名称
        'HOST':'127.0.0.1', #数据库地址
        'PORT':3306, #端口
        'USER':'root', #数据库用户名
        'PASSWORD':'1234', #数据库密码
    } 
}
```

之后到setting同一级目录下的 **__init__.py** 中引入模块进行配置

```python
import pymysql
pymysql.install_as_MySQLdb()
```

###### 5.3.2 定义模型

Django规定，如果要用模型，则必须要建一个app，接下来建立一个名为TestModel的app

进入项目一级目录，即manage.py所在的目录

```
python manage.py startapp TestModel
```

生成app目录之后，里面由很多py文件，其中由models.py

```python
from django.db import models

# Create your models here.
class Test(models.Model):
	name=models.CharField(max_length=20)#类里面的字段代表数据表中的字段（name）,数据类型CharField（相当于varchar）,max_length限定长度
```

修改setting.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestModel',#在这添加app目录名
]
```

cmd到项目manage.py目录,，进行建表

```
python manage.py makemigrations TestModel #让Django知道我们的模型是由变化的
python manage.py migrate TestModel #创建表结构
```

###### 5.3.3 数据库操作

- 添加操作

在Test容器下，建立testdb.py

```python
from django.http import HttpResponse
from TestModel.models import Test

#数据库操作
def testdb(request):
	test1=Test(name='runoob')
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")
```

为了说明它添加成功，在urls.py中设置

```python
from django.urls import path
from . import views,testdb

urlpatterns = [
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
]
```

运行 **127.0.0.1:8000/testdb/** 出来 **数据添加成功！**

- 获取数据

```python
#获取数据
def testdb(request):
	#初始化
	response=""
	response1=""

	list=Test.objects.all()#相当于SQL中SELECT * FROM
	response2=Test.objects.filter(id=1)#相当于SQL中WHERE
	response3=Test.objects.get(id=1)#获取单个对象
	Test.objects.order_by('name')[0:2]#限制返回的数据，相当于SQL中的OFFSET 0 LIMIT 2
	Test.objects.order_by("id")#数据排序
	Test.objects.filter(name='runoob').order_by("id")#方法可以连锁使用

	#输出数据
	for var in list:
		response1+=var.name+" "
	response=response1
	return HttpResponse("<p>"+response+"</p>")
```

- 更新数据

```python
#更新数据
def testdb(request):
	test1=Test.objects.get(id=1)
	test1.name='Google'
	test1.save()

	#Test.objects.filter(id=1).update(name='Google')
	#修改所有的列
	#Test.objects.all().update(name='Google')

	return HttpResponse("<p>修改成功！</p>")
```

- 删除数据

```python
#删除数据
def testdb(request):
	test1=Test.objects.get(id=1)
	test1.delete()

	#Test.objects.filter(id=1).delete()
	#删除所有数据
	#Test.onjects.all().delete()
	return HttpResponse("<p>删除成功！</p>")
```

#### 6.Django表单

##### 6.1 HTTP请求

###### 6.1.1 GET方法

在Test容器中建立一个search.py文件，用于接收用户请求

```python
from django.http import HttpResponse
from django.shortcuts import render

#表单
def search_form(request):
	return render(request,'search_form.html')

#接受请求数据
def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET and request.GET['q']:
		message='你搜索的内容为：'+request.GET['q']
	else:
		message='你提交了空表单'
	return HttpResponse(message)

```

在search.py中有search_form.html，因此在模板目录下要建立search_form.html

```html
<form action="/search/" method="get">
	<input type="text" name="q">
	<input type="submit" value="搜索">
</form>
```

urls.py中路径修改一下

```python
from django.conf.urls import url
from . import views,testdb,search

urlpatterns = [
    url(r'testdb/$', testdb.testdb),
    url(r'search_form/$', search.search_form),
    url(r'search/$', search.search),
]
```

###### 6.1.2 POST方法

在模板中建立post.html

```html
<form action="/search-post/" method="post">
	{% csrf_token %}
	<input type="text" name="q">
	<input type="submit" value="搜索">
</form>

<p>{{ rlt }}</p>
```

在Test容器中建立一个search2.py文件，用于接收用户请求

```python
from django.shortcuts import render
from django.views.decorators import csrf

def search_post(request):
	ctx={}
	if request.POST:
		ctx['rlt']=request.POST['q']
	return render(request,"post.html",ctx)
```

urls.py中路径修改一下

```python
from django.conf.urls import url
from . import views,testdb,search,search2

urlpatterns = [
    url(r'^testdb/$', testdb.testdb),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),
]
```

##### 6.2 Request对象

每个视图函数的第一个参数是一个HttpRequest对象

#### 7.Django视图

##### 7.1 视图层

- 每一个视图都负责一个HttpRequest对象，对象中包含生成的响应
- 视图层中有两个重要的对象，请求对象（request）和相应对象（HttpResponse）

##### 7.2 请求对象

HttpRequest对象（简称request对象）

###### 7.2.1 GET

```python
包含HTTP GET 的所有参数
取值格式：对象.方法
实例：
def runoob(request):
	name=request.GET.get("name")
	return HttpResponse('姓名：{}'.format(name))
```

###### 7.2.2 POST

```python
包含HTTP POST 的所有参数
常用于表单，form表单里的标签name属性对应参数的键，value属性对应参数的值
取值格式：对象.方法
实例：
def runoob(request):
	name=request.POST.get("name")
	return HttpResponse('姓名：{}'.format(name))
```

###### 7.2.3 body

```python
数据类型是二进制字节流，处理二进制图片、Json等非常有用
实例：
def runoob(request):
	name=request.body
	print(name)
	return HttpResponse("菜鸟教程")
```

###### 7.2.4 path

```python
获取URL的路径，数据类型是字符串
实例：
def runoob(request):
	name=request.path
	print(name)#输出/runoob/
	return HttpResponse("菜鸟教程")
```

###### 7.2.5 method

```python
获取当前请求的方式，数据类型是字字符串，结果为大写
实例：
def runoob(request):
	name=request.method
	print(name)#输出GET/POST
	return HttpResponse("菜鸟教程")
```

##### 7.3 响应对象

响应对象主要有三种形式：HttpResponse()、render()、redirect()

###### 7.3.1 HttpResponse()

返回文本，参数为字符串，字符串写文本内容。如果参数为字符串里含有html标签，也可以进行渲染

###### 7.3.2 render()

返回文本，第一个参数为request，第二个参数为字符串，第三个参数为字典（是可选参数，键为页面参数，值为views参数名）

```python
def runoob(request):
	name="菜鸟教程"
	return render(request,"runoob.html",{"name":name})
```

###### 7.3.3 redirect()

重定向，跳转新页面。

```python
def runoob(request):
	return redirect("/index/")
```

