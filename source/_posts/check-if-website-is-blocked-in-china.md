---
date: '2015-10-31 19:32:22'
title: Check if website is blocked by China's GFW
---
Firstly, the two websites below are good tools for checking if your website is blocked in China.

https://en.greatfire.org
http://www.websitepulse.com/help/testtools.china-test.html

It would be really convenient if I can get a VPS that's located in China, then I can see how my website is behaving when visited from China. I actually tried to register one with aliyun.com from alibaba in China, but failed because I don't have a Chinese phone number. I don't really want to pay for some VPS service simply for checking whether my website work in China anyways.

**DNS**

I bought my domain name from Godday so the name server is from them too. Godaddy's name server has been reported to be blocked by China in the past, although I personally didn't experience it since I'm not in China. 

There are some alternatives like DNSPOD and Amazon's Route 53. I've been using DNSPOD for a few years for most of my websites and it's pretty stable, plus its free tier is great. This time, however, I have not switched to DNSPOD from Godday's DOMAINCONTROL.COM yet since I checked using tools above and find my website working fine in China currently.

I'll switch to DNSPOD again if I found any problem.

---
P.S. 

11.20.2015

I'm in China right now so I tested my blog thoroughly and everything is working fine except:

* Embeded Youtube video can't be loaded.

* Gravatar can't be loaded, timeout after 20s.


Youtube is expected to be blocked by China's GFW for sure, but I have zero clue why GFW block Gravatar too...

For Gravatar, I found that gravatar.com and secure.gravatar.com still work, only www.gravatar.com is blocked. So I believe the domain name of gravatar.com is not yet blocked, only IP of www.gravatar.com is blocked.




