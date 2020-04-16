---
date: '2012-09-09 15:35:40'
title: Thoughts about Cracked Wordpress Themes and Plugins
---

To me it’s not very ethical to crack a charged premium theme/plugin since I know it really takes designers and programmers a lot of effort to create a well functioning and beautiful theme/plugin. Also it’s quite unfair for customers who pay for it, while those who don’t pay are getting the same service free of charge. Some may argue that the crackers spend their time cracking which means they are not just <label>being idle and profitting by other’s toil. Moreover some of them are not interested in the loot at all and the only reason they crack is they actually find it great fun in the cracking process itself. Therefore, I reserve my point here</label><label> as long as they aren’t </label>**distributing** the cracked themes or plugins.

Is downloading cracked themes/plugins unethical then? My answer is yes, but once you know that there are so many free riders out there. And you just need to type a few words in Google, then with a few clicks then sixty bucks will be saved. The right decision can be quite hard to make for the unwealthy group, e.g., students.

Others may argue that there is a risk which you may find the theme/plugin you buy isn’t exactly the one you need and since you don’t want it any more the money you pay is a big waste. Therefore these people would say that premium themes/plugins should always provide a free trial and since usually there isn’t such thing, this becomes their reason to justify themselves for downloading the cracked ones, promising that they would pay later if it’s really satisfying. This used to convince me but after a second thought, I realize that a piece of code isn’t that much different from an apple or a Macbook. It’s great if there are free trials for people to try before they buy but if there isn’t, one should think twice like they do before buying a sweet looking but potentially sour one’s teeth off plum.

I’ve been thinking more and more about the copyright issues since I came to the U.S. and have gradually started to donate to the theme/plugin authors( very little though ). Still I always do a search to make sure there is no cracked copies before I fill in my credit card numbers when purchasing themes/plugins. And yes, I sometimes download cracked themes. My understanding of copyright is still improving and I think  it’s a huge topic to dive into too, but I’ll learn it gradually and save it for my future post.

My initial motivation to write this post is that I found a tiny “callback” script in a cracked theme. It’s very bothering since it loads quite slow, moreover when sometimes that resource server is down, it takes about 18 sec for my WordPress blog to load! (same for every page because it’s in the header) When the time is out, it shows a very ugly broken image at the header. That drives me so crazy. So I used GTMetrics to track the source, then search all files in my themes but failed to find the script that send the request. Therefore I thought it’s a sly script that has already moved the script away from the theme folder. However when I change my theme, the request no longer exists. The most possible reason then seem to be that the script is somehow encoded. I start checking the theme files by eye. Luckily, it’s not a very complex encryption. The cracker simply reverse the link. Below is how this code work :

 

Original:

<pre><code>

echo ‘&lt;img src=”http://swotong.com/flight.jpeg”>’;  
 

Reversed:
echo strrev( ‘>”gepj.thgilf/moc.gnotows//:ptth”=crs gmi<’);

</code></pre>

 

It’s fun, isn’t it~  ^ ^


