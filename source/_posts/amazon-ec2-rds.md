---
date: '2014-05-08 06:56:27'
title: Amazon EC2 + RDS
---

用了亚马逊EC2作服务器后发现数据库mysql总是崩溃，因为内存不够，参考一些文章优化了配置，设置swap space也解决不了问题。 网上很多人都建议用亚马逊的RDS来放置数据库，通过EC2去连接RDS读取数据。没有看到特别好的教程，我研究了半天才设置成功。 以下几点要注意：

1. RDS的security group要和EC2的instance一致

2. EC2的IP Permission设置如下：

[![Selection_010](/content/images/uploads/2014/05/Selection_010.png)](/content/images/uploads/2014/05/Selection_010.png)

inbound rule 要加上 mysql 类型， 其中Source处我选择的是Custom IP， 填入EC2 的Private IP (不是你的Public IP, 两者不同！)   这里填的IP地址是允许访问数据库的地址，如果选择anywhere那么任何地址都可以访问; 如果选My IP那就是你现在浏览网页所用的电脑的IP地址; 所以如果填了EC2的Private IP，就只有通过你自己的EC2 instance才可以访问数据库。

接下来outbound rule 里也要加上mysql，但好像必须选择anywhere才行。

如果上面设置的有问题的话很可能会遇到这个错误：

**ERROR 2003 (HY000): Can’t connect to MySQL server on ‘address.rds.amazonaws.com’ (110)**

我就是上面两个设置没有做好，导致连接失败的。。

确保能从EC2连到RDS就没什么问题了，后面就是将wp-config.php文件里的“localhost”改成RDS的endpoint地址了。

<pre><code>
/** MySQL hostname */  
 define(‘DB_HOST’, ‘localhost’);
</code></pre>
 

Amazon RDS像EC2一样也提供免费的服务。 免费 + 免费 = 免费 ：）

看看用了RDS + EC2 以后还会不会出问题了。

 


