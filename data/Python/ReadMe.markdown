# txtBlog.py 简介




## 测试代码高亮效果
### Python web
快速启动一个服务器，可以使用flask包:
```Python
from flask import Flask
app = Flask(__name__)
@app.route('/')  
def hello_world():
    return "hello world"
if __name__=='__main__':
    app.run(host="192.168.2.120",port=8000)
```


### JavaScript closure
定时器练习：每秒钟打印一个数字，该数字递增。
```JavaScript
for(var i = 0; i < 5; i++) {
	(function(a){
		console.log("i=",i);
		setTimeout(function () {
			console.log(a);
		}, 1000*a);
	})(i)
}
console.log('a');
```

### C语言
```C
#include<stdio.h>
int main(){
	int i=10;
	char word[]="C world";
	printf("hello, %s! %d\n", word, i);
}
// hello, C world! 10
```