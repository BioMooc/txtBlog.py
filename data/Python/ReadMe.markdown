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

或者一行实现简单web预览图片功能: `$ python -m http.server --bind 192.168.2.100 8001`




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















## LaTex

txtBlog.py uses MathJax.js([cnd](https://cdnjs.com/libraries/mathjax), [github](https://codeload.github.com/mathjax/MathJax/zip/2.7.5), [docs](https://mistune.readthedocs.io/en/latest/)) to render LaTeX inside html/markdown(some). Just put your LaTeX math inside `$$`.

开启或者关闭LaTex解析功能，`请在 /config/conf.ini 中的设置 LaTex = on 或 off(默认)`。

> 目前只有 mistune v0.x.x 版本支持 LaTex，而更高的版本 v1.x.x 或 v2.x.x 或 v3.x.x 暂时不支持 LaTex 解析。

> 本质是一个跳过 $$ xx $$ 中的内容，原样留给html页面的 js 渲染公式。

```
如果太复杂，可能放弃开发该功能。
> python -V
Python 3.8.0

卸载老版本
$ pip3 uninstall mistune #v2.0.5

安装新版本
$ pip3 install mistune -i https://pypi.douban.com/simple/

还是老版本！尝试更新 pip
$ python -m pip install --upgrade pip -i https://pypi.douban.com/simple/
$ python -m pip install --upgrade mistune -i https://pypi.douban.com/simple/

再次指定版本安装
$ pip3 uninstall mistune
$ pip3 install mistune==3.0.1 -i https://pypi.douban.com/simple/
Looking in indexes: https://pypi.douban.com/simple/
ERROR: Could not find a version that satisfies the requirement mistune==3.0.1 (from versions: 0.1.0, 0.2.0, 0.3.0, 0.3.1, 0.4, 0.4.1, 0.5, 0.5.1, 0.6, 0.7, 0.7.1, 0.7.2, 0.7.3, 0.7.4, 0.8, 0.8.1, 0.8.2, 0.8.3, 0.8.4, 
2.0.0a1, 2.0.0a2, 2.0.0a3, 2.0.0a4, 2.0.0a5, 2.0.0a6, 2.0.0rc1, 2.0.0, 2.0.1, 2.0.2, 2.0.3, 2.0.4, 2.0.5, 
3.0.0a1, 3.0.0a2, 3.0.0a3, 3.0.0rc1, 3.0.0rc2, 3.0.0rc3, 3.0.0rc4, 3.0.0rc5)
目前找不到该版本。

$ pip3 install mistune==0.8.4 -i https://pypi.douban.com/simple/
```



(1) 正常显示 **行内**
 
这个公式 $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ 是很牛叉的。

Therefore, given the squared distances between rows ($D\bullet D$) and the cross product of the centered matrix $B=(HX)(HX)^t$, we have shown.



(2) 正常显示 **行间**

$$c = \sqrt{a^2 + b^2}$$


行间吗 $$\alpha+\beta=\gamma$$

$$\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}\int_{0}^{1}f(x)dx \sum_{1}^{2}$$


$$
S^{(r) } =
\begin{pmatrix}
s_1 &0 & 0 &0 &...\\
0&s_2&0 & 0 &...\\
0& 0& ...& ... & ...\\
0 & 0 & ... & s_r &...\\
...& ...& ...& 0 & 0 \\
\end{pmatrix}
$$


$$
\begin{equation*}
\text{stress}^2=\frac{\sum(f(d)-\tilde{d})^2}{\sum d^2}.
\end{equation*}
$$


$$
\begin{equation*}
{\cal X}^2=\sum_{i,j} \frac{\left(n_{ij}-\frac{n_{i\cdot}}{n}\frac{n_{\cdot j}}{n}n\right)^2}
{\frac{n_{i\cdot}n_{\cdot j}}{n^2}n}
\end{equation*}
$$



(3) 测试行内长公式，其中的下划线常常被markdown错误的提前解析，公式内出现em标签导致`mathJax无法解析`。

$$\varGamma(x)=\frac{\int_{\alpha}^{\beta}g(t)(x-t)^2\text{d}t}{\phi(x)\sum_{i=0}^{N-1}\omega_i}\tag{2}$$

$\varGamma(x)=\frac{\int_{\alpha}^{\beta}g(t)(x-t)^2\text{d}t}{\phi(x)\sum_{i=0}^{N-1}\omega_i}$

行内公式不能正常显示 $\varGamma(x)=\frac{\int_{\alpha}^{\beta}g(t)(x-t)^2\text{d}t}{\phi(x)\sum_{i=0}^{N-1}\omega_i}$ int后的下划线










## 长片段R代码
```R
# 使用 DESeq2分析DEG，并画火山图
##########################
# 1 get DE gene list, with DESeq2
##########################
library(DESeq2)

# matrix
countData <- cbind( RNA[,cid.norm], RNA[,cid.sync] )
dim(countData) #14675    56
countData[1:4,1:4]
#过滤掉5个细胞以下表达的基因
df=data.frame(
  gene=row.names(countData),
  num.N=apply(countData[, cid.norm]>0,1,sum),
  num.S=apply(countData[, cid.sync]>0,1,sum),
  row.names = 1
)
head(df)
df2=df[which(df$num.N>5 & df$num.S>5),]
dim(df2) #7487 2
#
countData=countData[rownames(df2),]
dim(countData) #[1] 7487   56

#条件
condition <- factor(c( rep('normal', length(cid.norm)), rep('sync', length(cid.sync))  ), 
                    levels=c('normal','sync'))
condition
#
dds <- DESeqDataSetFromMatrix(countData, DataFrame(condition), design= ~ condition )
# 过滤
nrow(dds) #7487
dds2 <- dds[ rowSums(counts(dds)) > 1, ]
nrow(dds2)#[1] 7487

keyword='sync_VS_normal_HeLa'
#
#一步法
dds3 <- DESeq(dds2) #耗时1min
## estimating size factors
## estimating dispersions
## gene-wise dispersion estimates
## mean-dispersion relationship
## final dispersion estimates
## fitting model and testing
## -- replacing outliers and refitting for 5164 genes
## -- DESeq argument 'minReplicatesForReplace' = 7 
## -- original counts are preserved in counts(dds)
## estimating dispersions
## fitting model and testin

#获取结果
res <- results(dds3)
head(res)
#log2 fold change (MLE): condition sync vs normal 
#Wald test p-value: condition sync vs normal 
#DataFrame with 6 rows and 6 columns
#baseMean     log2FoldChange             lfcSE               stat             pvalue
#<numeric>          <numeric>         <numeric>          <numeric>          <numeric>
#  AAAS  45.0706763507379 -0.286189288744119 0.984181112955205 -0.290789251060485  0.771212506698282
#AAGAB 37.6621410990222  0.761637086304566   1.1243489415785  0.677402768961818  0.498150441980007

#                   padj
#              <numeric>
# AAAS  0.941981213557402
#AAGAB 0.849654084021838

# 校正后p-value为NA的赋值为1
res$padj[is.na(res$padj)] = 1

# order
res <- res[order(res$padj),]
dim(res) #7487 6

# set cutoff
resSig <- subset(res, abs(log2FoldChange)>log2(2) & padj < 0.05)
dim(resSig) #[1] 252  6
head(resSig)

#save to file
resSig<-data.frame(resSig)
dim(resSig) #[1] 252   6
head(resSig)
write.csv(resSig, file=paste0("DESeq2_DEG_",keyword,".csv") )


#save all file for GSEA
res2=data.frame(res)
dim(res2) #7487 6
head(res2)
write.csv(res2, file=paste0("DESeq2_ALL_",keyword,".csv") )




##########################
# 2 volcano plot
##########################
library('ggplot2')
dif=data.frame(res)
dif$threshold= factor( abs(dif$log2FoldChange) > log2(1.5) & dif$padj < 0.05, #1.5倍, 0.05
                       levels=c(TRUE,FALSE) )
str(dif)
head(dif)
tb=table(dif$threshold);tb
#TRUE FALSE 
#304  7235

#
dif$threshold2="ns";
dif[which(dif$log2FoldChange > log2(1.5) & dif$padj < 0.05),]$threshold2="up";
dif[which(dif$log2FoldChange < (-log2(1.5)) & dif$padj < 0.05),]$threshold2="down";
dif$threshold2=factor(dif$threshold2, levels=c('down','ns','up'))
tb2=table(dif$threshold2);tb2
#down   ns   up 
#130 7183  174

# save up and down gene list
geneUp=row.names(dif[which(dif$threshold2=='up'),]);length(geneUp) #174
head(geneUp)
writeLines(geneUp, paste0('DESeq2_', keyword,'_genes_UP.txt') )
#
geneDown=row.names(dif[which(dif$threshold2=='down'),]);length(geneDown) #130
head(geneDown)
writeLines(geneDown, paste0('DESeq2_', keyword,'_genes_DOWN.txt') )

##############
g = ggplot(data=dif, aes(x=log2FoldChange, y=-log10(padj), color=threshold2)) +
  geom_point(alpha=0.4, size=0.4) +
  theme_bw() +
  theme(legend.box = "horizontal", #显著性图例，水平，标到底部
        legend.position="bottom") +
  #scale_color_manual('Significant',labels=c("TRUE","FALSE"), values=c("red", "grey") )+ 
  scale_color_manual('Significant',labels=c(paste0("down(",tb2[[1]],')'),'ns',
                                            paste0("up(",tb2[[3]],')' )),
                     values=c("blue", "grey",'red') )+
  xlab("log2(FoldChange)") + ylab("-log10(p.adj)") +
  labs(title= paste0("DEG: ",keyword) ); g
# add text to a few genes
dd_text = dif[ ((abs(dif$log2FoldChange) > 2) & (dif$padj < 1e-10) ) | 
                 abs(dif$log2FoldChange) > 5.5,]; dim(dd_text)
head(dd_text)
#add text
library(ggrepel)
g2=g + geom_text_repel(data=dd_text, aes(x=log2FoldChange, y=-log10(padj), label=row.names(dd_text)), 
                       size=2.5, colour="black",alpha=0.6); g2
#保存图片
CairoPDF(file=paste0('volcano_plot_',keyword,'.pdf'), width=3.6,height=4)
print(g2)
dev.off()
#

##########################
# 3 check the counts; 用原始counts还是用标准化过后的呢？
##########################
showCounts=function(gene1){
  print(gene1)
  c0=as.numeric(RNA[gene1,cid.norm]);
  c1=as.numeric(RNA[gene1,cid.sync]);
  deltaCV=sd(c1)/mean(c1)-sd(c0)/mean(c0)
  df=data.frame(
    counts=c(c0,c1),
    type=c(rep('normal', length(c0)),   rep('sync', length(c1)) )
  )
  #library(ggplot2)
  g=ggplot(df, aes(type,log10(counts+1),color=type))+
    theme_bw()+
    geom_boxplot()+geom_jitter(size=0.5, alpha=1)+
    scale_color_manual(values=c('grey','#93BBFD'))+
    labs(title=gene1,x=paste0("deltaCV:",round(deltaCV,2) ) , y="log10(RNAcounts+1)")
  g
}
dd_text=dd_text[order(-dd_text$log2FoldChange),]
head(dd_text)
dim(dd_text) #21
geneUp2=rownames(dd_text[which(dd_text$log2FoldChange>0),] );length(geneUp2) #13
geneDown2=rownames(dd_text[which(dd_text$log2FoldChange<0),] );length(geneDown2) #8
#
CairoPDF(file=paste0("02-Check_counts_", keyword,".pdf"),width=7,height=5)
grid.arrange(
  showCounts(geneUp2[1]),
  showCounts(geneUp2[2]),
  showCounts(geneUp2[13]),
  
  showCounts(geneDown2[1]),
  showCounts(geneDown2[7]),
  showCounts(geneDown2[8]),
  nrow=2
)
dev.off()
```