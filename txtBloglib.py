import json,re,time,os
from flask import escape, url_for
import mistune
# version 0.0.7-8

#文本文件阅读器，input filepath, return string from the file.
#v0.3 <h4>下添加换行，防止遮挡;
#v0.4 对尖括号转码
#v0.5 添加纸质背景
def txtReader(fpath):
	fr=open(fpath, 'r', encoding="utf8")
	tmp=''
	for lineR in fr.readlines():
		line=lineR.strip()
		#if line.match("")
		line=re.sub("<","&lt;",line);
		line=re.sub(">","&gt;",line);
		#add text
		if re.match("\={40,}",line):
			tmp+="<hr class=top><h4>\n"
		elif re.match("\-{40,}",line):
			tmp+="</h4><hr class=under>\n"
		else:
			tmp+=line+"\n";
	#关闭文件
	fr.close()
	js='<script type="text/javascript" src="static/js/txt.js"></script>\n\n'
	return js+"<div class='content'><pre class=ubuntu1>" + tmp + "</pre></div>\n";

#html读取器
#v0.1
def htmlReader(fpath):
	fr=open(fpath, 'r', encoding="utf8")
	tmp=fr.read();
	fr.close()
	return tmp;
#

#markdown读取器
#v0.1
#v0.2 增加top目录
#v0.3 代码高亮
#v0.4 左下角添加目录
def markdownReader(fpath):
	# read markdown
	fr=open(fpath, 'r', encoding="utf8")
	text=fr.read()
	fr.close()
	# get html from markdown
	tmp=mistune.markdown(text, escape=False, hard_wrap=True) #'I am using **mistune markdown parser**'
	tmp="<div class=markdown>\n"+tmp+"</div>\n"
	#tmp="<div class=content>\n"+tmp+"</div>\n"
	
	# left bottom corner contents 
	cornerContents="""
<div id="common_box">
 <div id="cli_title"> Contents <b id="cli_on">+</b></div>
 <div id="f_content" class=content></div>
</div>
<script type="text/javascript" src="/static/js/startMove.js"></script>\n
"""
	tmp+=cornerContents;#其他js在markdown.js中
	
	# add markdown style sheet and top contents js, left bottom corner contents.
	css='<link rel="stylesheet" type="text/css" href="/static/css/MarkDown3.css" media="all">\n'
	js='<script type="text/javascript" src="static/js/markdown.js"></script>\n\n'
	tmp=css+js+tmp;
	
	# high light code
	css2='<link rel="stylesheet" href="/static/css/highlight-routeros.css">\n'
	js2='<script src="/static/js/highlight.pack.js"></script>\n\n'
	tmp=tmp + css2+js2   + '<script>hljs.initHighlightingOnLoad();</script>';
	
	return tmp;



#input k and id, return url_left and content, filepath
#v0.3
def getData(k,id):
	#1.解析id为2个数字
	arr=re.split("_", id)
	n0=int(arr[0])
	n1=int(arr[1])

	#2.解析json文件获取左侧目录，和文件名字
	load_f=open("data/"+k+".json",'r',encoding="utf8")
	#读取json
	menus = json.load(load_f)

	#凑出来文件路径
	menuCur =  menus[n0]["data"][n1]
	filepath="data/"+k+"/"+menuCur[1]+"."+menuCur[2] #路径
	suffix=menuCur[2].lower() #后缀

	#拼凑出超链接
	url_left=""
	for i in range(len(menus)):
		#print("="*10,menus[i]["title"]);
		url_left+="<li><h5 class=title>"+str(i)+" "+menus[i]["title"]+"</h5>\n<ul class=submenu>\n";

		arr2=menus[i]["data"];
		for j in range(len(arr2)):
			#print("title=",arr2[j][0], str(i)+"_"+str(j) )
			cur=""
			if i==n0 and j==n1:
				cur=" class=cur"
			#
			id=str(i)+"_"+str(j)
			item_url=url_for('hello', k=k, id=id) #第一个参数是函数名，不是路由
			
			url_left+="<li"+cur+"><a href=" + item_url +">"+id+" "+arr2[j][0]+"</a></li>\n"
		url_left+="</ul>\n</li>\n"
	#关闭文件
	load_f.close();
	
	#上次修改时间
	lastModified = "2017-10-19 7:0:0"


	#根据文件类型，读取文件
	content='<div class="alert">该文章暂时未公开，请稍后再来...</div>';
	if os.path.exists(filepath):
		# modified date and time;
		#modified=time.localtime(os.path.getctime(filepath))
		modified = os.path.getmtime(filepath)
		year,month,day,hour,minute,second=time.localtime(modified)[:-3]
		lastModified=str(year)+"-"+str(month)+"-"+str(day) +" "+str(hour)+":"+str(minute)+":"+str(second)
		# content
		if suffix=="html":
			content=htmlReader(filepath)
		elif suffix=="markdown" or suffix=='md':
			content=markdownReader(filepath)
		else: #txt
			content=txtReader(filepath)

	return (url_left, content,filepath.replace("data/",""), lastModified,suffix)
	#          0        1       2                              3           4


#顶部菜单生成
#v0.2
def getTopMenu(k):
	load_f=open("data/topMenu.json",'r',encoding="utf8")
	#读取json
	menus = json.load(load_f)

	tmp=""
	for i in range(len(menus)):
		item_url=url_for('hello', k=menus[i][0], id="0_0")
		cur=""
		if menus[i][0]==k:
			cur=" current"
		tmp+=" <a class='topmenu"+cur+"' href=" + item_url +" title="+menus[i][1]+">"+menus[i][0]+"</a> "
	return tmp;
#



#底部菜单生成
#v0.1
# 根据友情链接数组，输出拼接好的字符串。【对外】
# 1.输入一级数组： ['http://jsbin.com/','jsbin','练习前端的好工具！']
# 2.或二级数组：
#	[
#		['http://jsbin.com/','jsbin','练习前端的好工具！'],
#		['http://jquery.cuishifeng.cn/','jQuery手册']
#	];
# 3.返回链接字符串。
def get_links(arr):
	def get_link(ar):
		title=""
		if len(ar)>2:
			title="title="+ar[2]
		return "<a target=_blank href="+ar[0]+" "+title+">"+ar[1]+"</a> | \n"
	#
	if isinstance(arr[0],str):
		return get_link(arr);
	html=""
	for i in range(len(arr)):
		html+=get_link(arr[i])
	return html;
#