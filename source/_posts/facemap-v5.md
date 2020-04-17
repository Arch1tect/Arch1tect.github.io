---
date: "2013-06-18 03:11:14"
title: FaceMap V5
---

写安卓应用近来占用了我每天的绝大多数时间，回头看看，接触安卓开发竟然已经一个月有余了。其中专心学习官网教程大概只有第一个礼拜，后面就全是围绕具体的一个个 project 来学习用到的模块，虽然这样学很不系统，但乐趣亦无穷。

而最近的半个多月在做的这个 project 涉及到的则不仅限于安卓了。大概刚好三分之一安卓，三分之一 Google Map API,   还有三分之一的服务器端（php+sql）!   还有十分之一是 P 图其实，加起来就不等于一怎么样 ╮(╯_╰)╭

总的来说我非常享受该 project, 既喜欢项目本身的概念，也喜欢这个设计与实现的过程，同时也因为有三个方面的程序要写，让我能持续有新鲜感~

Project 取名叫 FaceMap （暂定）， [初衷其实是记录人的运动轨迹](http://swotong.com/three-weeks-is-updated-once-a-real-man/)，侧重于大量收集数据来做好看的 data visualization, 然后听了 TY 的建议想再加入收藏地点的功能, 当然还有我一直最感兴趣的社交功能。 但是后来做的时候我逐渐意识到记录运动轨迹早有一些专业团队做了，而且我所希望做到的记录日常详尽轨迹的想法，实现起来有大量消耗用户的电量和流量等弊端。至于记录地点的功能，Google， 百度地图本身就提供了这个功能，而且它们和自己的社交平台已经有了很好的联系。 加上我势单力薄，功能越多，对我就越不利， 于是我有了做减法的想法， 整个 app 最好全是 UGC, 不用我发布任何实际的内容，所以现在的核心功能自然就在社交上了，特色则是地图与人物形象的结合。

（又想起了建筑设计，两者都是不断 back and forth, 有时直接把概念换掉。 但换掉并不等于重来，每次的 research 都是可以积累的。。）

人类是视觉动物，千言万语难敌一张 JPEG，不想写了，传截图。。

[![conversation](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/conversation-200x300.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/conversation.png)

尝试中我情不自禁地把一些喜欢的动漫角色加了进去。

[![device-2013-06-16-080506](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-16-080506-200x300.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-16-080506.png)

然后瞬间觉得这个 app 有爱了 – -。。。

[![device-2013-06-16-075039](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-16-075039-300x200.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-16-075039.png)

现实与梦幻的界限渐渐模糊了的感觉。。。

[![device-2013-06-17-132255](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-17-132255-200x300.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-17-132255.png)

人物的 Avatar 在街景里也能看到，下图藏了“胸针”~

[![Screen Shot 2013-06-18 at 1.42.23 AM](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/Screen-Shot-2013-06-18-at-1.42.23-AM-300x177.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/Screen-Shot-2013-06-18-at-1.42.23-AM.png)

为了方便 Debug, 我加了个显示进程用的功能，既容易发现问题，用户也可以看到数据传输的动态，自行控制。

[![processing](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/processing-200x300.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/processing.png) [  
![show_process](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/show_process-200x300.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/show_process.png)

<span style="text-decoration: underline;">  
</span>  [  
](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/show_process.png)

按钮在 V5.0 里都换了风格，不会这么吓人了。。。但我懒得截新图了。

下回再写，困死 T^T
