from flask import Flask, escape,request, url_for,render_template,send_from_directory,redirect
from txtBloglib import *
from footer_urls import *

app = Flask(__name__)

# when browse the root /, jump to hello page immediately.
@app.route('/') #没参数时
def index():
	url=url_for('hello',k="Python",id="0_0") #第一个参数是函数名，不是路由
	return '<meta http-equiv="refresh" content="0;url='+url+'">'
	#return redirect(url_for('hello',k="Python",id="0_0")); 
#

@app.route('/index/<k>/') #只有1个参数时
def hello2(k):
	url=url_for('hello',k=k,id="0_0")
	return '<meta http-equiv="refresh" content="0;url='+url+'">'
	#return redirect(url_for('hello',k=k,id="0_0")); 
#

#1.Get paras from url: k and id, and response almost all the requests.
@app.route('/index/<k>/<id>.html') #2个参数时
def hello(k,id="0_0"):
	#get top menu html
	topMenu=getTopMenu(k);

	#get leftMenu and content html
	rs=getData(k,id)
	if(len(rs)<3):
		return render_template('page_not_found.html',info=rs[1])

	#bottom links html, defined in footer_urls.py
	footer='友情链接[IT Tools]: '+get_links(footer_urls["links_IT_tools"]);
	footer+='<br />生物信息学: '+get_links(footer_urls["bio_info"]);

	#render template
	return render_template('hello.html', topMenu=topMenu, leftMenu=rs[0], filepath=rs[2],  \
		content=rs[1], lastModified=rs[3],suffix=rs[4], footer=footer)
# http://127.0.0.1:8000/index/Python/0_0.html



#



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
	#app.run(host="127.0.0.1",port=8000) #default, private
	app.run(host="0.0.0.0",port=8000) #public