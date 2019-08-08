
#**
# 根据友情链接数组，输出拼接好的字符串。【对外】
# 1.输入一级数组： ['http://jsbin.com/','jsbin','练习前端的好工具！']
# 2.或二级数组：
#	[
#		['http://jsbin.com/','jsbin','练习前端的好工具！'],
#		['http://jquery.cuishifeng.cn/','jQuery手册']
#	];
# 3.返回链接字符串。
def get_links(arr):
	def get_link(ar):
		title=""
		if len(ar)>2:
			title="title="+ar[2]
		return "<a target=_blank href="+ar[0]+" "+title+">"+ar[1]+"</a>\n"
	#
	if isinstance(arr[0],str):
		return get_link(arr);
	html=""
	for i in range(len(arr)):
		html+=get_link(arr[i])
	return html;
#


links_IT_tools=[
	['http://jsbin.com/','jsbin','练习前端的好工具！'],
	['http://jquery.cuishifeng.cn/','jQuery手册'],
	['http://www.runoob.com/','菜鸟教程网'],
	['http://www.w3school.com.cn/','w3school'],
	['http://php.net/','PHP']
];

htmlLink='<br />友情链接[IT Tools]: ';
htmlLink+=get_links(links_IT_tools);
print(htmlLink)