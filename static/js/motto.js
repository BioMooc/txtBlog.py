/*
* 封装的页面底部名人名言显示框架
* v0.2
* 调用格式 motto_Plugin.run([x ,y], obj); 第一个参数是坐标，相对于浏览器左下角，可选。第二个参数obj，要内包含<span>，可选。
比如 
motto_Plugin.run(); 
motto_Plugin.run([100 ,30], document.getElementsByClassName("motto")[1]);

* 需要样式表配合。
*/

(function(){
	//封装插件
	var motto_Plugin={
		'mottos':[
			"及时当勉励，岁月不待人！",
			"身体是革命的本钱。",
			"千里之行，始于足下。",
			"子曰：逝者如斯夫，不舍昼夜。",
			"如果有一天我好运来临，那一定是我努力所得，并非上天眷顾。",
			"The future belongs to those who believe in the beauty of their dreams.",
			//"Some 5,000 red-winged blackbirds, European starlings, common grackles and brown-headed cowbirds suffered blunt-force trauma after colliding with cars, trees and buildings, an ornithologist from the Arkansas Game and Fish Commission would tell National Geographic. //[熟词生义] game. 猎物",
		],
		'bgColors':['red','#F19C01','#A49B03','green','blue','#18C1C1','purple','black'],
/*
#F19C01 orange
#D2C701 yellow A49B03
// Math.random(); 产生 [0, 1) 之间的随机数
*/
		//define methods;
		$:function(s){
			return document.getElementById(s);
		},
		run:function(coord,obj){
			var oDiv=document.createElement("div");
			oDiv.setAttribute("class",'motto');
			oDiv.append(document.createElement("span"));
			var obj=obj|| oDiv;
			if(obj==oDiv){
				document.body.append(oDiv);
			}
			
			var coord=coord||[0,0]
			obj.style.left=coord[0]+"px";
			obj.style.bottom=coord[1]+"px";
			
			var o=obj.getElementsByTagName("span")[0];//获取内部的span
			var _this=this;//纠正this指向
			o.parentElement.setAttribute("title",'我是名言名句君');
			o.innerHTML=_this.mottos[ Math.floor(Math.random()*(_this.mottos.length) ) ];//随机选中一句名人名言
			//每2秒检查一下执行情况
			setInterval(function(){
				//console.log(this);
				var left=parseInt(o.style.left);
				
				if (left==0 || isNaN(left)){//缩回去
					startMove(o, {'left':o.offsetWidth+10}, 'easeOut', 20,function(){
						this.parentElement.style.background=_this.bgColors[ Math.floor(Math.random()*(_this.bgColors.length) ) ];
						//o.parentElement.style.background="red"
					});
				}else if(left==o.offsetWidth+10){ //可见
					startMove(o, {'left':0}, 'easeOut', 0.1, function(){//easeOut linear
						//clearTimeout(o.timer2);//清除定时器;
						o.style.left=1+"px";
						o.timer2=setTimeout(function(){
							o.style.left=0+'px';
						},10000); //暂停5s
					});
				}else{
					//console.log("啥都没做")
				}
			}, 2000);
		} //end of run;
	}
	//挂载到全局对象上
	window.motto_Plugin=motto_Plugin;
})();
//end of plugin

//这是比较安全的绑定方式
addEvent(window, 'load', function(){
	motto_Plugin.run( [ Math.min(document.body.offsetWidth/4,200),0]);
});