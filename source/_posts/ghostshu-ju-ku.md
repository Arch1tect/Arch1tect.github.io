---
date: '2015-10-25 22:29:37'
title: "Ghost\u6570\u636E\u5E93"
---
Ghost默认的数据库是sqlite3，也支持MySQL。

在/var/www/ghost/content/data， 可以看到前面提到过的两个数据库文件：ghost.db和ghost-dev.db 。

.db文件可以下载到本地然后用[sqlitebrowser](http://sqlitebrowser.org/)来浏览，截图如下：

<br />

![ghost sqlite tables](/content/images/2015/10/ghostTables.png)

也可以直接在shell里用sqlite3操作，比如：

打开ghost-dev.db数据库文件
`$ sqlite3 ghost-dev.db`

查看所有的表
`sqlite> .tables`

查看一个表的结构，比如posts这个表
`sqlite> .schema posts`

选择所有文章的标题
`sqlite> select title from posts;`

