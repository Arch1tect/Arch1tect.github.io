---
date: '2015-10-24 18:40:19'
title: "\u5B89\u88C5Ghost \uFF08AWS EC2\uFF09"
---
终于成功装好了Ghost,昨晚试了好久一直不成功今天才发现明明端口是2368，但我一直在试2386。。。 

具体步骤

1. 安装Node 0.10.40版本
2. 下载安装Ghost:

下载Ghost

`$ curl -L https://ghost.org/zip/ghost-latest.zip -o ghost.zip`

解压缩到特定文件夹

`$ unzip -uo ghost.zip -d /var/www/ghost`

安装

`$ cd /var/www/ghost && npm install --production`

运行

`$ npm start --production`

这时Ghost会监听127.0.0.1:2368, 要从外界访问的话，需要编辑config.js，将其中的127.0.0.1改成0.0.0.0即可。最后还要确认AWS EC2的Security Rule是允许外界访问2368这个port的。


