---
date: "2012-12-06 23:43:31"
title:
    "\u5982\u4F55\u89E3\u51B3\u8BC4\u8BBA\u88AB\u8BEF\u5224\u4E3A\u5783\u573E\u8BC4\
    \u8BBA(Wordpress Akismet)"
---

WordPress 用户中不少都开启了 Akismet 插件，然而该插件有时候会误判，甚至有时候会将你的正常网站列入 spammer 名单里。这样无论你的评论内容是什么，只要填入了自己的网站地址，就会被 Akismet 直接送进垃圾箱。本文简单介绍解决方法。

**如何得知评论被判断为垃圾评论？**

评论后刷新页面，既没有显示出你的评论，也没有“您的评论正在等待审核” (Your comment is awaiting moderation) 的提示。 这时候，你的评论多半已经直接进了垃圾箱。

**如何确定自己的网站误入 Akismet 的 spammer 名单？**

如果评论被吞的情况经常发生，并且你在尝试了不输入网站地址或输入其他网站地址后，发现评论能正常显示或有被审核的提示，那么你的网站地址多半已经被 Akismet 误放进了 spmmer 名单里。

**解决办法：**

1. 打开下面网址：

[http://akismet.com/contact/](http://akismet.com/contact/)

2. 在 search 框里随便输入什么，比如‘mistake’， 然后点 search.

3. 下面的表单会出现（点击放大）：

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/Screen-Shot-2012-12-06-at-11.38.09-PM.png)

填写表单，记得要勾选“<label for="fp">I think Akismet is catching my comments by mistake</label>”。

4. 最后点击 Submit 提交表单即可。

三个小时内应该可以得到回复，个人经验。

完。

Happy blogging guys： ）
