from flask import Flask, escape,request, url_for
from txtBloglib import *

app = Flask(__name__)

#生成url
@app.route('/')
def index():
    urls=url_for('hello2', k='Java',id="0_0") #第一个参数是函数名，不是路由
    return '<a target=_blank href='+urls+'>index</a> '+urls


#1.从url传入get参数:k和id
@app.route('/index.py')
def hello2():
    kw = request.args.get("k", "Python")
    id = request.args.get("id", "0_0")
    #strs= 'keyword:{escape(kw)}<br>id: {escape(id)}'
	#top menu
    strs=getTopMenu(kw);
	
    rs=getData(kw,id)
    return strs+"<hr>"+rs[0]+"<hr>"+rs[2]+"<hr>"+rs[1];
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