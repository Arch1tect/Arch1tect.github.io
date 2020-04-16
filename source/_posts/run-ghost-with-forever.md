---
date: '2015-10-24 22:17:25'
title: "\u8FD0\u884CGhost\uFF08Forever\uFF09"
---
接下来继续编辑config.js，将端口从2368改成80，并且将url改成服务器的地址。

因为AWS EC2每次重启都会重新分配IP，我申请了Elastic IP并绑定到了当前instance上。

如果仍然用下面的命令去运行Ghost，当前用户一旦关掉连接，这个Process也会停止。

`$ npm start --production`

<b>Forever comes for rescue!</b>

用Forever这个程序去运行Ghost就可以解决这个问题了:

安装Forever：`$ npm install -g forever`

运行Forever并将log存入文件ghost_forever.log方便日后查询

 `$ forever -l /var/www/ghost/ghost_forever.log start index.js`

停止运行 `$ forever stop index.js`

我需要在命令前加sudo否则会报错，估计是因为要listen port 80需要root权限。

用`$ sudo forever list`可以看到正在运行的任务，任务的log文件存放位置，还有任务的pid和uptime等等，非常方便。

---
值得注意的是Ghost运行分为Production和Development两种模式，默认模式为Development，所以上面用forever启动的是Development模式。Ghost的数据库相对应的也有两个：ghost.db与ghost-dev.db，所以在Dev模式下添加的文章都会进入到ghost-dev.db这个数据库文件里。