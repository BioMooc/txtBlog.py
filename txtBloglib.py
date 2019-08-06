import json,re
from flask import escape, url_for


#文本文件阅读器，input filepath, return string from the file.
def txtReader(fpath):
	print(fpath)
	fr=open(fpath, 'r', encoding="utf8")
	tmp=""
	for lineR in fr.readlines():
		line=lineR.strip()
		tmp+=line+"<br>";
		print(tmp)
	#关闭文件
	fr.close()
	return tmp;
#
htmlReader=txtReader #todo





#input k and id, return url_left and content, filepath
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
	suffix=menuCur[2] #后缀

	#拼凑出超链接
	url_left=""
	for i in range(len(menus)):
		#print("="*10,menus[i]["title"]);
		url_left+="<h5 class=title>"+menus[i]["title"]+"</h5>\n<ul class=submenu>\n";

		arr2=menus[i]["data"];
		for j in range(len(arr2)):
			#print("title=",arr2[j][0], str(i)+"_"+str(j) )
			cur=""
			if i==n0 and j==n1:
				cur=" class=cur"
			#
			item_url=url_for('hello2', k=k, id=str(i)+"_"+str(j)) #第一个参数是函数名，不是路由
			
			url_left+="<li"+cur+"><a href=" + item_url +">"+arr2[j][0]+"</a></li>\n"
		url_left+="</ul>\n"
	#关闭文件
	load_f.close();


	#根据文件类型，读取文件
	content="";
	if suffix=="html":
		content=htmlReader(filepath)
	elif suffix=="txt":
		content=txtReader(filepath)
	return (url_left, content,filepath)
#


#顶部菜单生成
def getTopMenu(k):
	load_f=open("data/topMenu.json",'r',encoding="utf8")
	#读取json
	menus = json.load(load_f)

	tmp=""
	for i in range(len(menus)):
		item_url=url_for('hello2', k=k, id="0_0")
		cur=""
		if menus[i][0]==k:
			cur=" current"
		tmp+=" <a class='topmenu"+cur+"' href=" + item_url +" title="+menus[i][1]+">"+menus[i][0]+"</a> "
	return tmp;

