---
date: '2014-03-07 04:26:44'
title: "Ubuntu13.10\u901A\u8FC7profile\u6587\u4EF6\u4FEE\u6539PATH"
---

装了数学软件sage, 在下载文件夹里，每次想打开得cd到这个文件夹里然后 ./sage 来运行，很麻烦。

用terminal直接打开程序非常方便，而可以打开的程序的路径都被保存在了的$PATH这个变量里面，于是我查了一下怎么修改$PATH, 命令如下：

`export PATH=$PATH:/your/target/dir`

可以直接打在terminal里，但这样就只在该terminal运行时的session里有效。

所以这个命令需要存在一个固定的文件里，让系统每次打开都会自动运行。

Ta-dah! 它就是/etc/profile 文件了，我们只要把上面这行加进去就改好了。 注意这个是只读文件，一定要sudo vi 或者 sudo gedit之类的才能编辑哦！

比如

`sudo gedit ~/.profile`

 

好了，现在在terminal里打sage就像打python一样可以直接启动这个程序了：）

 

（这个profile文件是面向整个系统的，如果是针对特别用户的Path修改，则在另一个文件，或者用另外的办法。）


