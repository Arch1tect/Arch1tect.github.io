---
date: '2014-02-07 02:14:29'
title: "\u6A21\u4EFFGoogle Doc\u7684Mobile App"
---

移动端创业课的第一个练手的小project是做一个简单的Google Doc, 多人即时编辑文件的app.

留篇日志记一下。


[![Screenshot_2014-02-08-15-29-47](/content/images/uploads/2014/02/Screenshot_2014-02-08-15-29-47-576x1024.png)](/content/images/uploads/2014/02/Screenshot_2014-02-08-15-29-47.png)


[![Screenshot_2014-02-06-17-59-29](/content/images/uploads/2014/02/Screenshot_2014-02-06-17-59-29-576x1024.png)](/content/images/uploads/2014/02/Screenshot_2014-02-06-17-59-29.png)

用了 Google Protocol Buffer 这种格式来传输数据， 以前只用过xml 和 json, 这个据说快好多倍，不过我自己没有测试比较过。

我是这样设计的：每次传数据就是一个action类型，action内容和action位置。 所以如果我在编辑框的第12个字符的位置输入了一个apple, 那发送的包里面就是action type: insertion; action string: apple; action position: 12.  Google Doc的基本功能都能做到的，但仅限文字编辑。


