################################
# project name: txtBlog.py is the python3 version of txtBlog 
# desc: [知识管理]A simple yet powerful blog system for reading and organizing txt files.
# desc2: Pyhton3编写的、基于文件的文本笔记管理系统，简捷高效，可用于管理知识。
# version: 0.0.9
# github: https://github.com/DawnEve/txtBlog.py
# appearence: https://github.com/DawnEve/txtBlog
#
# local test url: http://blog2.163.com:8000/
# local dir:G:\xampp\htdocs\163
################################



################################
整体构架:
# 和记忆作斗争，是“坐家”们毕生的事业，本项目是一个简洁的文本笔记系统，就是为了管理知识，支持插入少量图片。
# 使用Python3的flask包作为web框架，尽量简化。https://flask.palletsprojects.com/en/1.1.x/
# 顶部关键词，左侧文件名，都使用json格式的配置文件。
# 支持html/txt/markdown格式的笔记，未来会支持 ReStructuredText等;
# 为了应付最危险的情况：python部件不再支持(5-10年内不会发生)，博客系统失灵，建议文件命名时要言简意赅、见名知意！保证human也能读懂。
#





################################
What's new?
v0.0.9-1 为markdown代码块添加行号
v0.0.9-6 data/search.sh 单行脚本搜索功能









################################
安装方法：
1. 环境： 
OS: win10和linux都可以，但是需要有可用的端口号，本项目默认使用8000端口。

安装python3，查看版本号
$ python -V  
## Python 3.6.4

使用pip安装 flask(web服务器): 
$ pip install flask

使用pip安装 mistune(markdown解析器): 
$ pip install mistune



2.下载该项目
通过
$ git clone https://github.com/DawnEve/txtBlog.py.git
或者下载压缩包并解压
$ wget https://github.com/DawnEve/txtBlog.py/archive/master.zip

可以放到硬盘的任意位置，但是路径中不要出现中文字符。



3.修改该项目的IP和端口
index.py的最后一行为host和端口号。 
如果不确定，不用修改，使用默认值即可。



4.运行该txt博客
$ cd txtBlog.py/
进入项目文件夹，运行：
$ python index.py

按照命令行提示的网址： Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
打开chrome浏览器，输入 http://127.0.0.1:8000/ 并回车即可访问。

如果报错，请阅读出错提示，百度解决，或者留言 issues 提问。










################################
新增、删除、修改笔记内容：
注意: 所有路径和文件名，尽量不要出现空格和汉字，避免报错！建议使用下划线、连字符、或驼峰格式等。
不推荐: Python 001.txt, Python基础.txt,
推荐: Python_001.txt, Python-001.txt, PythonBasic.txt, 


1. 文件结构
所有可自由修改的部分，主要集中在data/文件夹中。
/data/
 |- topMenu.json
 |- R.json
 |- Python.json
 |- R/
 |- Python/
    |- images/
    |- Python001.html
    |- Python-basic.txt
 |- Linux/

(1)json格式的顶部目录 topMenu.json，一行一个顶部链接；
第一个字符直接显示出来，第二个字符鼠标悬停时显示出来。
[
	["Linux", "basic 操作"],
	["Python", "爬虫"],
	["R", "画图效果"]
]
第一个字符要和/data/下的文件夹同名。

Pyhton对json要求很严格： 
	- 最后一个元素后不能出现逗号！否则报错。
	- 键值对中，键要用双引号，值如果是字符串也要用双引号。
	- json中不能出现注释！相比js中的json，太可悲了。





(2)json格式的左侧目录 Python.json为例
[
	{
		"title":"前沿与资料",
		"data":
		[
			["项目描述", "Python001", "html"],
			["常用资源", "Python002", "md"],
			["入门教程", "Python003", "txt"]
		]
	}
]
该文件的文件名，要和/data/下的文件夹同名，并在topMenu.json中出现
是一个数组[]，数组中是对象{}，对象的title是显示到左侧的仅有分类作用的一级标题，对象的data属性是二级标题，可以点击并跳转。
data属性也是一个数组，每个元素是一个3元素数组，第一个是页面显示用，第二项是文件名(不带路径，不带后缀名)，第三项是文件后缀名(不带点)





