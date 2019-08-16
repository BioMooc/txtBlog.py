/* 添加目录
*v 0.2
*/
function addContents(){
	//get dom: h4 node
	var	oContent=getElementsByClassName('content')[0],
		oPre=oContent.getElementsByTagName('pre')[0],
		aH4=oPre.getElementsByTagName('h4'),
		
		oDiv=createElement('div'),
		oUl=createElement('ol');
	//add h2 title
	oDiv.appendChild( createElement('h2',{},'目录' ) );
	//oDiv.appendChild( createElement('p',{}, 'lastModified: ' + document.lastModified ) );
	//添加内容
	for(var i=0;i<aH4.length;i++){
		var text=aH4[i].innerHTML;
		if(trim(text)!=''){
			// 添加锚定a标签到h4标签前面，包含显示编号
			var oH4 = aH4[i], oHr=oH4.previousSibling;
			oHr.parentNode.insertBefore( createElement('a',{'name':i}, ''), oHr ); //hr.top前加锚点,无显示
			oH4.parentNode.insertBefore( createElement('a',{'class':'smallA'}, '[Section '+(i+1)+']'), oH4 ); //h4前显示section，从1开始，而不是0.
			
			//li中添加span,span中添加text
			var innerSpan = createElement('span',{},text );
			var innerLi = createElement('li',{'class':'text_menu'} );
			
			// 添加点击锚点
			var innerA = createElement('a',{'href':'#'+i});
			
			// 装载锚点 
			innerLi.appendChild(innerSpan);
			innerA.appendChild(innerLi);
			oUl.appendChild( innerA );
		}
	}
	oDiv.appendChild( oUl );
	//添加标题
	oDiv.appendChild( createElement('h2',{},'正文' ) );
	//加入文档流
	oContent.insertBefore( oDiv, oPre);
}

//风险：修改的时候防止被覆盖！
/*
window.onload=function(){
	addContents();
}
*/
//这是比较安全的绑定方式
addEvent(window, 'load', function(){
	addContents();
});

