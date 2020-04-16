---
banner_img: /content/images/uploads/2013/02/Screen-Shot-2013-02-02-at-1.41.23-AM.png
date: '2013-02-02 03:16:11'
index_img: /content/images/uploads/2013/02/Screen-Shot-2013-02-02-at-1.41.23-AM.png
title: "Wordpress \u540C\u4E00\u9875\u9762\u5B9E\u73B0\u591A\u4E2A\u677F\u5757\u72EC\
  \u7ACB\u5FAA\u73AF\u7684\u65B9\u6CD5\uFF08\u542B\u7FFB\u9875\u529F\u80FD\uFF1A\uFF09"
---

这周给StarryStory的网站更新，将首页划分成了三个板块,（case, story, observation)  每个板块显示的文章通过tags来过滤，同时各板块都有翻页功能，并且“记忆”其他板块所在页面，效果如下图：

[![Screen Shot 2013-02-02 at 1.41.23 AM](/content/images/uploads/2013/02/Screen-Shot-2013-02-02-at-1.41.23-AM-293x300.png)](/content/images/uploads/2013/02/Screen-Shot-2013-02-02-at-1.41.23-AM.png)

（图片里应该可以看到三个灰色/蓝色的翻页部分吧？ 不清楚的话可以直接去[StarryStory](http://starrystory.org)那里体验。）

下面的代码实现这三个板块的独立循环和翻页功能：  
<pre><code>  
$paged1 = isset( $_GET['paged1'] ) ? (int) $_GET['paged1'] : 1; //paged1 是中间Story板块  $paged2 = isset( $_GET['paged2'] ) ? (int) $_GET['paged2'] : 1; //paged2 是中间下方Observation板块  
$paged3 = isset( $_GET['paged3'] ) ? (int) $_GET['paged3'] : 1; //paged3 是左边Case板块

//上面的意思大概是如果用户原来在板块某个页码，那么就输出那个页码的内容，否则输出该板块的第一页.

// 中间Story板块的循环

$recentStory = new WP_Query(“tag=’story’&showposts=5&paged=” . $paged1 ); //这里是用tag来过滤，也可以用category过滤

while($recentStory->have_posts()) : $recentStory->the_post();
the_title();  
 the_excerpt();  //因为是示例代码，这里只放文章标题和摘要。各位自己要加需要的div class id来调整输出的格式哦。

endwhile;
//这个array是Story板块翻页用的
$pag_args1 = array(
‘format’ => ‘?paged1=%#%’,  
 ‘current’ => $paged1,  
 ‘total’ => $recentStory->max_num_pages,  
 ‘add_args’ => array( ‘paged2′ => $paged2, ‘paged3′ => $paged3 ) //如果你有更多的板块，也要加进这个array里  
 );  
echo paginate_links( $pag_args1 );

//Story板块完成~！

//接下来是中间下方的Observation板块的循环，代码和上面大同小异。

$recentObservation = new WP_Query(“tag=’observations’&showposts=1&paged=” . $paged3 );
//这个循环输出tag为observation的文章

while($recentObservation->have_posts()) :     

    $recentObservation->the_post();

    the_title();  
    the_excerpt();

endwhile;

//这个array是Observation板块翻页用的  
$pag_args2 = array(

 ‘format’ => ‘?paged3=%#%’,  
 ‘current’ => $paged3,  
 ‘total’ => $recentObservation->max_num_pages,  
 ‘add_args’ => array( ‘paged2′ => $paged2,’paged1′ => $paged1 )  
);  
 echo paginate_links( $pag_args2 );

//我想诸位肯定都明白了，第三个板块的代码我就不贴了.

</code></pre>

虽然上面的代码是生成三个板块的，如果要更多板块只要按照这个结构增加就好了~

另外这个功能用ajax实现就更好了。

参考资料：

这个分版块的功能还是很有用的，网上似乎没有好的教程，我是在stackexchange某人的回答里找到了上面的实现方法：

[http://wordpress.stackexchange.com/questions/47259/multiple-wp-query-loops-with-pagination](http://wordpress.stackexchange.com/questions/47259/multiple-wp-query-loops-with-pagination)

 

 


