---
date: "2019-09-28 20:33:13"
title: "\u5F00\u6E90\u4E00\u53F6\uFF01"
---

<p>最近终于把一叶开源了，这个项目也陆陆续续做了几年了，不过多介绍了，官网网站有介绍。</p><p><a href="https://yiyechat.com">https://yiyechat.com</a></p><!--kg-card-begin: image--><figure class="kg-card kg-image-card"><img width="300px" src="https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/2019/09/sunday-morning-1.png" class="kg-image"></figure><!--kg-card-end: image--><!--kg-card-begin: markdown--><h3 id="">为什么开源？</h3>
<p>自己长期个人维护这个项目也是有些疲惫，而且希望能多听取一下别人的意见，这样进步的也更快一些。</p>
<p>而且和写代码相比，更头疼的还是功能的取舍，怎样设计合理。如果对设计不自信的话，便完全没有动力去写代码实现功能，因为很有可能是白费功夫。</p>
<!--kg-card-end: markdown--><!--kg-card-begin: hr--><hr><!--kg-card-end: hr--><h2 id="b2b-vs-b2c">B2B vs B2C</h2><!--kg-card-begin: markdown--><p>我最近把重心重新放在了支持站长的使用，浏览器拓展在国内的市场比较小，用的人很少，推广工作进行起来很困难。如果一些网站本身就有了一定的流量，然后装上一叶，那么可能效果会好很多，因为用户不用额外装什么软件，只要打开常去的网站，就会发现突然多了聊天的功能，看到右下角的数字知道有多少其他游客在线，或者看到飘过的弹幕后决定一起聊天。</p>
<p>站长如果要自己增加留言和实时聊天的功能，还需要一定的开发和维护的成本，一叶的引入则简单得多，站长只需要引入两行代码：</p>
<pre><code>&lt;link href=&quot;https://yiyechat.com/open-source/build/content-static/css/main.css&quot; rel=&quot;stylesheet&quot;&gt;
									
&lt;script src=&quot;https://yiyechat.com/open-source/build/content-static/js/main.js&quot; &gt;&lt;/script&gt;
</code></pre>
<p>完成。</p>
<p>站长也可以进行各种设置，通过在自己的网站定义一个spConfig对象，如下所示：</p>
<pre><code>window.spConfig = {
	tabList:['discover','chat','comment','profile','close'], 
	defaultTab: 'chat',
	chatModes:['room','site','page']
}
</code></pre>
<p>如果还有其他需求，自己修改对应的源代码也很容易，后端可以直接托管，也可以运行在自己的服务器上。</p>
<!--kg-card-end: markdown--><p></p>
