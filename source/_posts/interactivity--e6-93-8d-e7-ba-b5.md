---
date: "2012-03-14 03:46:10"
title: "Interactivity  |  \u64CD\u7EB5"
---

This post shows how to control your object during the game with different methods.

此篇介绍如何用不同的方法操纵 Box2d 中的物体。

This should be an exciting post for newbies, finally we are able to control things in the Box2d world! (dragging your player with mouse joint doesn’t count : ) In this post we will use keyboard for controlling and before that, I’ll show you four basic methods :

**Force**

<pre><code>  
function push() {  
    car.ApplyForce(new b2Vec2(-99,0), car.GetWorldCenter());  
}  
 </code></pre>

**Impulse**

<pre><code>  
function hit() {  
    car.ApplyImpulse(new b2Vec2(-99,0), car.GetWorldCenter())  
}  
 </code></pre>

**Velocity**

<pre><code>  
function speed() {  
    car.SetLinearVelocity(new b2Vec2(-99,0))  
}  
</code></pre>

**Teleportation**

<pre><code>  
function teleport() {  
    car.SetPositionAndAngle(new b2Vec2(5,0),0);  
}  
 </code></pre>

The codes above are pretty simple so I won’t explain too much. The second parameter in force/impulse defines where specifically on the object will the  force / impulse be applied to. <span style="text-decoration: underline;">GetWorldCenter</span> refers to object’s center of mass so it won’t rotate if that’s where the force / impulse is applied to. And <span style="text-decoration: underline;">GetWorldPoint</span> with a vector parameter will be what you need if you want to apply the  force / impulse to any specific point relative to the object (the point doesn’t have to be on the object). Now that these methods are defined, let’s use the following codes to implement keyboard function:

<pre><code>

function swtkeyboard(e){  
 var evtobj=window.event? event : e //distinguish between IE’s explicit event object (window.event) and Firefox’s implicit.  
    var unicode=evtobj.charCode? evtobj.charCode : evtobj.keyCode  
    var actualkey=String.fromCharCode(unicode)

   if (actualkey == ”f” )  
       push();

   if (actualkey == ”i” )  
       hit();

   if (actualkey == ”v” )  
       speed();

   if (actualkey == ”t” )  
       teleport();  
 }

</code></pre>

Last step! Add the above function into <span style="text-decoration: underline;">update</span> function:

<pre><code>

function update() {

    world.Step(1 / 60, 10, 10) ;  
    world.DrawDebugData() ;  
    world.ClearForces() ;  
    document.onkeypress=swtkeyboard; 
 }

</code></pre>

Done! I added a temple just for fun~ ^ \_ ^

<center>  
<iframe height="240" scrolling="no" src="https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/project/box2d_example/studynotes5.html" style="width: 610px; height: 330px;" width="320"></iframe></center>      Press different keys (f, i, v, t) to test these different methods. Notice that <span style="text-decoration: underline;">force</span> will need to be applied for some time in order to show the effect. And the effects of both applying force and impulse depend on the mass of an object while applying velocity has nothing to do with the mass of an object. Please google Newton’s Laws if you don’t know why.

---

<div style="text-align: center;"></div>     激动人心的时刻到了，我们终于可以在Box2d的世界里控制物体了！（用鼠标拖拽可不算，那个叫玩赖）这篇我们使用高贵的键盘来进行操纵，在那之前，容我先介绍四种基本的控制物体的方式：

**作用力**

<pre><code>  
 function push() {  
     car.ApplyForce(new b2Vec2(-99,0), car.GetWorldCenter()) ;  
 }  
 </code></pre>

**冲量**

<pre><code>  
 function hit() {  
     car.ApplyImpulse(new b2Vec2(-99,0), car.GetWorldCenter())  
 }  
 </code></pre>

**速度**

<pre><code>  
 function speed() {  
     car.SetLinearVelocity(new b2Vec2(-99,0));  
 }  
 </code></pre>

**瞬移**

<pre><code>  
 function teleport() {  
     car.SetPositionAndAngle(new b2Vec2(5,0),0);  
 }  
 </code></pre>

上面的代码很简洁吧，注意冲量和作用力有两个参数，第二个 <span style="text-decoration: underline;">GetWorldCenter</span>  表示作用点在物体的质心上，此时物体收到作用力或冲量后，只会发生平动不会发生转动（突然好怀念物理）。 你可以使用  <span style="text-decoration: underline;">GetWorldPoint</span>  和一个矢量来定义具体的作用点。（作用点的位置相对于物体，但可以不在物体上。） 定义好了这几个操纵方式，是时候设置键盘的操作了，我用四个键分别给物体以上四种命令:

<pre><code>

function swtkeyboard(e){  
 var evtobj=window.event? event : e //distinguish between IE’s explicit event object (window.event) and Firefox’s implicit.  
 var unicode=evtobj.charCode? evtobj.charCode : evtobj.keyCode  
 var actualkey=String.fromCharCode(unicode)

   if (actualkey == ”f” )  
       push();

   if (actualkey == ”i” )  
       hit();

   if (actualkey == ”v” )  
       speed();

   if (actualkey == ”t” )  
       teleport() ;  
 }

</code></pre>

最后一步，将  document.onkeypress=swtkeyboard  加入  <span style="text-decoration: underline;">update</span>  中:

<pre><code>

function update() {

    world.Step(1 / 60, 10, 10) ;  
    world.DrawDebugData() ;  
    world.ClearForces() ;  
    document.onkeypress=swtkeyboard ;
 }

</code></pre>

大功告成，我顺便放了个神庙让小车撞着玩~ ^ \_ ^

<center>  
<iframe height="240" scrolling="no" src="https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/project/box2d_example/studynotes5.html" style="width: 610px; height: 330px;" width="320"></iframe></center>     试试按不同按键 (f, i, v, t) 来理解上面介绍的四种操纵方式。 注意作用力 f 需要按住一段时间才能看到效果。（一直按着小车就能爬上山坡了呢。） 作用力和冲量产生的效果和物体本身的质量有关，速度则不然。 如果您不解请百度牛顿定律什么的。
