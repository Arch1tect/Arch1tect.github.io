---
date: '2014-05-04 22:20:12'
title: "Amazon ec2 wordpress \u56FA\u5B9A\u94FE\u63A5\u4FEE\u6539\u95EE\u9898"
---

转到ec2后发觉wordpress建的网站不能修改固定链接了，以往是要修改.htaccess文件，但ec2默认是没有这个.htaccess文件的，所以要修改 /etc/httpd/conf目录下的httpd.conf文件，找到<Directory>改成下面这样：

Options FollowSymLinks  
 AllowOverride All

最后

sudo apachectl -k restart

完


