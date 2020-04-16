---
date: '2014-03-07 22:20:17'
title: "Diffie Hellman\u7B97\u6CD5"
---

Diffie Hellman算法要早于RSA, 事实上它是最早的加密算法之一，而且据说启发了RSA等算法。

先提一个问题吧：

Alice 和 Bob 想有一个全世界只有他俩知道的小秘密，但是大坏蛋Eve从始至终一直监听他们之间说的每句话， 那么请问Alice 和 Bob 还能通过传达消息来得到这个只有他俩知道的小秘密么？

[![problem](/content/images/uploads/2014/03/problem.gif)](/content/images/uploads/2014/03/problem.gif)

 

在知道Diffie Hellman算法前，我以为这是不可能的，因为Eve除了本身不能发布信息，A和B之间的所有信息他全部都能窃听的到。

而正确答案则是可以，具体如下：

首先Alice或者Bob选两个数字g和p, 比如 g = 3, p = 11.  （p一定要是质数）

然后Alice随便想一个数字x并且不告诉任何人，比如x = 5; 同样的Bob随便想一个数字y不告诉任何人，比如y = 7.

Alice 加密数字 x ，用 g^x(mod 11) 这个公式 , 带入数字可以得到： 3^5 % 11  =   1

相似的， Bob 加密 y, 得到 3^7 % 11 =  9

好了，Alice 和 Bob 现在交换刚刚加密后的信息， Bob 接收到Alice发的加密后的数字1, Alice接收到Bob发的加密后的数字9. 邪恶的Eve此时也得到了这两个数字。

Alice 解密Bob发的数字9, 9^5 % 11 = 1

Bob 解密Alice发的数字1, 1^7 % 11 = 1

好了，此时Alice和Bob之间成功有了这个共享的小秘密，也就是数字1

我们反观坏人Eva， 他知道 g = 3, p =11， 他也知道Alice 和 Bob交换了数字9 和数字1, 但因为他不知道x 和 y, 所以便无法得到秘密数字1。

————————————————————————————————————————–

**Ephemeral**是这种算法的一大特点，不像RSA丢失了private key就彻底暴漏， Diffie-Hellman算法每次对话都可以换x和y的值， 只要确保信息确实是由Alice和Bob发出而不是第三个人发出的就没有问题。不过它和RSA本来应用的环境也不同。

下面这个帖子有比较RSA和DHP的特点和应用：

[http://security.stackexchange.com/questions/35471/is-there-any-particular-reason-to-use-diffie-hellman-over-rsa-for-key-exchange](http://security.stackexchange.com/questions/35471/is-there-any-particular-reason-to-use-diffie-hellman-over-rsa-for-key-exchange)

 


