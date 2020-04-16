---
date: '2013-03-03 20:59:29'
title: Notify Friends Plugin and Code
---

Feel free to comment and help me improve! ![:)](http://swotong.com/wp-includes/images/smilies/icon_smile.gif)

English version

The code below will email your friend once you publish your post if you have @ their names in your post. And you’ll receive an email yourself about how many of your friends received your email notification successfully. Just paste the code below into your functions.php file in the theme you are currently using and you are good to go! Or you can download the simple plugin which is basically the same thing except more convenient for you to activate/deactivate.

Only works for friends who have commented on your blog before (otherwise how do you get their email)

<pre><code>  
 function email_friend() {

// get post object  
 $post = get_post($id);  
 // get post content  
 $content = $post->post_content;  
 // get how many people is mentioned in this post  
 //$mentionCount = preg_match_all(‘/(@(\w)+)/’, $content, $matches);  
 $mentionCount = preg_match_all(‘/(@[^\s]+)/’, $content, $matches);//support other lang

// if there is at least one @ with a name after it  
 if (0 !== $mentionCount) {

$friendList = array();//for storing correct names

for ($mentionIndex=0; $mentionIndex < $mentionCount; $mentionIndex++) {

$mentionName = $matches[0][$mentionIndex];

$mentionName = str_replace(‘_’,’ ‘,$mentionName); //change _ back to space

$mentionName = substr($mentionName, 1); //get rid of @  
 //for security and add wildcard  
 $friend_display_name_like = ‘%’ . like_escape($mentionName) . ‘%’;

global $wpdb;

// get correct name first  
 $friendCorrectName = $wpdb->get_var( $wpdb->prepare( ”

SELECT comment_author  
 FROM $wpdb->comments  
 WHERE comment_author  
 LIKE %s “,  
 $friend_display_name_like  
 )) ;

// get friend email by comment author name  
 $friend_email = $wpdb->get_var( $wpdb->prepare( ”

SELECT comment_author_email  
 FROM $wpdb->comments  
 WHERE comment_author  
 LIKE %s “,  
 $friendCorrectName  
 )) ;

if($friend_email) {// if found email address then email

$postTitle = get_the_title($id);  
 $post_permalink = get_permalink( $id );  
 $to = $friend_email;  
 $subject = ‘Arch!tect mentioned you in his new post 《’.$postTitle .

‘》’;

$from = “noreplay@swotong.com”;

$headers = “From:” . $from;

$message = “Arch!tect mentioned you in his new post《”.$postTitle .  
 “》 check it out？\n\n” .”Post link：”.$post_permalink  
 .”\n\n\nPlease don’t reply this email.\r\n”;

if(mail($to, $subject, $message, $headers)) {  
 //if send successfully put his/her name in my list  
 array_push($friendList, $friendCorrectName);  
 //array_push($friendList, $friend_email);  
 }

}

}  
 $comma_separated = implode(“,”, $friendList); //friend list array to string

// now send an email to myself about the result  
 $postTitle = get_the_title($id);  
 $post_permalink = get_permalink( $id );  
 $to = ‘myOwn@email.com’;  
 $subject = “Your new post《”.$postTitle .  
 “》has notified “.count($friendList).”friends successfully”;  
 $from = “noreplay@email.com”;  
 $headers = “From:” . $from;  
 //list all friends that received my email  
 $message = “Your new post《”.$postTitle .  
 “》has notified “.count($friendList).”friends successfully:\n\n”.$comma_separated ;

mail($to, $subject, $message, $headers);

}

}//end of email_friend function

add_action ( ‘publish_post’, ‘email_friend’ );  
</code></pre>

 

——————————————————–中文版—————————————————————–

这段代码用于通知朋友你的新博文中提到了对方，用法很简单，像社交网站那样@一下对方的用户名就好啦~ 文章发表的同时email就会发出，然后会有一封email发回给你自己，报告有多少朋友成功收到了你的email通知，听上去很简单吧！你可以下载插件或者直接把下面的代码粘贴到当前主题的functions.php文件里，妥妥的~

只对曾在你的博客评论过的朋友有效哦~ （不然要怎样获取对方的邮箱地址）

<pre><code> 
 function email_friend() {  
 // get post object  
 $post = get_post($id);  
 // get post content  
 $content = $post->post_content;  
 // 看有几个@ （@后面要有跟字符，单独一个@不算）  
 //$mentionCount = preg_match_all(‘/(@(\w)+)/’, $content, $matches);  
 $mentionCount = preg_match_all(‘/(@[^\s]+)/’, $content, $matches);// \s支持中文  
 if (0 !== $mentionCount) { //如果有的话

$friendList = array(); //这个array用来放一会儿成功发送过去的朋友名单

for ($mentionIndex=0; $mentionIndex < $mentionCount; $mentionIndex++)

{

$mentionName = $matches[0][$mentionIndex];

$mentionName = str_replace(‘_’,’ ‘,$mentionName); //把下划线变回空格

$mentionName = substr($mentionName, 1); //去掉 @ 符号

$friend_display_name_like = ‘%’ . like_escape($mentionName) . ‘%’; //like_escape为了数据库安全

global $wpdb;

// 获取正确ID名，因为前面@的不一定是完整的拼写  
 $friendCorrectName = $wpdb->get_var( $wpdb->prepare( ”

SELECT comment_author  
 FROM $wpdb->comments  
 WHERE comment_author  
 LIKE %s “,  
 $friend_display_name_like  
 )) ;

// 获取朋友的邮箱地址

$friend_email = $wpdb->get_var( $wpdb->prepare( ”

SELECT comment_author_email  
 FROM $wpdb->comments  
 WHERE comment_author  
 LIKE %s “,  
 $friendCorrectName  
 )) ;

if($friend_email) {// 如果有找到提到的朋友的邮箱地址就发信给他~  
 $postTitle = get_the_title($id);

$post_permalink = get_permalink( $id );

$to = $friend_email;

$subject = ‘Arch!tect在他的新博文 《’.$postTitle .

‘》中@了你 \(^o^)/’;

$from = “noreplay@whatsoever.com”;

$headers = “From:” . $from;

$message = “Arch!tect在他的新博文 《”.$postTitle .

“》 中@了你，不去看看吗？\n\n” .”博文地址：”.$post_permalink

.”\n\n\n请误直接回复本邮件。 \r\n”;

if(mail($to, $subject, $message, $headers)) {

array_push($friendList, $friendCorrectName); //如果发送成功了，放进名单里  
 //array_push($friendList, $friend_email);  
 }

}

}  
 $comma_separated = implode(“,”, $friendList);

$postTitle = get_the_title($id);  
 $post_permalink = get_permalink( $id );  
 $to = ‘youremail@address.com’;//你的邮箱地址，记得引号哦  
 $subject = “博文《”.$postTitle .  
 “》发布同时成功通知了”.count($friendList).”位朋友”;  
 $from = “noreplay@whatever.com”; //希望显示的发信人地址  
 $headers = “From:” . $from;  
 $message = “博文《”.$postTitle .  
 “》发布同时成功通知了”.count($friendList).”位朋友： \n\n” .$comma_separated ;

mail($to, $subject, $message, $headers);  
 }

}//end of email_friend function

add_action ( ‘publish_post’, ‘email_friend’ );

</code></pre>

 

 


