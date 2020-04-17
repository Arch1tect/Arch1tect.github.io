---
date: "2012-03-23 02:22:02"
title: "Collision Detection  |  \u78B0\u649E\u68C0\u6D4B"
---

This post will introduce collision detection. Do I need to explain why this is extremely useful in a game? ^ ^

这篇介绍碰撞检测，它的用处太多了吧, 比方说如果玩家碰到什么不该碰的东西就会挂掉之类的。。 ^ ^

The simplest reason for why we need a collision detection would be deciding whether your player can jump or not.（You don’t want your player to be able to jump even when falling in the air right?）So to know whether your player is on the ground is important. Before I learn collision detection, this is how I solve the problem:

<pre><code>  
 …  
 if (player.y=10) // ’10′ is the y coordinate of player when it’s on the ground  
 canjump=true;  
 …  
 if (actualkey== ”w”  &&  canjump)  
 jump();  
</code></pre>

When the player is jumping its y coordinate will be smaller than 10 therefore can’t jump anymore.  That seems pretty easy right? No, It can be a lot of work in a real game if done that way! Imagine having 20 floating platforms, moreover your player may need to jump on other moving objects too… Now let’s look at a better way – **b2ContactListener**. It’s a very powerful and complex function but for now we only need **BeginContact **and** EndContact**. As their names suggest, they tell you when the contact begin and end. So you can know when your player is contacting the ground or other objects and when it’s not. I’m going to use the same example from my [last post](http://box2dweb.com/interactivity-%e6%93%8d%e7%ba%b5/ "Interactivity  |  操纵") to show you how it works:

**Step 1**,
add userData

For later referring, just add this line <span style="text-decoration: underline;">bodyDef.userData = ‘wheel’</span> when creating the wheel of the car :

<pre><code>  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 bodyDef.userData = ‘wheel’ // just add this line into the original code  
 …  
 …  
 var wheel1=world.CreateBody(bodyDef);  
 wheel1.CreateFixture(fixDef);  
</code></pre>

**Step 2**, set up jump function and key:

<pre><code>   
 function jump() {  
 car.SetLinearVelocity(new b2Vec2(0,-10))  
 }  
 …  
 …  
 //you learnt where to put the following lines from last post  
 if (actualkey==”j” && onground )  
 jump();  
</code></pre>

**Step 3**, set up listener

 <pre><code>   
 var listener = new Box2D.Dynamics.b2ContactListener;  
 listener. BeginContact = function(contact) {  
 if (contact.GetFixtureA().GetBody().GetUserData()== ‘wheel’ || contact.GetFixtureB().GetBody().GetUserData()== ‘wheel’ )  // think about why we don’t use fixture’s userData directly.  
 onground = true;  // don’t put ‘var’ here!  
 }  
 listener. EndContact = function(contact) {  
 if (contact.GetFixtureA().GetBody().GetUserData()== ‘wheel’ || contact.GetFixtureB().GetBody().GetUserData()== ‘wheel’ )  
 onground = false;  
 }  
 </code></pre>

**Step 4**, add following line into update()

`world.SetContactListener(listener);`

In step 3, it’s basically checking whether one of the two fixtures that are involved in contact is ‘wheel’. Alright, now if  you press ‘j’ when the wheel is contacting the ground, the car below should be able to jump!

<center>  
<iframe height="240" scrolling="no" src="https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/project/box2d_example/studynotes7.html" style="width: 600px; height: 330px;" width="320"></iframe></center> －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

窃以为碰撞检测最基本的用途是用来判定一个物体是否可以“往上跳”（当物体正在空中下坠的时候，一般来说是不允许跳的对吧）。具体要如何判定是问题的关键！ 在寡人学会用碰撞检测之前，本王是这么解决这个问题的：

<pre><code>  
 …  
 if (player.y=10) // ’10′是指玩家在地上时候的纵坐标  
 canjump=true;  
 …  
 if (actualkey==”w” && canjump)  
 jump();  
 </code></pre>

于是当玩家在地上的时候，它的纵坐标就大于等于 10，跳起来就小于 10 了，于是就不能跳了。 这似乎是个简单易行的方法？ 当然不！这完全是个费力不讨好的笨法子。 当你面对十几、二十个浮动的平台，而且还有其他活动的物体需要玩家踩着往上跳的时候，你的头就果断变大了。。。所以现在,我们开始学习高端技术 –  接触监听器（**b2ContactListener）。 **这是 box2d 提供的一个非常强大的功能，我们暂时只介绍其中的接触开始（**BeginContact）**与   接触结束**（EndContact）。** 就像名字听起来一样，它们分别在物体间的接触开始和结束的时候给于你提示。 没错~ 有了它们我们就可以对玩家是否站在地上了如指掌了~ 现在我直接拿[上篇](http://box2dweb.com/interactivity-%e6%93%8d%e7%ba%b5/ "Interactivity  |  操纵")中的例子向你展示**接触监听器**具体是如何使用的:

**步骤 1,** 添加 userData

为了后面可以“验明正身”，请在创建轮子的时候加入这行用来标记  <span style="text-decoration: underline;">bodyDef.userData = ‘wheel’</span>  :

<pre><code>  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 bodyDef.userData = ‘wheel’ // 这行是新加入的哦~  
 …  
 …  
 var wheel1=world.CreateBody(bodyDef);  
 wheel1.CreateFixture(fixDef);  
 </code></pre>

**步骤 2**, 设置向上跳的功能以及对应的键 :

<pre><code>  
 function jump() {  
 car.SetLinearVelocity(new b2Vec2(0,-10))  
 }  
 …  
 …  
 //看过上一篇的话你应该知道下面两行该放哪吧~  
 if (actualkey==”j” && onground )  
 jump();  
 </code></pre>

**步骤 3**, 设置监听器：

<pre><code>  
 var listener = new Box2D.Dynamics.b2ContactListener;  
 listener. BeginContact = function(contact) {  
 if (contact.GetFixtureA().GetBody().GetUserData()== ‘wheel’ || contact.GetFixtureB().GetBody().GetUserData()== ‘wheel’ )  // 想想为什么不直接用fixture 的 userData。  
 onground = true;   // 别加 ‘var’ !  
 }  
 listener. EndContact = function(contact) {  
 if (contact.GetFixtureA().GetBody().GetUserData()== ‘wheel’ || contact.GetFixtureB().GetBody().GetUserData()== ‘wheel’ )  
 onground = false;  
 }  
 </code></pre>

**步骤 4**, 把下面这行放进 update() ：

`world.SetContactListener(listener);`

在第三步中，我们检验了接触物体的 userData，接触总是发生在两个物体间，我们想知道这两个物体其中一个是否就是开始标记过的。 OK，现在只要你在小车的轮子接触着地面的时候按下“j”键，小车就会蹦起来啦！ 撒花~~~

<center>  
<iframe height="240" scrolling="no" src="https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/project/box2d_example/studynotes7.html" style="width: 600px; height: 330px;" width="320"></iframe></center>
