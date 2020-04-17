---
date: "2014-03-07 22:20:17"
title: "Diffie Hellman\u7B97\u6CD5"
---

Diffie Hellman 算法要早于 RSA, 事实上它是最早的加密算法之一，而且据说启发了 RSA 等算法。

先提一个问题吧：

Alice 和 Bob 想有一个全世界只有他俩知道的小秘密，但是大坏蛋 Eve 从始至终一直监听他们之间说的每句话， 那么请问 Alice 和 Bob 还能通过传达消息来得到这个只有他俩知道的小秘密么？

[![problem](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2014/03/problem.gif)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2014/03/problem.gif)

在知道 Diffie Hellman 算法前，我以为这是不可能的，因为 Eve 除了本身不能发布信息，A 和 B 之间的所有信息他全部都能窃听的到。

而正确答案则是可以，具体如下：

首先 Alice 或者 Bob 选两个数字 g 和 p, 比如 g = 3, p = 11.  （p 一定要是质数）

然后 Alice 随便想一个数字 x 并且不告诉任何人，比如 x = 5; 同样的 Bob 随便想一个数字 y 不告诉任何人，比如 y = 7.

Alice 加密数字 x ，用 g^x(mod 11) 这个公式 , 带入数字可以得到： 3^5 % 11  =   1

相似的， Bob 加密 y, 得到 3^7 % 11 =  9

好了，Alice 和 Bob 现在交换刚刚加密后的信息， Bob 接收到 Alice 发的加密后的数字 1, Alice 接收到 Bob 发的加密后的数字 9. 邪恶的 Eve 此时也得到了这两个数字。

Alice 解密 Bob 发的数字 9, 9^5 % 11 = 1

Bob 解密 Alice 发的数字 1, 1^7 % 11 = 1

好了，此时 Alice 和 Bob 之间成功有了这个共享的小秘密，也就是数字 1

我们反观坏人 Eva， 他知道 g = 3, p =11， 他也知道 Alice 和 Bob 交换了数字 9 和数字 1, 但因为他不知道 x 和 y, 所以便无法得到秘密数字 1。

————————————————————————————————————————–

**Ephemeral**是这种算法的一大特点，不像 RSA 丢失了 private key 就彻底暴漏， Diffie-Hellman 算法每次对话都可以换 x 和 y 的值， 只要确保信息确实是由 Alice 和 Bob 发出而不是第三个人发出的就没有问题。不过它和 RSA 本来应用的环境也不同。

下面这个帖子有比较 RSA 和 DHP 的特点和应用：

[http://security.stackexchange.com/questions/35471/is-there-any-particular-reason-to-use-diffie-hellman-over-rsa-for-key-exchange](http://security.stackexchange.com/questions/35471/is-there-any-particular-reason-to-use-diffie-hellman-over-rsa-for-key-exchange)
