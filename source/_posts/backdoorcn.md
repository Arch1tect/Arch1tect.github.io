---
date: "2012-07-05 13:09:51"
title: "\u4E00\u4E2A\u5E26\u6709\u540E\u95E8\u7684Wordpress\u63D2\u4EF6"
---

本篇只作简单介绍，详细请见上一篇“

[How a wordpress plugin or theme hack your site](http://swotong.com/how-a-wordpress-plugin-or-theme-hack-your-site/ "Permalink to How a wordpress plugin or theme hack your site")

”

该脚本两个主要功能：

1、将 config.php 发送到黑客指定邮箱

2、建立后门

实现过程：

用户 下载插件上传后，一旦启用，启用钩子 会自动执行该代码，完成以上两个任务，插件删除后不能清除后门。

使用：

开发者收到邮件后，检查附件中的 config 文件内容，推测出用户的账号密码以及网站地址。

来到网站地址/wp-login.php 尝试用推测的账号密码登陆

尝试用推测出的 ftp 远程连接

使用后门登陆:

网址/wp-cong.php(使用 s、w、t 三个参数进行创建、删除用户，t 则为文件毁灭，不可逆)

注：删除用户在 mu 下数据库中会留下痕迹（用户名 ID）。

[下载](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/09/hello-dolly.zip "下载该插件")

#### 免责声明：

#### 该材料仅供学习交流使用，严禁用于非法用途及非正当用途，否则后果自负。
