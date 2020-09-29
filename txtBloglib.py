import json,re,time,os
from flask import escape, url_for
#import mistune
import configparser
# version 0.0.7-8
# version 0.0.7-9 部分支持行内Math






#import re
from mistune import Renderer, Markdown, InlineLexer
# todo 单引号括起来的还没有处理好？ //------> todo
# define new sub class
#让mistune不后台处理$$和$$之间的LaTex代码，交给前台的js处理成数学公式
class LaTexRenderer(Renderer):
    #def LaTex(self, alt, link):
    def LaTex(self, text):
        return '$$%s$$' % (text)
    def LaTex_inline(self, text):
        return '$%s$' % (text)


class LaTexInlineLexer(InlineLexer):
    def enable_LaTex(self):
        # add LaTex rules
        self.rules.LaTex = re.compile(
            r'\$$'                   # $$ 头
            r'([\s\S]+?)'   # *** 中间
            r'\$$(?!\])'             # $$ 尾
        )
        # Add LaTex parser to default rules
        # you can insert it some place you like
        # but place matters, maybe 3 is not good
        self.default_rules.insert(3, 'LaTex')
        #
        self.rules.LaTex_inline = re.compile(
            r'\$'                   # $$ 头
            r'([\s\S]+?)'   # *** 中间
            r'\$(?!\])'             # $$ 尾
        )
        self.default_rules.insert(0, 'LaTex_inline')


    def output_LaTex(self, m):
        text = m.group(1)
        #alt, link = text.split('|')
        # you can create an custom render
        # you can also return the html if you like
        #return self.renderer.LaTex(alt, link)
        return self.renderer.LaTex(text)
    def output_LaTex_inline(self, m):
        text = m.group(1)
        #alt, link = text.split('|')
        # you can create an custom render
        # you can also return the html if you like
        #return self.renderer.LaTex(alt, link)
        return self.renderer.LaTex_inline(text)
# the end of sub class

# 跳过LaTex片段的markdown to html parser mistune子类
def md2html(md):
	renderer = LaTexRenderer()
	inline = LaTexInlineLexer(renderer)
	# enable the feature
	inline.enable_LaTex()
	markdown = Markdown(renderer, inline=inline)
	return markdown(md)
#







# read configure file
# v0.1 没有该值怎么办？
def getConf(section, item): 
	base_dir = str(os.path.dirname(__file__))
	base_dir = base_dir.replace('\\', '/')
	file_path = base_dir + "./config/conf.ini"
	#return base_dir;
	#print("file_path=", file_path);
	
	cf = configparser.ConfigParser()   # configparser类来读取config文件
	cf.read(file_path)

	return cf.get(section, item); 


#文本文件阅读器，input filepath, return string from the file.
#v0.3 <h4>下添加换行，防止遮挡;
#v0.4 对尖括号转码
#v0.5 添加纸质背景
#v0.6 分离txt.css，支持在config/conf.ini配置文件中切换皮肤
def txtReader(fpath,txtStyle="ubuntu1"):
	fr=open(fpath, 'r', encoding="utf8")
	tmp=''
	for lineR in fr.readlines():
		#line=lineR.strip("\n")#去除两端的换行
		line= re.sub(r'\n$',"", lineR) #只去除末尾的换行

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
	css='<link rel="stylesheet" type="text/css" href="/static/css/txt.css" media="all">\n'
	js='<script type="text/javascript" src="/static/js/txt.js"></script>\n\n'
	#获取配置风格
	txtStyle=getConf('style','txt');
	
	return css+js+"<div class='content'><pre class="+txtStyle+">" + tmp + "</pre></div>\n";

#html读取器
#v0.1
def htmlReader(fpath):
	fr=open(fpath, 'r', encoding="utf8")
	tmp=fr.read();
	fr.close();
    
    # LaTex
	#js3='<script src="/static/js/MathJax.js"></script>\n';
	js3='<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>';
	js3+='<script src="/static/js/showLaTex.js"></script>\n\n';
	if getConf("function","LaTex")=="on":
		tmp=tmp+js3;
        
	return tmp;
#

