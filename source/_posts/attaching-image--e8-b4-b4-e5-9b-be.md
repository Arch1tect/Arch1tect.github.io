---
date: '2012-05-01 19:20:47'
title: "Attaching Image | \u8D34\u56FE"
---

This post is about attaching image!  
 该篇将介绍如何贴图!

You need to know how to use canvas before reading this but don’t worry that’s quite easy to learn.  
 First we need to prepare two images ‘tinywhale.png’ and ‘brotherwhale.png’ and use Image() as shown below.

<pre><code>  
 var image = new Image() ;  
 image.src = “tinywhale.png” ;

var image2 = new Image() ;  
 image2.src = “brotherwhale.png” ;

</code></pre>

Then delete or comment out the original world.DrawDebugData() in update() and add following code at the same place:

<pre><code>

context.clearRect(0, 0, 550, 480);  
 for (b = world.GetBodyList() ; b; b = b.GetNext())  
 {  
 if (b.GetType() == b2Body.b2_dynamicBody)  
 {  
 var pos = b.GetPosition();

context.save();  
 context.translate(pos.x * 20-20, pos.y * 20);  
 context.rotate((b.GetAngle())/15);  
 context.drawImage(image, -25, -25);  
 context.restore();  
 }

if (b.GetType() == b2Body.b2_kinematicBody)  
 {

var pos = b.GetPosition();

context.save();  
 context.translate(pos.x * 20, pos.y * 20);  
 context.rotate((b.GetAngle())/15);  
 context.drawImage(image2, -25, -25);  
 context.restore();  
 }

}  
 </code></pre>

Basically the above code is attaching *tinywhale.png* to every dynamicBody while attaching *brotherwhale.png* to kinematicBody(there is only one in the demo). Here ‘attach’ actually means using the positions of objects calculated by box2d for the images we have.

P.S.  
 try pressing T and w a s d j or you can drag with your mouse directly ^ ^

 

 

 

<center><iframe height="480" width = "100%"  scrolling="no" src="/content/images/project/learnBox2d/mywhale/newSquid.html" ></iframe></center>  
   

 

阅读此篇前你需要了解一定的canvas使用方法。即便你不会使用canvas，也很容易就可以学会它的基本用法。

贴图前首先准备好要贴的图~

<pre><code>  
 var image = new Image();  
 image.src = “tinywhale.png” ;

var image2 = new Image();  
 image2.src = “brotherwhale.png” ;

</code></pre>

然后将update（）中的 world.DrawDebugData() 替换为下面的代码：

<pre><code>

context.clearRect(0, 0, 550, 480);  
 for (b = world.GetBodyList() ; b; b = b.GetNext())  
 {  
 if (b.GetType() == b2Body.b2_dynamicBody)  
 {  
 var pos = b.GetPosition();

context.save();  
 context.translate(pos.x * 20-20, pos.y * 20);  
 context.rotate((b.GetAngle())/15);  
 context.drawImage(image, -25, -25);  
 context.restore();  
 }

if (b.GetType() == b2Body.b2_kinematicBody)  
 {

var pos = b.GetPosition();

context.save();  
 context.translate(pos.x * 20, pos.y * 20);  
 context.rotate((b.GetAngle())/15);  
 context.drawImage(image2, -25, -25);  
 context.restore();  
 }

}  
 </code></pre>

简单来说上面的代码将图片*tinywhale.png*贴在了每个dynamicBody上，将*brotherwhale.png*贴在了每个kinematicBody上面。其实说‘贴’并不恰当，应该说是在用box2d来计算图片每时每刻具体应该在什么位置。

P.S.  
 鼠标拖拽之余再试试用键盘操纵它们吧~ （其实只有一只是可以动滴。。）

 

 

 
<center><iframe height="480" width = "100%"  scrolling="no" src="/content/images/project/learnBox2d/mywhale/newSquid.html" ></iframe></center>  

 


