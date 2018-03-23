30分钟写出一个51job职位小爬虫,小白也能写的出来,不用懂正则, 不用懂xpath,分分钟写出来,大神走开
# 前提环境:你的电脑里装过python 2/3 和 pip(python包管理工具)
* 第一步: 命令行输入 sudo pip install scrapy
安装scrapy,scrapy是一个非常流行的爬虫框架使用简单,这一步你网速够快5秒搞定
* 第二步:命令行输入 scrapy startproject my51JobSpider
创建了一个scrapy叫 my51JobSpider,看看目录,创建成功,耗时1秒
```
├── README.md
└── my51JobSpider
├── my51JobSpider
│   ├── __init__.py
│   ├── __pycache__
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg
```
下面来简单介绍一下各个主要文件的作用：
> scrapy.cfg ：项目的配置文件
/ ：项目的Python模块，将会从这里引用代码
items.py ：项目的目标文件
pipelines.py ：项目的管道文件
settings.py ：项目的设置文件
> spiders/ ：存储爬虫代码目录

![Snip20180323_15.png](https://upload-images.jianshu.io/upload_images/3258209-2bc68ed566129317.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)

* 第三步:进入spiders目录下输入 scrapy genspider mainSpider "51job.com"
目录下创建一个名为mainSpider的爬虫，并指定爬取域的范围是"51job.com",当你敲的比较慢吧,给你1秒钟
进入目录看看里面现在有什么吧
![Snip20180323_17.png](https://upload-images.jianshu.io/upload_images/3258209-77ca70504acb31df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)

> start_urls = () ：爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。

> parse(self, response) ：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：

> 负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
生成需要下一页的URL请求。
* 第四步:我们现在分析一个51job的结构
下图是各个职位类型的入口
![image.png](https://upload-images.jianshu.io/upload_images/3258209-41e1808c1cca4e64.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)
这时候我们需要用到两个神器 chrome浏览器和XPath Helper插件,别说你没chrome,下载一个呗
不会正则和XPATH怎么爬呢,重点来了!!!!
右击![image.png](https://upload-images.jianshu.io/upload_images/3258209-ebcd6e3d775adf33.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)
打开XPath Helper插件
![image.png](https://upload-images.jianshu.io/upload_images/3258209-2b4959e47557144c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)
现在你的屏幕应该是这样的
![image.png](https://upload-images.jianshu.io/upload_images/3258209-eee300e43e6ba47a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000)
我们选择要爬取的连接
![image.png](https://upload-images.jianshu.io/upload_images/3258209-5895f405c3b91a35.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/800)
右击标签->copy->copy xpath,我们会得到一串神奇的字符
/html/body/div[5]/div[2]/div[1]/a[1]
![Snip20180323_31.png](https://upload-images.jianshu.io/upload_images/3258209-6874cb7180b121ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)
输入xpath 插件
![image.png](https://upload-images.jianshu.io/upload_images/3258209-7f9c1b96e4629e4f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)
很显然这不是我们想要的链接,介绍一个xpath语法,在后面加上/@xxx,就代表获取这个表情的xxx属性,我们试试
/html/body/div[5]/div[2]/div[1]/a[1]/@href
![image.png](https://upload-images.jianshu.io/upload_images/3258209-e005ccfa6a9eff01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)
ok这样就获取到了我们想要的链接,但是只有一条,再来说明一下xpath第二个重要的语法,//xxx代表获取这个层级下所有的xxx标签,我们继续改造
/html/body/div[5]/div[2]//div//a/@href
![image.png](https://upload-images.jianshu.io/upload_images/3258209-50059243613cf532.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)
搞定!
写行代码
```
def parse(self, response):
liststype = response.xpath('/html/body/div[5]/div[2]//div//a/@href')
for url in liststype:
print url.extract()
```
运行看看效果~~~~~ 兜兜转转介绍了很多基础知识 ~~~ 10分钟过去了
![Snip20180323_28.png](https://upload-images.jianshu.io/upload_images/3258209-866df8e93880e7e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)

* 第五步:殊途同归
//*[@id="resultList"]/div[4]/p/span/a/@href
同样道理改造一下
//*[@id="resultList"]//div/p/span/a/@href
![image.png](https://upload-images.jianshu.io/upload_images/3258209-921be69f952684f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/800)
除了内容我们还要获取一下页码的链接
//*[@id="resultList"]/div[55]/div/div/div/ul/li[3]/a
同样道理改造一下
//*[@id="resultList"]/div[55]/div/div/div/ul//li/a/@href
5分钟~~~ 瑟瑟发抖~~~
![image.png](https://upload-images.jianshu.io/upload_images/3258209-f5d4b257e3568794.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 第六步:终极对决
终于到了我们最后一关啦.额..最后一页
![image.png](https://upload-images.jianshu.io/upload_images/3258209-6673696548eb94fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
同样道理获取我们想要的信息,大家都很聪明应该能明白的~ 5分钟应该够了吧
职位名称 = '/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()'
地区 = '//span[@class="lname"]/text()'
薪资 = '/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()'
经验 = '/html/body/div[3]/div[2]/div[3]/div[1]/div/div/span[1]/text()'
雪咯 = '/html/body/div[3]/div[2]/div[3]/div[1]/div/div/span[2]/text()'
* 第⑦步:把代码补全
强行9分钟~~
```
def parse(self, response):
liststype = response.xpath('/html/body/div[5]/div[2]//div//a/@href')
for url in liststype:
yield scrapy.Request(url=url.extract(),callback=self.parseSearch)

pass
def parseSearch(self,response):
listsjob = response.xpath('//*[@id="resultList"]//div/p/span/a/@href')
listpages = response.xpath('//div[@class="p_in"]/ul/li/a/@href')
for page in listpages:
yield scrapy.Request(url=page.extract(),callback=self.parseSearch)
for url in listsjob:
yield scrapy.Request(url=url.extract(),callback=self.parseDesc)
pass

def parseDesc(self,response):
context= response.text
title = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()').extract()[0]
area = response.xpath('//span[@class="lname"]/text()').extract()[0]
money = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()').extract()[0]
exp = response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div/span[1]/text()').extract()[0]
study = response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div/span[2]/text()').extract()[0]
all = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()').extract()[0]
lists = all.replace(' ','').replace('\r','').replace('\t','').split('|')
company = lists[0]
people = lists[1]
type = lists[2]

print (title)
item = My51JobspiderItem()
item['title'] = title
item['area'] = area
item['money'] = money
item['company'] = company
item['people'] = people
item['type'] = type
item['study'] = study
item['exp'] = exp
yield item
pass
```
看看效果~~ good
![image.png](https://upload-images.jianshu.io/upload_images/3258209-9bd4f1ef2d592e0e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 总结:
娱乐贴~~ 给大家多一个无聊时的乐趣,xpath还是有很多语法需要学习,还有scrapy,有问题直接问,保证回答但是不许骂我,还有建议大家不要在繁忙时间随便爬,友好一点,凌晨两三点去偷偷的干
github地址:https://github.com/CZXBigBrother/51JobSpider
