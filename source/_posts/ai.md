---
date: "2012-12-22 05:19:29"
title: "\u673A\u5668\u4EBA\u7248\u4E00\u5361\u7267\u5E08\u59B9\uFF08AIML & Program-O\uFF09"
category: project
---

最近一个星期在研究人工智能，或者应该叫 NLP（Natural Language Processing）自然语言处理，因为它与真正的“智能”距离还很远。

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/88d16d81800a19d808aa05d733fa828ba71e4621.png)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/62f958ee3d6d55fb8f29f7f46d224f4a22a4dde7.png)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/dancer.png)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/chinese.png)

吹牛，其实是一点中文也看不懂。。。

除了基本的对话外，还可以播放英语，搜索图片，带你环游世界等等，关键词分别为“play music”, “search XXX” 与 “take me to XXX” 。

(推荐 Chrome…)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/Screen-Shot-2012-12-22-at-4.54.45-AM.png)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/Screen-Shot-2012-12-25-at-1.17.15-AM.png)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/hongkong.png)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/tokyo.png)

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/mars.png)

说脏话会被喷一脸墨水，请自重！

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/12/b86d9345d688d43f504710207d1ed21b0cf43be0.png)

————————————-AIML 与 Program O———————————————-

—————————————————————————————————————————————–

这个机器人主要由 AIML 与 Program-O  两部分组成了它的灵与肉。 首先让我们看它的灵魂—–AIML。

