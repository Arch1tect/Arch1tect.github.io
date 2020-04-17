---
date: "2015-12-07 05:41:00"
title: "Ghost\u52A0\u5165Swiftype\u641C\u7D22\u529F\u80FD"
---

Ghost 原生的搜索功能不知道何时才能出现，终于今天决定加入第三方的搜索功能。我没有用 Google Custom Search 因为国内屏蔽 Google，最后选择了用 Swiftype 的免费服务。

安装过程非常简单，Swiftype 的网站上有简明的介绍，我就不赘述了。新的搜索框被我放在了 tag cloud 之中，看起来还挺和谐。

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/2015/12/Screenshot--7-.png)

装完以后我发现 Swiftype 缓存了我博客的所有页面，包括`/page/`,`/tag/`,`/author/`等页面和分页页面。这样带来的问题就是当我搜索关键字的时候，如果关键字出现在了文章节选里，那么它就也会出现在上面提到的那些目录页面里，从而造成搜索结果里包含分页页面。解决办法很简单，只要在缓存结果中去掉上面三个路径即可。这样搜索的结果就只含有具体文章页面了。

该设置的位于 Swiftype 网站的 Manage->Domain->Manage Rules 页面的*Pages matching any of these rules will be excluded*这句话下面。
