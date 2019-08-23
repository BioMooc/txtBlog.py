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





### LaTex

txtBlog.py uses MathJax.js([cnd](https://cdnjs.com/libraries/mathjax), [github](https://codeload.github.com/mathjax/MathJax/zip/2.7.5), [docs](https://mistune.readthedocs.io/en/latest/)) to render LaTeX inside html/markdown(some). Just put your LaTeX math inside `$$`.


$$c = \sqrt{a^2 + b^2}$$

$\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$。

$\varGamma(x)=\frac{\int_{\alpha}^{\beta}g(t)(x-t)^2\text{d}t}{\phi(x)\sum_{i=0}^{N-1}\omega_i}\tag{2}$

$$
\varGamma(x)=\frac{\int_{\alpha}^{\beta}g(t)(x-t)^2\text{d}t}{\phi(x)\sum_{i=0}^{N-1}\omega_i}\tag{2}
$$


$$\alpha+\beta=\gamma$$


$$\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}$$

