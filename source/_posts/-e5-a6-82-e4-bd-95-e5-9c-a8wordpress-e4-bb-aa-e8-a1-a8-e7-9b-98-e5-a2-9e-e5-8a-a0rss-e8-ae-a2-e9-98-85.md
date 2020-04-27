---
date: "2012-06-13 19:50:45"
title: "\u5982\u4F55\u5728Wordpress\u4EEA\u8868\u76D8\u589E\u52A0RSS\u8BA2\u9605"
---

首先，仪表盘里默认的这几个 RSS 是在 wp-admin/includes/dashboard.php 里面设定好了的，由 wp-admin/index.php 这个文件来调用。可以直接在那个文件处修改.

增加 rss 需要用到这两个 function： custom_dashboard_widget() 和 add_custom_dashboard_widget()

例：

<pre><code>  
 //下方代码添加一个名为“我订阅的RSS”的RSS栏目~  
 function custom_dashboard_widget() {

echo ‘<div>’; wp_widget_rss_output(‘[http://www.36kr.com/feed/’](), array( ‘show_author’ => 1, ‘show_date’ => 1, ‘show_summary’ => 1 )); echo “</div>”;

}

function add_custom_dashboard_widget() {

wp_add_dashboard_widget(‘custom_dashboard_widget’, ‘我订阅的RSS’, ‘custom_dashboard_widget’);

}  
 add_action(‘wp_dashboard_setup’, ‘add_custom_dashboard_widget’);

</code></pre>

就这么简单~ 用 0 或者 1 控制是否显示作者、日期、简要。。。

这个段代码可以放在主题的 fuctions.php 里也可以随便放在一个常用的插件的 php 文件里~

![](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/09/6a63f6246b600c33c055e9621a4c510fd9f9a16f-1.png)