AIML 的全称是  **[Artificial Intelligence](http://en.wikipedia.org/wiki/Artificial_intelligence "Artificial intelligence") Markup Language**, 它是这个机器人“理解”人类的语言并做出回应的核心部分。其最基本的单位为 category, 里面包含了`<pattern>` 和 `<template>`两个元素，分别对应用户的输入和机器人的输出，具体结构如下：

`<category> <pattern>WHAT IS YOUR NAME</pattern> <template>My name is John.</template> </category>`

AIML 理解人类输入的句子的方法叫做 “pattern matching,”   字面意思就解释了它的原理。以上方这个 category 为例，当人类输入“what is your name”（不区分大小写）后， 因为与“WHAT IS YOUR NAME”这个 pattern 相符合，因此机器人给出的回答便是“My name is John.”

这看起来似乎与智能沾不上边，然而 AIML 就是在这个不能再简单的结构的基础之上加以辅助用的几个标签，成功的理解了无数复杂难懂的句子，三次赢得**[Loebner Prize](http://en.wikipedia.org/wiki/Loebner_Prize "Loebner Prize")大奖，并在 2004 年的**Chatterbox Challenge 上取得了冠军桂冠。\*\*\*\*

下面我具体介绍两个很有用的标签：<that>和<srai>， 大家可以从中一窥机器人是如何通过 AIML 进行“思考”的。

————————–`<that>` 标签介绍开始  ————————————————–

`<that>`标签中的 that 指代的就是机器人说的上一句话。

请看下面的人机对话，分析机器人最后一句：

机器人：“Do you like movies?”

人类：“Yes.”

机器人：“What’s your favorite movie?”

上面这个对话是这样实现的:

机器人首先通过 pattern matching， 匹配到了“YES” 但是机器人的数据库中对应“YES”的回答必然非常多，比方有下面 A 和 B 两个 categories。于是机器人便去匹配 that 标签，也就是机器人自己上句说过的话，即“Do you like movies?” 这样它就可以确定应该匹配 category A 了，最后给出正确的回应“ What’s your favorite movie?”

`<category A> <pattern>YES</pattern> <that> DO YOU LIKE MOVIES </that> <template> What's your favorite movie? </template> </category> <category B> <pattern>YES</pattern> <that> DO YOU LIKE BOOKS </that> <template> What's your favorite book? </template> </category>`

————————–`<srai>` 标签介绍开始  ————————————————–

`<srai>`标签中的 srai 有很多种解释：“Symbolic Reduction Artificial Intelligence”, “Syntactic Rewrite AI”, “Simple Recursive AI”, “Stimulus-Response AI” 其实它的意思也很简单，就是将`<srai>`标签中的内容重新交给机器人去分析, 因此它被放在`<template>`内。

我想了一个同时结合`<srai>`和`<that>`两个标签的例子，请看下面对话，分析机器人最后一句：

人类：“My girlfriend just broke up with me, and I always thought we could last forever! Now I’m feeling so miserable!”

机器人：“I understand.”

人类：“No！” （人类不信机器人能理解失恋之苦- -|||）

机器人：“I understand it very well, Because I’m very intelligent like you.”

上面这个对话是这样实现的:

机器人首先通过 pattern matching， 匹配到了“NO” 然后像上个例子介绍的那样，通过<that>标签，机器人正确的找到了下方的 category A 了，而 category A 给出的回应是`<srai>YOU DO NOT UNDERSTAND</srai>`。 看到了`<srai>`标签后机器人“明白”它的思考过程还没有结束，而它下一步要做的便是将`<srai>`标签里的“YOU DO NOT UNDERSTAND”当做用户的输入，重新在数据库内进行新的一轮 pattern matching。

而第二轮的 pattern matching 和 category B 成功匹配（这里我们假设数据库里没有其它相同的 pattern 存在了），于是机器人最后输出“I understand it very well, Because I’m very intelligent like you.”   成功！

`<category A> <pattern>NO</pattern> <that>I UNDERSTAND</that> <template> <srai>YOU DO NOT UNDERSTAND</srai> </template> </category> <category B> <pattern>YOU DO NOT UNDERSTAND</pattern> <template>I understand it very well, Because I'm very intelligent like you. </template> </category>`

————————–`<srai>` 标签介绍结束 ————————————————–

注：这里我只是简单介绍，实际上 AIML 还有打分系统，会在候选的回应中选出得分最高的来回应。

另外通过 AIML，机器人可以暂时或永久的记忆人类提供的个人信息，比如名字、职业、性别等，还可以学习新的知识（本人尚未了解）。

我很喜欢 AIML 通过递归一层层的简化问题，一步一步的“理解”问题，最后得出回应的这个过程，也正因为如此所以想要更深入的去了解它。

———————————————————————————————————————————-

AIML 就先介绍到这里了，接下来是机器人的肉—-Program-O

Program-O 是 AIML 的一种  interpreter，还有很多种：

-   [Program D](http://aitools.org/programd) (Java, J2EE)
-   [Program Q](http://sourceforge.net/projects/qaiml) (C++, Qt)
-   [Program W](http://programw.sourceforge.net/) (Java)
-   [CHAT4D](http://www.toolbox.free.fr/TB/Chat4D.html) edit and run (delphi) (French)
-   [Program O](http://www.program-o.com/) (PHP/MySQL)
-   [Program E](http://sourceforge.net/projects/programe/) (PHP)
-   [Program N](http://www.aimlpad.com/) Program N is no longer available
-   [Program P](http://www.sweb.cz/alicebot/) (Pascal)
-   [Program V](http://www.virtualitas.net/perl/aiml/) (Perl)
-   [Program Y/PyAIML](http://pyaiml.sourceforge.net/) (Python)
-   [Program R](http://aiml-programr.rubyforge.org/) (Ruby)

它们由不同的语言编写，而我选择 Program-O 是因为它方便在我的服务器上运行。

Interpreter 和 AIML 的关系在我看来就像磁带和录音机，而录音机（Program-O）的用处就是播放磁带(AIML)。

比较遗憾的是 Program-O 本身还有一些 bug，我放在网上的这个机器人就经常因此而输出错误，在 debug log 里可以看到明明 AIML 已经得到了正确回应，到了最后一步要 Program-O 进行输出的时候却发生了错误。。。于是机器人总是说“I can’t understand what you are saying > <” 。。。 我在 Debug 时发现是 php 一个 eval function 的问题，但还一直没有解决。。。

另外 Program-O 的官方支持也比较欠缺，官网上找不到 documentation, 官方论坛的人也寥寥无几，我一周前注册了，现在账号仍未被激活。

不过还是要感谢作者开发这个 interpreter~

安装过程很简单，下载程序与 AIML 后上传到自己的服务器上，然后自然可以看到安装指引。

Program-O 下载地址： [http://github.com/Program-O/Program-O/archive/master.zip](http://github.com/Program-O/Program-O/archive/master.zip)

AIML 库下载地址： [http://code.google.com/p/aiml-en-us-foundation-alice/](http://code.google.com/p/aiml-en-us-foundation-alice/)         推荐下载第一个“Foundation A.L.I.C.E. Bot”

Anyway, 如果你看完觉得感兴趣，也打算用 AIML 做一个机器人，欢迎进这个刚建好的 QQ 群交流：288261890

参考资料：

[http://www.alicebot.org/documentation/aiml-reference.html ](http://www.alicebot.org/documentation/aiml-reference.html)

[http://en.wikipedia.org/wiki/AIML](http://en.wikipedia.org/wiki/AIML)
