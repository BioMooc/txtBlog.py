################################
# project name: txtBlog.py is the python3 version of txtBlog
# desc: [知识管理]A simple yet powerful blog system for reading and organizing txt files.
# version: 0.0.5

# local url:http://blog2.163.com/
# dir:G:\xampp\htdocs\163
################################


################################
整体构架:
# 使用flask框架，尽量简化。https://flask.palletsprojects.com/en/1.1.x/
# 顶部关键词，左侧文件名。使用json做配置文件。
# 预计支持html/txt格式的文档。尽量留下扩展。


################################
安装方法：
1.安装python3，使用pip安装 flask
pip install flask

2.修改该项目的IP和端口
把index.py的最后一行改成合适的值，如果不确定，就是用默认值即可。

3.运行该txt博客项目
进入项目文件夹，运行：
python index.py

Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
按照命令行提示的网址，到浏览器输入 http://127.0.0.1:8000/ 即可访问。



################################
增删修改博客内容：
注意: 所有路径和文件夹，尽量不要出现空格和汉字，避免出错！连接使用下划线、连字符、或驼峰格式等。
不推荐: Python 001.txt, Python基础.txt,
推荐: Python_001.txt, Python-001.txt, PythonBasic.txt, 


1. 所有可自由修改的部分，集中在data/文件夹中。
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


(2)json格式的左侧目录 Python.json为例
[
	{
		"title":"前沿与资料",
		"data":
		[
			["项目描述", "Python001", "html"]
		]
	}
]
该文件的文件名，要和/data/下的文件夹同名，并在topMenu.json中出现


(3)文件夹内是文本文件: .txt、.html，将来会考虑支持 .markdown(.mk)
1)txt格式文档，符合前一行有40个=、后一行有40个-的行，会被解析成标题，并自动生成目录。
如
========================================
web based tutorials
----------------------------------------

2)html的编写应该写到
<div class=content></div>中，中间支持<h2>,<h3>,<p>等标签及预定义格式
图片建议也放到同关键词的images文件夹下，使用完整路径访问，如 
<img class="banner" src='data/Python/images/SciPy_ecosystem.png'>

这各项目叫做txtBlog，对图片支持程度较低，尽量少用图片！


2. 更新时要注意文件和目录的同步！防止互相被孤立！
{现在只能手动同步，或者看到报错在同步更新。}



################################
如何升级
只需要把自己的data/文件夹放到并覆盖新版本中的data/文件夹即可。

