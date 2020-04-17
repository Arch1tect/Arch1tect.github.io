---
date: "2014-03-07 05:55:51"
title: "RSA\u7B97\u6CD5"
---

今天复习密码学看到了 RSA 的部分，我无意搜到了几篇阮一峰前辈的相关博文，发现大神文笔真是好，写什么都能写的特别清楚明白，完整可靠。我把三篇博文链接贴在这里，以后再复习也许会用到。（我最早知道他是看了他翻译的 Paul Graham 的文集《黑客与画家》）

————————————–阮一峰日志—————————————————————

#### 密码学笔记

[http://www.ruanyifeng.com/blog/2006/12/notes_on_cryptography.html](http://www.ruanyifeng.com/blog/2006/12/notes_on_cryptography.html)

#### RSA 算法原理（一）

[http://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html](http://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html)

#### RSA 算法原理（二）

[http://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html](http://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html)

—————————————————————————————————–

###### 我之前的误解

我之前学的时候知道 RSA 安全的关键是已知公匙 e， 要计算私匙 d 难度巨大，d 通过下面的公式计算

ed ≡ 1 (mod φ(n))

这个等价于求下面方程 x,y 的整数解

ex + φ(n)y = 1

但我搞错了一点，我以为计算 ex + by = 1 是困难所在， 事实上该方程只要 log(n)的时间就可以解出来，用辗转相除法即可。而真正的难处还是在计算 φ(n)这儿。**n = pq**, 最初制造公钥私钥的人知道 p 和 q, 所以可以轻易的用 φ(n) =（p-1）(q-1)计算，而外人不知道 p,q 是多少， 就只看到一个巨大的 n(一般是 1024 位二进制的大数)， 想要因式分解则难上加难。算不出 φ(n)，便也算不出私钥是多少了。

————————————–小例子————————————————————–

看完了阮大神的文章可以试试解我下面这个简单的秘密～

[![Letters-and-number-code](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2014/03/Letters-and-number-code.jpg)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2014/03/Letters-and-number-code.jpg)

首先让字母对应数字， A-1 B-2 C-3 D-4 …. Z-26

用公钥加密后的信息： 17  67  59  59  69

公钥： {23, 77}  （公钥是加密用的，解密者不需要知道）

私钥： {47, 77}

解密后的信息： ？？？？？

这个密匙长度只有 7 位（2^7 = 128, 77 < 128），所以我们完全可以脑算破解之，但是我刚刚提到过一般 RSA 的密匙长度有 1024 位甚至 2048 位那么大。O(∩_∩)O

###### 简单示范一下怎么破解私钥：

**φ(n) = φ(77) = φ(7×11) = φ(7) x φ(11) = 6 x 10 = 60    （关键步骤）**

根据

ed ≡ 1 (mod φ(n))

得到

ed ≡ 1 (mod 60)

即

23x + 60y = 1

已知 x,y 皆为整数，用辗转相除法很快可以求得一对解：  
 x = -13, y = 5  
 x 即为前面式子里的 d 也就是私钥，我们知道 x 是相对于 60 循环的，所以{-13, 77}， {47， 77},  {107， 77}， {167， 77}   等等都是对的私钥，我们用哪个去解密都没问题。

小结： 我们之所以能成功破解在于看出了 n = 77 = 7 \* 11, 而对于十分巨大的数字，这个步骤就非常难，需要计算机算个好几百年了。

路过有兴趣的朋友把原信息算出来留言我吧！是五个字母的英文单词哦～