(3)文件夹内是文本文件: .txt/.html/.markdown/.md
未来会考虑支持 rst //todo


1)txt格式文档，符合前一行有40个=、后一行有40个-的行，会被解析成标题，并自动生成顶部目录。
如
========================================
web based tutorials
----------------------------------------


2)html的编写应该写到<div class=content></div>中，中间支持<h2>,<h3>,<p>等标签及预定义格式；
更多html标签的含义和用法请参考网络资源，如 https://www.runoob.com/html/html-tutorial.html

图片建议也放到同关键词的images文件夹下，使用完整路径访问，如
<img class="banner" src='/data/Python/images/SciPy_ecosystem.png'>
注意目录最前的 / 符号不能省略！

该项目叫做txtBlog，对图片支持程度较低，尽量少用图片！尽量用占用空间较小的瘦身图片！
否则可能会影响项目的迁移、存储、显示！




3)支持使用GitHub Flavored Markdown 
- 纯python版的markdown解析器 mistune;
- css使用github的主要样式，颜色参考 https://segmentfault.com/a/1190000018084098
- 支持代码高亮(依赖 highlight.js);
- md中的代码行号由自定义js实现 模仿 模仿 https://blog.csdn.net/hustqb/article/details/80628721
- 支持LaTex(依赖 MathJax.js, 在线cdn，加载很慢) ，默认不开启，开关在 /config/conf.ini；






2. 更新时要注意文本文件和json目录的同步！防止互相被孤立！
也就是说改文件名时，要同时在对应的json目录中修改，否则系统web页看不到该文件;
删除文件时，要在对应的json里删除该行;
{现在只能全手动同步，或者看到报错再更新至同步。}







3. 底部友情链接的更新
链接数据是json格式的，定义在文件 /footer_urls.py 中。
链接html生成函数 get_links() 在 /txtBloglib.py 中定义，并在 /index.py 中执行。





4. 如何制作皮肤？

目前 
- txt 页面默认是极简风格。
- txt和markdown都是自动生成顶部页内目录。
- markdown页左下角有可伸缩的目录，并响应鼠标滚轮高亮当前目录；


(1)css文件在 static/css/下，可尝试修改该文件。
未来可能会支持更多可配置的外观。//todo
/static/css/
|-- base.css 是基础样式，不建议改动;
|-- main.css 是html和txt页面的样式，可以尝试更改为自己喜欢的颜色;
|-- MarkDown3.css 是markdown的样式表;
|-- txt.css 是txt文件的样式表，支持在/config/conf.ini中指定皮肤样式


(2)自定义txt皮肤，就是在/static/css/txt.css末尾添加css代码，格式模仿前几个即可。








5.【还没有实现】 如何全站静态化？//todo 
$ pip install Frozen-Flask
$ python index.py build

url已经静态化风格了。






todo:
1. 自由切换 data 文件夹的位置，这样一个博客笔记系统，就可以对应多个内容部分了。
data dir -> shelf; 书架子
top menu -> book; 书
left mune -> chapter; 章节
top contents -> headers; 小标题



2. 全站静态化，这样就可以放到github上；






################################
如何升级
1. 从github使用 git clone 下载新的框架;
2. 把旧项目中自己的data/文件夹，复制粘贴，覆盖新版本中的data/文件夹；
3. 其他小的数据文件包括：
	- 底部友情链接: /footer_urls.py
	- English 频道的名人名言: 
	- 自定义风格: /config/conf.ini


彩蛋：
English项目下添加菜单：底部名人名言插件，刷新随机展示一条，会周期性滚动。
	- 滚动显示的内容在 /static/js/motto.js
