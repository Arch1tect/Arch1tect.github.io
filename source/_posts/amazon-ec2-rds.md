---
date: "2014-05-08 06:56:27"
title: Amazon EC2 + RDS
---

用了亚马逊 EC2 作服务器后发现数据库 mysql 总是崩溃，因为内存不够，参考一些文章优化了配置，设置 swap space 也解决不了问题。 网上很多人都建议用亚马逊的 RDS 来放置数据库，通过 EC2 去连接 RDS 读取数据。没有看到特别好的教程，我研究了半天才设置成功。 以下几点要注意：

1. RDS 的 security group 要和 EC2 的 instance 一致

2. EC2 的 IP Permission 设置如下：

[![Selection_010](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2014/05/Selection_010.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2014/05/Selection_010.png)

inbound rule 要加上 mysql 类型， 其中 Source 处我选择的是 Custom IP， 填入 EC2 的 Private IP (不是你的 Public IP, 两者不同！)   这里填的 IP 地址是允许访问数据库的地址，如果选择 anywhere 那么任何地址都可以访问; 如果选 My IP 那就是你现在浏览网页所用的电脑的 IP 地址; 所以如果填了 EC2 的 Private IP，就只有通过你自己的 EC2 instance 才可以访问数据库。

接下来 outbound rule 里也要加上 mysql，但好像必须选择 anywhere 才行。

如果上面设置的有问题的话很可能会遇到这个错误：

**ERROR 2003 (HY000): Can’t connect to MySQL server on ‘address.rds.amazonaws.com’ (110)**

我就是上面两个设置没有做好，导致连接失败的。。

确保能从 EC2 连到 RDS 就没什么问题了，后面就是将 wp-config.php 文件里的“localhost”改成 RDS 的 endpoint 地址了。

<pre><code>
/** MySQL hostname */  
 define(‘DB_HOST’, ‘localhost’);
</code></pre>

Amazon RDS 像 EC2 一样也提供免费的服务。 免费 + 免费 = 免费 ：）

看看用了 RDS + EC2 以后还会不会出问题了。
