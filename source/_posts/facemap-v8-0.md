---
date: "2013-06-23 00:32:40"
index_img: https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-22-204230.png
title: FaceMap v8.0
category: project
---

周一期末考，加上近期用眼过度，我决定暂停两天左右的 FaceMap 应用开发。刚好基本功能已经完成的七七八八了。

FaceMap  的开发总是伴着时刻不停的 StackOverflow 查询，因为感觉基本上什么都不懂 ╮(╯_╰)╭, 而编这样的实际程序和上学期算法课的 project 又大不相同，感觉基本上没有用到算法，偶尔有点小设计。。。

这周终于完成了私信功能。我打算再继续增加功能前先好好整理一下，既要解决兼容性的问题，也要把现在写好的代码块打扫干净，比如统一一下命名方式，去掉没有必要的重复代码，优化一下每次数据传输的大小等等，也方便后面继续扩展。

照例先上图记录一下变化。

菜单、按钮全部透明化：

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-22-203208.png)

增加了选择某用户后的弹出菜单。

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-22-202755.png)

选择发送私信给用户：

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-22-202814.png)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-22-204230.png)

私信目前我只是设置了收件箱和发件箱而已：

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/device-2013-06-22-205838.png)

今天早上想加入 AI 聊天系统，需要 hack 一下 program-o，因为 program-o 是给每个对话的用户都存档，虽然这样机器人可以通过查找上文语境给出更恰当的回答，但在这个应用里保存每个用户的对话内容则完全没有必要了，占用空间也影响速度。 我忙了几个小时没弄出个所以然，加上我很快意识到我当前的 priority 应该是确保基本功能不出问题，这个既不属于基本功能，也还没想清楚要怎么利用，于是作罢。

（另外 program-o 出了支持中文的新版本，但目前我没看到有中文的 AIML 库，英文版的之所以让人感觉还比较“智能”，官方提供的四万条目的 AIML 库功不可没。）

**下一步？**

因为放了许多二次元动漫人物，看起来越发像游戏了的感觉。我甚至想起了我最早玩的也是唯一玩过的网游 – 石器时代。

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/F201012030828432254610002.jpg)

呵呵，谁知道呢。。。把 idea 先记下来边走边看好了 ╮(╯_╰)╭

**兼容问题**

安卓程序开发还挺顺利的感觉，没开发过别的所以也没办法比较，不过兼容性实在令人头疼。 我手机的安卓版本是 4.04 版，我知道最新的是 4.2， 加上我的手机才 40 刀，所以我一直以为我这部的配置是最低最落伍的。结果我发现原来现在还有很大一部分人用的是 2.0 几的版本。也因此，有些代码在我的机子里可以运行，到了用户手上就各种出错 T^T。。 接下来几天都要用来调整兼容性了。

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/Screen-Shot-2013-06-22-at-11.02.49-PM.png)

举个例子 getActionBar()这个 method 安卓 API 低于 11 的系统就没有，所以 TY 下载了我的程序后一打开就直接退出了 （我当时听到他说打开就 crash 那刻简直心如死灰，本来自信满满的）QAQ   但这个问题很快就解决了，这还要归功于 google play developer console, 用户在程序异常退出后可以选按提交报告，TY 提交 1 秒后我就收到了所有需要的信息，从而顺利解决了这个问题。

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/Screen-Shot-2013-06-22-at-11.12.33-PM.png)
