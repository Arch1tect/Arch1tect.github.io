---
date: '2015-12-07 05:41:00'
title: "Ghost\u52A0\u5165Swiftype\u641C\u7D22\u529F\u80FD"
---
Ghost原生的搜索功能不知道何时才能出现，终于今天决定加入第三方的搜索功能。我没有用Google Custom Search因为国内屏蔽Google，最后选择了用Swiftype的免费服务。

安装过程非常简单，Swiftype的网站上有简明的介绍，我就不赘述了。新的搜索框被我放在了tag cloud之中，看起来还挺和谐。

![](/content/images/2015/12/Screenshot--7-.png)


装完以后我发现Swiftype缓存了我博客的所有页面，包括`/page/`,`/tag/`,`/author/`等页面和分页页面。这样带来的问题就是当我搜索关键字的时候，如果关键字出现在了文章节选里，那么它就也会出现在上面提到的那些目录页面里，从而造成搜索结果里包含分页页面。解决办法很简单，只要在缓存结果中去掉上面三个路径即可。这样搜索的结果就只含有具体文章页面了。

该设置的位于Swiftype网站的Manage->Domain->Manage Rules页面的*Pages matching any of these rules will be excluded*这句话下面。