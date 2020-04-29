---
date: "2013-06-04 04:33:32"
index_img: https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-04-235513.png
title: FaceMap
category: project
---

安卓开发这个最近每天的主要活动进展的还是比较顺利的，看了一些基础的官方文档之后，我就不耐烦的开始写具体的小程序了。 目前比较完整的程序一个是跨浏览器和手机通用的[聊天室](https://play.google.com/store/apps/details?id=com.swotong.simplechat)（主要为了学习安卓的网络相关模块），另一个则是 FaceMap（目前打算长期开发这个）。 其实这之前还想写写小游戏的，因为一直很喜欢物理引擎什么的。奈何一时找不到顺手的游戏引擎，unity3D 应该比较好，可是对我目前来说太专业了，而且想先从简洁点的 2D game 入手。 试了试 Cocos-X, 我感觉虽然 Cocos 的 iphone 游戏引擎做的很好，但是安卓的好像还比较难上手，配置的步骤就好多。。 最后决定用一个叫 AndEngine 的引擎了，因为看到一套 Tutorial 还挺好的，不过 Tutorial 还没出完。所以。。。就暂时不写游戏啦~

**Mobile App: FaceMap**

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/unnamed-2.png)

（暂时想了这么个毫无创意的名字。。╮(╯_╰)╭）

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/Screen-Shot-2013-06-09-at-12.44.48-AM.png)

安卓应用地址：[https://play.google.com/store/apps/details?id=com.swotong.googlemaplayer](https://play.google.com/store/apps/details?id=com.swotong.googlemaplayer "faceMap")

网页体验版地址：[ http://szblogger.com/googleMap/map_view.php](http://szblogger.com/googleMap/map_view.php "web version")

<span style="color: #ff0000;">（安卓版的手机上必须下载 google play services;  网页版无需手机，点最下面那行字里的“here”, 然后同意浏览器获取位置就可以用了~）</span>

这个就是我几天一直在写的应用了，最开始想做的这个应用主要是要每天收集用户走过的路线，然后可能一年、十年后，用户可以 plot 出这些“岁月的痕迹”，看看自己这些年都走过哪些地方。 但是和一般的 “where I’ve been” 那种图不同，我想做的应用是更重视一条条的线路而不只是点。 于是一个在一座城市里工作了十多年的人 plot 出来的图，会清楚的看到一条连接着家和办公地点的线，如果 zoom in，他/她会看到自己每天中午和同事们去到哪些饭店吃饭，晚上去哪里放松（或者是直接回家）。 他/她可以看到每周末自己喜欢去哪里休闲，每逢放假会去哪里游玩，等等等等……

我一直觉得这会是一张既好看又有意义且信息量爆棚的图，因为每一次的 zoom in, 都可以发现新的细节，于是人的记忆便也随之被唤醒。。。大概这也可以算是数据可视化的魅力吧。

（突然发现这和我做建筑设计时总喜欢先在脑海中 picture 最终效果的样子，然后以此为目标来设计的习惯不谋而合了。。）

不过等真的开始写我意识到了一些实际问题，比方一般人不会愿意总是开着这样耗流量和电量的程序，而且如果开着程序的话，不做点儿什么好像有点浪费？。。。于是，SNS 方面的功能便被我加了进去，目前还只是发状态，未来私信、传照片什么的自然是必不可少的了。 （我发现写这个 app, 刚好可以学习和实践各种数据传输方面的知识~）

![hi](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/Screen-Shot-2013-06-08-at-4.28.37-AM.png)

（上图是网页版的，不用手机也可以试试哦~）

比较遗憾的发现 Google Map 在国内好多功能没有，而且图片清晰度太让人失望了。。。

再放几张用这个 App 记录路径的截图吧：

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-04-235357.png)

![device-2013-06-04-235419](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-04-235419.png)

![device-2013-06-05-000105](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-05-000105.png)

![device-2013-06-04-235513](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-04-235513.png)

我开始看到第三张觉得挺奇怪的，自己的路线这么蜿蜒曲折，然后调出卫星图才发现原来是沿着树林走的，有的时候看到松鼠，我也会走过去逗逗。写这个的时候经常找朋友帮忙测试，这里要多谢各位~（后面还有无尽的测试呢 ╮(╯_╰)╭）

P.S.

对了，如果有朋友对这个 app 感兴趣的话, 欢迎找我一起开发。