#markdown读取器
#v0.1
#v0.2 增加top目录
#v0.3 代码高亮
#v0.4 左下角添加目录
#v0.5 增加LaTex支持，依赖MathJax.js，不好用。因为mistune解析markdown时转义_为<i>，导致带有_的公式转换失败
#v0.6 LaTex根据配置文件，决定是否加载
def markdownReader(fpath):
	# read markdown
	fr=open(fpath, 'r', encoding="utf8")
	text=fr.read()
	fr.close()
    
    #遇到 MathJax 和markdown 冲突怎么办?https://www.v2ex.com/t/240363
    # mathjax中的'_'(下划线字符 下标)与markdown中的斜体冲突
    
    
	# markdown to html
	#tmp=mistune.markdown(text, escape=False, hard_wrap=True) #'I am using **mistune markdown parser**'
	tmp=md2html(text) #'I am using **mistune markdown parser**'  , escape=False, hard_wrap=True
	tmp="<div class=markdown>\n"+tmp+"</div>\n"
	#tmp="<div class=content>\n"+tmp+"</div>\n"
	
	# left bottom corner contents 
	cornerContents="""
<div id="common_box">
	<div id="cli_title" class=title> Contents <b id="cli_on">+</b></div>
	<div id="f_content" class=container>
		<div class=content></div>
		<div class="title">==This is the bottom==</div>
	</div>
</div>
<script type="text/javascript" src="/static/js/startMove.js"></script>\n
"""
	tmp+=cornerContents;#这个框架的内容由js在markdown.js中填充
	
	# add markdown style sheet and top contents js, left bottom corner contents.
	mdStyle=getConf("style","markdown") #get markdown style file name from config file.
	css='<link rel="stylesheet" type="text/css" href="/static/css/'+mdStyle+'.css" media="all">\n'
	js='<script type="text/javascript" src="/static/js/markdown.js"></script>\n\n'
	tmp=css+js+tmp;
	codeNumberJS='''
addEvent(window, 'load', function(){
    //1. get pre code
    var aPre=document.getElementsByTagName('pre');
    var aCode=[]
    for(var i=0;i<aPre.length;i++){
    var oPre=aPre[i]
    var aCode1=oPre.getElementsByTagName('code');
    if(1== aCode1.length){
        var oCode=aCode1[0]
        aCode.push(oCode)
        //2. get text inside
        var lines=oCode.innerHTML.split("\\n")
        var n=lines.length;
        //console.log('i=',i, lines, '; n=',n)

		//3.make a dom of numbering
		var oUl=document.createElement('ul');
		oUl.setAttribute('class', 'pre-numbering');
		for(var j=0;j<n-1;j++){
			var oLi=document.createElement('li');
			oLi.innerHTML=j+1;
			oUl.append(oLi)
		}
		//4. add to code
		oPre.append(oUl)
		oCode.setAttribute('class', oCode.getAttribute('class')+ ' has-numbering')
        oPre.setAttribute('class', 'prettyprint')
	}
}
})
'''
	# high light code
	css2='<link rel="stylesheet" href="/static/css/highlight-routeros.css">\n'
	js2='<script src="/static/js/highlight.pack.js"></script>\n\n'
	tmp=tmp + css2+js2   + '<script>hljs.initHighlightingOnLoad();'+codeNumberJS+'</script>';
	
	# LaTex
	#js3='<script src="/static/js/MathJax.js"></script>\n';
	js3='<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>';
	js3+='<script src="/static/js/showLaTex.js"></script>\n\n';
	if getConf("function","LaTex")=="on":
		tmp=tmp+js3;
	
	return tmp;



#input k and id, return url_left and content, filepath
#v0.3
def getData(k,id):
	#1.解析id为2个数字
	arr=re.split("_", id)
	n0=int(arr[0])
	n1=int(arr[1])

	#2.解析json文件获取左侧目录，和文件名字
	#读取json
	fname="data/"+k+".json";
	if not os.path.isfile(fname):
		return (0, fname + " not found!"); # 响应找不到目录.json错误
	#
	load_f=open(fname,'r',encoding="utf8")
	menus = json.load(load_f);
	load_f.close();

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

	#如果是英语频道，则新增底部英语随机句子。
	if k=="English" or getConf('function','motto')=="on":
		content+='\n<script src="/static/js/startMove_OOP.js"></script>\n<script src="/static/js/motto.js"></script>\n';

	return (url_left, content,filepath.replace("data/",""), lastModified,suffix)
	#          0        1       2                              3           4


#顶部菜单生成
#v0.2
def getTopMenu(k):
	#读取json
	load_f=open("data/topMenu.json",'r',encoding="utf8")
	menus = json.load(load_f);
	load_f.close();

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