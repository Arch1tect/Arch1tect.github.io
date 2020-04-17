---
date: "2015-10-25 22:29:37"
title: "Ghost\u6570\u636E\u5E93"
---

Ghost 默认的数据库是 sqlite3，也支持 MySQL。

在/var/www/ghost/content/data， 可以看到前面提到过的两个数据库文件：ghost.db 和 ghost-dev.db 。

.db 文件可以下载到本地然后用[sqlitebrowser](http://sqlitebrowser.org/)来浏览，截图如下：

<br />

![ghost sqlite tables](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/2015/10/ghostTables.png)

也可以直接在 shell 里用 sqlite3 操作，比如：

打开 ghost-dev.db 数据库文件
`$ sqlite3 ghost-dev.db`

查看所有的表
`sqlite> .tables`

查看一个表的结构，比如 posts 这个表
`sqlite> .schema posts`

选择所有文章的标题
`sqlite> select title from posts;`
