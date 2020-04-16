---
date: "2012-03-03 21:48:02"
title: "Render and Time | \u6E32\u67D3\u4E0E\u65F6\u95F4"
---

Being a physics engine, Box2d is mostly responsible for the physics part – simulating things that happen in your physics  world. That means you won’t be able to see anything on your screen unless you render them. Here we can use [canvas](http://en.wikipedia.org/wiki/Canvas_element "canvas") element from Html5 together with a convenient built-in function called **DebugDraw**. Below is how DebugDraw works:

<pre><code>  
 var debugDraw = new b2DebugDraw();  
 debugDraw.SetSprite ( document.getElementById (“canvas”).getContext (“2d”));  
 debugDraw.SetDrawScale(30); //define scale  
 debugDraw.SetFillAlpha(0.3); //define transparency  
 debugDraw.SetLineThickness(1.0);  
 debugDraw.SetFlags(b2DebugDraw.e_shapeBit | b2DebugDraw.e_jointBit);  
 world.SetDebugDraw(debugDraw);  
 </code></pre>

Scale is used to convert things from meter to pixel and is typically set to 30 （1m=30px）. Then we need to configure <span style="text-decoration: underline;">time</span> and put it into this function - **update()**:

<pre><code>  
 function update() {  
     world.Step(1 / 60, 10, 10);  
     world.DrawDebugData();  
     world.ClearForces();  
 };  
 </code></pre>

The second line in the above code is quite important, I’ll explain it a little bit: 1/60 means 60 FPS; the following 10, 10 are for velocity iterations and position iterations. And they both control the accuracy of the physics in your game. If you set them too high, though you can get more perfect physics, the performance/speed of your game will be affected.

Sweet! Now we can put everything together and finally see the output on the screen:

<center>  
<iframe height="240" scrolling="no" src="/content/images/project/box2d_example/studynotes1.html" style="width: 200px; height: 400px;" width="320"></iframe></center>  

The pink box is our happyBox, I add the green box as a holder because otherwise, by the time you read here, happyBox must have already fallen out of the screen and you won’t see what happened at all. I also change happyBox’s restitution attribute to 1 (which means it’s perfectly elastic while 0 would mean the opposite) so it will keep bouncing forever! Following is the complete code:

<pre><code>


var b2Vec2 = Box2D.Common.Math.b2Vec2  
 , b2BodyDef = Box2D.Dynamics.b2BodyDef  
 , b2Body = Box2D.Dynamics.b2Body  
 , b2FixtureDef = Box2D.Dynamics.b2FixtureDef  
 , b2World = Box2D.Dynamics.b2World  
 , b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape  
 , b2DebugDraw = Box2D.Dynamics.b2DebugDraw;

//create world  
 var world = new b2World(new b2Vec2(0, 10), true);

//create Mr happyBox  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 bodyDef.position.Set(2, 2);  
 var fixDef = new b2FixtureDef;  
 fixDef.density = 10.0;  
 fixDef.friction = 0.5;  
 fixDef.restitution =1;

 fixDef.shape = new b2PolygonShape;  
 fixDef.shape.SetAsBox(1, 1);

var happyBox = world.CreateBody(bodyDef)  
 happyBox.CreateFixture(fixDef);

//create a holder  
 var holderDef = new b2BodyDef;  
 holderDef.type = b2Body.b2_staticBody;  
 holderDef.position.Set(2, 10);

 var holder = world.CreateBody(holderDef)  
 holder.CreateFixture(fixDef);

//setup debug draw  
 var debugDraw = new b2DebugDraw();  
 debugDraw.SetSprite( document.getElementById (“canvas”).getContext(“2d”) );  
 debugDraw.SetDrawScale(30.0);  
 debugDraw.SetFillAlpha(0.5);  
 debugDraw.SetLineThickness(1.0);  
 debugDraw.SetFlags(b2DebugDraw.e_shapeBit | b2DebugDraw.e_jointBit);  
 world.SetDebugDraw(debugDraw);

window.setInterval(update, 1000 / 60);

//update  
 function update() {  
 world.Step(1 / 60, 10, 10);  
 world.DrawDebugData();  
 world.ClearForces();  
 };  
</code></pre>

Please take a look at line 37-43, notice that when creating the holder, I only defined its bodyDef (this time called holderDef), but use the same fixDef as happyBox for convenience. Line 11 – 17 is just for simplification purpose, so instead of typing ‘Box2D. Dynamics. b2FixtureDef’, you just need to type b2FixtureDef. Now skipping common html tags, there is only line 54 – ‘window.setInterval(update, 1000 / 60)’ that I haven’t explained. Please google it yourself if you don’t understand it.

---

<pre><code>  
 var debugDraw = new b2DebugDraw();  
 debugDraw.SetSprite ( document.getElementById (“canvas”).getContext (“2d”));  
 debugDraw.SetDrawScale(30); //定义比例  
 debugDraw.SetFillAlpha(0.3); //define transparency  
 debugDraw.SetLineThickness(1.0);  
 debugDraw.SetFlags(b2DebugDraw.e_shapeBit | b2DebugDraw.e_jointBit);  
 world.SetDebugDraw(debugDraw);  
 </code></pre>

Scale 用来把单位从米转化成像素，一般设置为 30 左右（1 米＝ 30 像素）。 接下来我们需要设置时间，并将其放进 update（）这个方法中：

<pre><code>  
 function update() {  
 world.Step(1 / 60, 10, 10);  
 world.DrawDebugData();  
 world.ClearForces();  
 };  
 </code></pre>

上面第二行比较重要，简单来说 1／60 是 60 帧每秒的意思， 后面的两个 10 分别掌管速度计算和位置计算的精确度。如果定得太高，固然精确，游戏的性能也会受到影响。

好了，现在我们把这些代码放到一起，就可以看到下面的效果了：

<center>  
<iframe height="240" scrolling="no" src="/content/images/project/box2d_example/studynotes1.html" style="width: 200px; height: 400px;" width="320"></iframe></center>  

这粉色的盒子是 happyBox 童鞋，下面的绿色盒子是我后来加上去用来 hold 住 happyBox 用的，不然当你读到这里时 happyBox 童鞋必然早已落到屏幕之外了。我还将它的恢复系数改成了 1， 这表示物体发生的碰撞是完全弹性碰撞，没有能量损失，所以他可以一直欢乐地蹦蹦跳跳下去。下面是完整的代码：

<pre><code>

var b2Vec2 = Box2D.Common.Math.b2Vec2  
 , b2BodyDef = Box2D.Dynamics.b2BodyDef  
 , b2Body = Box2D.Dynamics.b2Body  
 , b2FixtureDef = Box2D.Dynamics.b2FixtureDef  
 , b2World = Box2D.Dynamics.b2World  
 , b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape  
 , b2DebugDraw = Box2D.Dynamics.b2DebugDraw;

//创世  
 var world = new b2World(new b2Vec2(0, 10), true);

//造盒  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 bodyDef.position.Set(2, 2);  
 var fixDef = new b2FixtureDef;  
 fixDef.density = 10.0;  
 fixDef.friction = 0.5;  
 fixDef.restitution =1;

fixDef.shape = new b2PolygonShape;  
 fixDef.shape.SetAsBox(1, 1);

var happyBox = world.CreateBody(bodyDef)  
 happyBox.CreateFixture(fixDef);

//造Holder  
 var holderDef = new b2BodyDef;  
 holderDef.type = b2Body.b2_staticBody;  
 holderDef.position.Set(2, 10);

var holder = world.CreateBody(holderDef)  
 holder.CreateFixture(fixDef);

//设DebugDraw  
 var debugDraw = new b2DebugDraw();  
 debugDraw.SetSprite( document.getElementById (“canvas”).getContext(“2d”) );  
 debugDraw.SetDrawScale(30.0);  
 debugDraw.SetFillAlpha(0.5);  
 debugDraw.SetLineThickness(1.0);  
 debugDraw.SetFlags(b2DebugDraw.e_shapeBit | b2DebugDraw.e_jointBit);  
 world.SetDebugDraw(debugDraw);

window.setInterval(update, 1000 / 60);

//update  
 function update() {  
 world.Step(1 / 60, 10, 10);  
 world.DrawDebugData();  
 world.ClearForces();  
 };   
</code></pre>

第 37－43 行，当我定义 Holder 的时候，我只定义了他的 bodyDef 部分（这次叫做 holderDef），至于 fixDef 部分我直接再次调用了 happyBox 的 fixDef 来节约代码。第 11－17 行同样是为了便利，比如将原红头文件中的 Box2D. Dynamics. b2FixtureDef 用 b2FixtureDef 代替。

最后放一个好玩的超弹金箍棒。

<center>  
<iframe height="240" scrolling="no" src="/content/images/project/box2d_example/monkeykingbar.html" style="width: 610px; height: 480px;" width="320"></iframe></center>
