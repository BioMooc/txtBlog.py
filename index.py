from flask import Flask, escape,request, url_for,render_template,send_from_directory,redirect
from txtBloglib import *
from footer_urls import *

app = Flask(__name__)



@app.route('/')
def index():
	url=url_for('hello') #第一个参数是函数名，不是路由
	return '<meta http-equiv="refresh" content="0;url='+url+'">'
	#return '<a target=_blank href='+urls+'>index</a> '+urls


#1.Get paras from url: k and id
@app.route('/index.py')
def hello():
	#get paras
	kw = request.args.get("k", "R")
	id = request.args.get("id", "0_0")

	#get top menu
	topMenu=getTopMenu(kw);
	
	#get leftMenu and content
	rs=getData(kw,id)
	#return html+"<hr>"+rs[0]+"<hr>"+rs[2]+"<hr>"+rs[1];
	
	#bottom links, defined in footer_urls.py
	footer='友情链接[IT Tools]: '+get_links(footer_urls["links_IT_tools"]);
	footer+='<br />生物信息学: '+get_links(footer_urls["bio_info"]);

	#render template
	return render_template('hello.html', topMenu=topMenu, leftMenu=rs[0], filepath=rs[2],  \
		content=rs[1], lastModified=rs[3],suffix=rs[4], footer=footer)
# http://blog2.163.com:8000/index.py?k=R&id=0_0



#alternative: send k and id with url
@app.route('/s/<keyword>/<id>')
def profile(keyword,id):
	#return 'k:{} <br>id:{}'.format(escape(keyword), escape(id))
	return redirect(url_for('hello',k=escape(keyword), id=escape(id)))
# http://blog2.163.com:8000/s/R/0_0



# 添加新静态文件的路径，这样就允许data/下的图片加载了
@app.route("/data/<path:filename>")
def downloader(filename):
    return send_from_directory("data",filename,as_attachment=False)

"""
#这一句有啥用呢?
app.add_url_rule('/data/<path:filename>',endpoint='data',build_only=True)
"""


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')
#


if __name__ == '__main__':
	app.debug = True # 设置调试模式，生产模式的时候要关掉debug
	app.run(host="blog2.163.com",port=8000)