from flask import Flask, escape,request, url_for,render_template,send_from_directory
from txtBloglib import *

app = Flask(__name__)


@app.route('/')
def index():
	url=url_for('hello2') #第一个参数是函数名，不是路由
	return '<meta http-equiv="refresh" content="0;url='+url+'">'
	#return '<a target=_blank href='+urls+'>index</a> '+urls


#1.从url传入get参数:k和id
@app.route('/index.py')
def hello2():
	#get paras
	kw = request.args.get("k", "R")
	id = request.args.get("id", "0_0")

	#top menu
	topMenu=getTopMenu(kw);
	
	#bottom links
	footer="""
<br />友情链接[IT Tools]: <a href='http://jsbin.com/' target='_blank' title="练习前端的好工具！">jsbin</a> | 
"""
	
	#获取左侧munu和文章内容
	rs=getData(kw,id)
	#return html+"<hr>"+rs[0]+"<hr>"+rs[2]+"<hr>"+rs[1];
	
	return render_template('hello.html', topMenu=topMenu, leftMenu=rs[0], filepath=rs[2], content=rs[1], \
		lastModified=rs[3],suffix=rs[4], footer=footer)
	
# http://blog2.163.com:8000/index.py?k=R&id=0_0
# keyword:k:Java
# id: 0_0

#2.直接从url分离参数：k和id
@app.route('/s/<keyword>/<id>')
def profile(keyword,id):
	return 'k:{} <br>id:{}'.format(escape(keyword), escape(id))
# http://blog2.163.com:8000/s/Java/0_0
# k:Java 
# id:0_0




if __name__ == '__main__':
	app.run(host="blog2.163.com",port=8000)