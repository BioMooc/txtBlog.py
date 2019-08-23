from flask import Flask, escape,request, url_for,render_template,send_from_directory,redirect
from txtBloglib import *
from footer_urls import *


app = Flask(__name__)

# when browse the root /, jump to hello page immediately.
@app.route('/')
def index():
	url=url_for('hello') #第一个参数是函数名，不是路由
	return '<meta http-equiv="refresh" content="0;url='+url+'">'
#


#1.Get paras from url: k and id, and response almost all the requests.
@app.route('/index.py')
def hello():
	#get paras, with default values.
	kw = request.args.get("k", "Python")
	id = request.args.get("id", "0_0")

	#get top menu html
	topMenu=getTopMenu(kw);

	#get leftMenu and content html
	rs=getData(kw,id)

	#bottom links html, defined in footer_urls.py
	footer='友情链接[IT Tools]: '+get_links(footer_urls["links_IT_tools"]);
	footer+='<br />生物信息学: '+get_links(footer_urls["bio_info"]);

	#render template
	return render_template('hello.html', topMenu=topMenu, leftMenu=rs[0], filepath=rs[2],  \
		content=rs[1], lastModified=rs[3],suffix=rs[4], footer=footer)
# http://blog2.163.com:8000/index.py?k=R&id=0_0


# accept alternative URL: send k and id with url
# http://blog2.163.com:8000/s/R/0_0
@app.route('/s/<keyword>/<id>')
def profile(keyword,id):
	#return 'k:{} <br>id:{}'.format(escape(keyword), escape(id))
	return redirect(url_for('hello',k=escape(keyword), id=escape(id)))



# 添加新静态文件的路径，这样就允许data/下的图片加载了
@app.route("/data/<path:filename>")
def downloader(filename):
    return send_from_directory("data",filename,as_attachment=False)



# define a 404 page, and jump to new page in 5 seconds.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


# run the app
if __name__ == '__main__':
	app.debug = True # 设置调试模式，生产模式的时候要关掉debug
	#app.run(host="blog2.163.com",port=8000)
	app.run(host="127.0.0.1",port=8000) #default