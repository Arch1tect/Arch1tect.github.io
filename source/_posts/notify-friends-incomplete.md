---
date: '2013-03-07 05:02:43'
title: Notify Friends Incomplete
---

<pre><code>

<?php

/**

* @package Arch!tect

* @version 0.1

*/

/*

Plugin Name: Notify Friends  
 Plugin URI: [http://swotong.com](http://swotong.com)  
 Description: Life is like a boat  
 Author: Arch!tect  
 Version: 0.1  
 Author URI: [http://swotong.com](http://swotong.com)

*/

/*

╮(╯_╰)╭   buggy code, it can change friend’s name into link to their blog now.  
 But buggy if save multiple times before publishing etc…

*/

 

function email_friend()  {

// get post object  
 $post = get_post($id);  
 // get post content  
 $content = $post->post_content;//content before update no good  
 // if @ with a name after it exists  
 //$mentionCount = preg_match_all(‘/(@(\w)+)/’, $content, $matches);  
 $mentionCount = preg_match_all(‘/(@[^\s]+)/’, $content, $matches);//support Chinese  
 if (0 !== $mentionCount) {  
 $friendList = array();  
 for ($mentionIndex=0; $mentionIndex < $mentionCount; $mentionIndex++)  
 {  
 $mentionName = $matches[0][$mentionIndex];  
 $mentionName = str_replace(‘_’,’ ‘,$mentionName); //change _ back to space  
 $mentionName = substr($mentionName, 1); //get rid of @  
 $friend_display_name_like = ‘%’ . like_escape($mentionName) . ‘%’; //security and add wildcard  
 global $wpdb;  
 // get correct name  
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
 $subject = ‘Arch!tect在他的新博文 《’.$postTitle .  
 ‘》中@了你 \(^o^)/’;  
 $from = “noreplay@swotong.com”;  
 $headers = “From:” . $from;  
 $message = “Arch!tect在他的新博文 《”.$postTitle .  
 “》 中@了你，不去看看吗？\n\n”  .”博文地址：”.$post_permalink  
 .”\n\n\n请误直接回复本邮件。 \r\n”;  
 if(mail($to, $subject, $message, $headers)) {  
 array_push($friendList, $friendCorrectName);  
 }  
 }  
 }  
 $comma_separated = implode(“,”, $friendList);  
 $postTitle = get_the_title($id);  
 $post_permalink = get_permalink( $id );  
 $to = ’123@gmail.com’;  
 $subject = “博文《”.$postTitle .  
 “》发布同时成功通知了”.count($friendList).”位朋友”;  
 $from = “noreplay@swotong.com”;  
 $headers = “From:” . $from;  
 $message = “博文《”.$postTitle .  
 “》发布同时成功通知了”.count($friendList).”位朋友： \n\n”  .$comma_separated ;  
 if(count($friendList)>0){  
 mail($to, $subject, $message, $headers);  
 }  
 }  
 }//end of email_friend function  
    
 // change friend’s name to blog url  
 function post_update_edit_post_content( $content, $post_id ) {  
 $mentionCount = preg_match_all(‘/(@[^\s]+)/’, $content, $matches);//support Chinese  
    
 if (0 !== $mentionCount) {  
 for ($mentionIndex=0; $mentionIndex < $mentionCount; $mentionIndex++)  
 {  
 $mentionName = $matches[0][$mentionIndex];  
 //keep the potential incomplete input name by blogger, needed for replacing  
 $bloggerInputName =  $mentionName;  
 $mentionName = str_replace(‘_’,’ ‘,$mentionName); //change _ back to space  
 $mentionName = substr($mentionName, 1); //get rid of @  
 $friend_display_name_like = ‘%’ . like_escape($mentionName) . ‘%’; //security and add wildcard  
 global $wpdb;  
 // get correct name  
 $friendCorrectName = $wpdb->get_var( $wpdb->prepare( ”  
 SELECT comment_author  
 FROM $wpdb->comments  
 WHERE comment_author  
 LIKE %s “,  
 $friend_display_name_like  
 )) ;

// get friend’s url

/* notice: because sometimes visitor might not always type in his website  
 we need to find until found the one with website address if exist one  
 shouldn’t use IS NOT NULL use NOT LIKE ” instead  
 */

$friend_blog_url = $wpdb->get_var( $wpdb->prepare( ”  
 SELECT comment_author_url  
 FROM $wpdb->comments  
 WHERE comment_author_url NOT LIKE ”  
 AND comment_author  
 LIKE %s”,  
 $friendCorrectName  
 )) ;

if($friend_blog_url ) {  
 $link_title = “<a title=’click to visit “.$friendCorrectName.”‘”;  
 $friends_link = “href=’”. $friend_blog_url.”‘target=’_blank’> “;//open in new page  
 $friend_link_complete_string = “@ “.$link_title .$friends_link.$friendCorrectName.”</a>”;  
 $content= str_replace($bloggerInputName, $friend_link_complete_string, $content);

}else if($friendCorrectName ){

$just_change_name = “@ “.$friendCorrectName;  
 $content= str_replace($bloggerInputName, $just_change_name, $content);

}  
 }  
 }  
 return $content;

}

add_filter( ‘edit_post_content’, ‘post_update_edit_post_content’, 10, 2 );  
 add_action ( ‘publish_post’, ‘email_friend’);

</code></pre>


