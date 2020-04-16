---
date: '2012-03-03 21:43:03'
title: "Intro to Box2dweb | Box2dweb\u7B80\u4ECB"
---

FYI: The notes for **Box2dweb** starts in my next article.

注：关于Box2dweb的学习笔记从下一篇博文开始，这篇只是介绍。

     While having my sweet spring break, I finally have time to write some notes for this great engine – Box2dweb. Box2d is quite famous and since it’s open source, it has been widely used in thousands of games, even if you have never heard about box2d, you must know that game that has been downloaded more than 350 million times with earnings exceed 80 million US dollars —– “Angry birds”. [Yes, it uses box2d.](http://www.geek.com/articles/mobile/box2d-creator-asks-rovio-for-angry-birds-credit-at-gdc-2011032/ "story behind angry birds ")  And once you understand box2d, you will realize there’s actually not much work left to make a game like “Angry birds”. (absolutely no offense to Angry birds team, I love your game : ) OK, I don’t want to talk too much about Box2d since [Wikipedia](http://en.wikipedia.org/wiki/Box2D "about box2d") can do a much better job than me.

**Box2dweb** is the latest javascript port of Box2d，the **advantage** of this port is you can well combine it with Html5 and make really neat game or whatever you want. And since it’s ported to javascript, it’s supported by most browsers if not all. So no matter windows or mac you are using, you can access your game through your browser and it will look no difference. Also because it’s totally written in javascript, you can use both iphone and ipad to open it while Apple has announced they won’t support flash which seems always crash but they love Html5…

    The “disadvantage” of Box2dweb is that there are not many tutorials about it which is quite frustrating when I was learning it. (most tutorials I found are either for C++ or flash port of box2d) Therefore I decide to make my study note more detailed and easy to understand for others, so that it might help someone who get interest into it like me . ^-^

<span style="text-align: left;">    Btw I just found my interest in these stuff recently and I’m a student who has taken zero courses about computer or computer language. So if you can kindly point out my mistake and maybe even take 3 minutes to explain it a little bit for me, </span>**you are very much appreciated! **

     Check out [the first game I made in my life with Box2d!](http://box2dweb.com/html5-game-box2dweb/ "HTML5 Game (Box2dweb)")

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

    美好的春假让我终于可以空出点时间来写 Box2dweb 的学习笔记 ^^ Box2d 是一个非常有名的开源2D物理引擎，成百上千的游戏都曾经或者正在使用它。即便你没有听说过 Box2d, 我想你一定知道那个下载次数超过3.5亿, 赚走了超过8千万美元的“愤怒的小鸟”。 是的，[愤怒的小鸟用的就是box2d物理引擎。](http://www.geek.com/articles/mobile/box2d-creator-asks-rovio-for-angry-birds-credit-at-gdc-2011032/ "愤怒的小鸟承认使用box2d物理引擎") 而一旦你明白 Box2d 可以做些什么，你就会发现写一个能赚取8千万的游戏并没有你想象中那么难（无意冒犯愤怒的小鸟的制作团队，我也很爱你们的游戏：）好啦， 我不想过多的介绍这个物理引擎的光辉历史了，[Wikipedia](http://en.wikipedia.org/wiki/Box2D "about box2d") 介绍的很详尽了，但百度百科的介绍（如果那真的是介绍的话）就太费解了 ＝ ＝

     至于 Box2dweb 呢，则是 Box2d 的最新 javascript 版，使用 javascript 版的优点主要在于你可以把它和来势汹汹的 html5 结合来做出很简洁的游戏或者什么有趣的应用，它完全不依赖flash。因为是使用浏览器来运行，你可以在任意操作系统下得到一致的效果。同样的你也可以使用 iphone、ipod、ipad 等来进行正常的访问。 苹果已经宣布不支持flash，对[html5](http://tech.163.com/11/0920/16/7EDK3QVS0009387E.html "html5 is the future")则是寄予厚望。。。

     遗憾的是，不像 flash或者 C＋＋ 版的 Box2d，关于 Box2dweb 的学习资料着实少之又少， 学起来耗时耗力（我自己是看着其它语言的教程，摸索的javascript 版 ⊙﹏⊙）因此， 我决定把这个学习笔记写得尽量详细一些，或许可以帮到像我一样突然对这个物理引擎产生兴趣的朋友 ^-^

     顺便一提，在下只是最近突然对html5、box2d等产生了浓厚兴趣，并无任何计算机编程方面的基础。所以文中难免错漏百出，看官您若不吝赐教，着实感激不禁！

     去看看我用Box2d写的[第一个游戏！](http://box2dweb.com/html5-game-box2dweb/ "HTML5 Game (Box2dweb)")


