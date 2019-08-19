/**
* name: 为md生成目录 markdown.js: 顶部1个，左下角一个
* version: 0.1
# 
*/


//======================
//depend on startMove.js
/**
* name: 为左下角生成目录外框架，
* version: 0.1
* version: 0.2 初始化时候显示在底部不动;
*/
function addCornerContentsBox() {
	var combox = document.getElementById("common_box");
	var cli_title = document.getElementById("cli_title");
	var cli_on = document.getElementById("cli_on");//cli_title.getElementsByTagName("b")[0];
	var flag = true, initime = null, r_len = 0;
	var height90=parseInt(document.documentElement.clientHeight*0.9); //parseInt(getStyle(combox,"height"));
	var width=400; //parseInt(getStyle(combox,"width"));
	
	cli_on.onclick = function () {
		var oD=$("f_content")
		//console.log(flag, height90, oD.style.height,oD.offsetHeight, oD.scrollHeight, parseInt(getComputedStyle(oD,false)['height']) )
		if(oD.scrollHeight+20<height90){
			height90=oD.scrollHeight+20;
		}
		/*如果不需要动态效果，这两句足矣
		combox.style.right = flag?'-270px':0;
		flag = !flag;
		*/
		var px_left=flag?0:(200-width);
		var px_height=flag?height90:30;
		startMove(combox, {"left": px_left, 'height':px_height, "width": 400})
		cli_on.innerHTML=flag?"-":"+";
		//
		flag = !flag;
	}
	//加载后3秒页面自动收缩；不打扰用户，初始化静默收缩在左下角.
	//initime = setTimeout("cli_on.click()", 100);
}


// 挂载函数到load事件
addEvent(window, 'load', function(){
	addCornerContentsBox();
});



//======================
/**
* name: 为顶部生成目录
* version: 0.1
* version: 0.2 修正点击锚点错位一行的问题
# 
*/
function addContents(){
	var oMd=document.getElementsByClassName("markdown")[0],
		aH=oMd.querySelectorAll("h1,h2,h3,h4,h5,h6"),
		oUl=createElement('ol');

	//创建content
	oContent=createElement('div',{'class':"content"},"")
	oMd.parentElement.insertBefore(oContent, oMd) //加入文档流

	//1. add "目录"
	oContent.append(createElement('h2',{},'Contents' ))
		
	for(var i=0;i<aH.length;i++){
		var oH=aH[i],
			text=oH.innerText,  //"5.启动nginx"
			tagName=oH.tagName;  //"H3"
		var indentNum='indent_'+ tagName.replace("H",''); //标题缩进行数
		
		if(text.trim()!=""){
			// if h tag is empty, do nothing
			//1. add anchor
			//console.log(i,tagName, text,  aH[i])
			//oH.parentNode.insertBefore( createElement('p',{}, ''), oH);//占位置
			oH.parentNode.insertBefore( createElement('a',{'name':i,
				'style':"margin-top:-1px; padding-top:1px; border:1px solid rgba(0,0,0,0.0);"
			},), oH ); //h前添加锚点,无显示
			
			//2. show in the contents
			var innerSpan = createElement('span',{},text );
			var innerLi = createElement('li',{'class':'text_menu '+indentNum} );
			// 添加点击锚点
			var innerA = createElement('a',{'href':'#'+i, 'title':tagName+": "+text}); //鼠标悬停提示文字
			// 装载锚点 
			innerLi.appendChild(innerSpan);
			innerA.appendChild(innerLi);
			oUl.appendChild( innerA );
		}
	}
	//2. add contents
	oContent.append( oUl); //加入文档流
	
	//3.加入左下角菜单中
	$("f_content").getElementsByTagName("div")[0].append( oUl.cloneNode(true) );
	// 复制节点 https://blog.csdn.net/LLL_liuhui/article/details/79978487
	
	
	//3. add "正文"
	//oContent.append( createElement('h2',{},'正文' )); //加入文档流
}


// 挂载函数到load事件
addEvent(window, 'load', function(){
	addContents();
});






//======================
/**
* name: 为左下角目录响应鼠标滚动
* version: 0.1
# 
*/

function highlightCurrentContent() {
	//为了保证兼容性，这里取两个值，哪个有值取哪一个
	//scrollTop就是触发滚轮事件时滚轮的高度
	var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
	//console.log("滚动距离" + scrollTop);
	//开始循环干活了
	//目录内容
	var oMenu=$('f_content');
	var aSpan=oMenu.getElementsByTagName("span");
	
	//正文内容
	var aA= document.querySelectorAll("a[name]");
	//对正文的锚点进行遍历
	for(var i=0;i<aA.length;i++){
		if(aA[i].offsetTop<scrollTop){
			//remove class cur, for 导航
			for(var j=0;j<aSpan.length;j++){
				aSpan[j].parentElement.parentElement.setAttribute("class","");
			}
			
			//add class cur, for 导航
			var oA=aSpan[i].parentElement.parentElement
			oA.setAttribute("class","cur")
		}
	}
}

// 挂载函数到事件
addEvent(window, 'scroll', function(){
	highlightCurrentContent();
});
