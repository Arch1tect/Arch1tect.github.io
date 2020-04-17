---
date: "2012-03-10 22:06:33"
title: "Powerful Joints |  \u5F3A\u5927\u7684\u8FDE\u63A5\u5668"
---

This post mainly introduces revolute joint and a little bit of mouse joint.

本文主要介绍旋转连接器与鼠标连接器。

**Revolute Joint**

To me revolute joint is the most useful joint, it’s also quite easy to set up. Before that, I need to change the shape of the car to be a convex polygon and create those two wheels as individual objects this time instead of being fixtures of ‘car’.

<pre><code>

 //  making a car  
 //  two wheels  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 var fixDef = new b2FixtureDef;  
 fixDef.density = 30;  
 fixDef.friction = 10;  
 fixDef.restitution = 0.1;  
 fixDef.shape = new b2CircleShape(0.3)  
 // wheel1

var wheel1=world.CreateBody(bodyDef)  
 wheel1.CreateFixture(fixDef);  
 // wheel2  
 var wheel2=world.CreateBody(bodyDef)  
 wheel2.CreateFixture(fixDef);

// convex car body  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 bodyDef.position.Set(24,9)  
 // just change the fixDef.shape and keep other properties  
 fixDef.shape = new b2PolygonShape  
 fixDef.shape.SetAsArray([  
 new b2Vec2(1 , -1.2),  
 new b2Vec2(1.5, -0.5),  
 new b2Vec2(1.3 , 0),  
 new b2Vec2(-1.3, 0),  
 new b2Vec2(-1.5, -0.5),  
 new b2Vec2(-0.3 , -1.2)  
 ]);

 var car = world.CreateBody(bodyDef);  
 car.CreateFixture(fixDef);

// joints  
 var myjoint = new b2RevoluteJointDef();  
 myjoint.bodyA = car;  
 myjoint.bodyB = wheel1;  
 myjoint.localAnchorA.Set(-0.7,0);  
 myjoint.enableMotor = true;  
 myjoint.maxMotorTorque = 55;  
 myjoint.motorSpeed=-10;  
 world.CreateJoint(myjoint);

myjoint.bodyA = car;  
 myjoint.bodyB = wheel2;  
 myjoint.localAnchorA.Set(0.8,0);  
 world.CreateJoint(myjoint);  
 </code></pre>

Let’s look at the joint part starting from line 39, one joint usually connects two bodies, and you can use ‘<span style="text-decoration: underline;">localAnchor</span>‘ to specify where the joint is on that object. **Motor **is an interesting feature of joint, motorSpeed is in radian and clockwise direction. Notice that the car below isn’t able to climb to the top of the hill? That’s because the maxMotorTorque isn’t big enough. Btw don’t forget to add ‘ b2RevoluteJointDef = Box2D. Dynamics. Joints. b2RevoluteJointDef ‘ at the beginning.

<center>  
<iframe height="240" scrolling="no" src="https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/project/box2d_example/studynotes3.5.html" style="width: 600px; height: 330px;" width="320"></iframe></center> **Mouse Joint**

If you click on the car above, you can drag it and throw it anywhere. Isn’t it fun? Thanks to Mouse joint that makes it possible. But the way it’s set up is quite complex and requires deeper understanding of Box2d. Therefore I’ll just show you how to apply it for now and explain how it functions in the future.

**Step 1**, make sure you have these codes at the beginning.

<pre><code>

var b2Vec2 = Box2D.Common.Math.b2Vec2  
 , b2BodyDef = Box2D.Dynamics.b2BodyDef  
 , b2Body = Box2D.Dynamics.b2Body  
 , b2FixtureDef = Box2D.Dynamics.b2FixtureDef  
 , b2World = Box2D.Dynamics.b2World  
 , b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape  
 , b2CircleShape = Box2D.Collision.Shapes.b2CircleShape  
 , b2RevoluteJointDef=Box2D.Dynamics.Joints.b2RevoluteJointDef  
 , b2MouseJointDef = Box2D.Dynamics.Joints.b2MouseJointDef  
 , b2DebugDraw = Box2D.Dynamics.b2DebugDraw  
 , b2Fixture = Box2D.Dynamics.b2Fixture  
 , b2AABB = Box2D.Collision.b2AABB;

</code></pre>

**Step 2**, add the following codes after <span style="text-decoration: underline;">window.setInterval(update, 1000 / 60);</span>

<pre><code>

//mouse

var mouseX, mouseY, mousePVec, isMouseDown, selectedBody, mouseJoint;  
 var canvasPosition = getElementPosition(document.getElementById( “canvas” ));

document.addEventListener( “mousedown” , function(e) {  
 isMouseDown = true;  
 handleMouseMove(e);  
 document.addEventListener( “mousemove” , handleMouseMove, true);  
 }, true);

document.addEventListener( “mouseup”, function() {  
 document.removeEventListener( “mousemove” , handleMouseMove, true);  
 isMouseDown = false;  
 mouseX = undefined;  
 mouseY = undefined;  
 }, true);

function handleMouseMove(e) {  
 mouseX = (e.clientX – canvasPosition.x) / 30;  
 mouseY = (e.clientY – canvasPosition.y) / 30;  
 };

function getBodyAtMouse() {  
 mousePVec = new b2Vec2(mouseX, mouseY);  
 var aabb = new b2AABB();  
 aabb.lowerBound.Set(mouseX – 0.001, mouseY – 0.001);  
 aabb.upperBound.Set(mouseX + 0.001, mouseY + 0.001);

// Query the world for overlapping shapes.

selectedBody = null;  
 world.QueryAABB(getBodyCB, aabb);  
 return selectedBody;  
 }

function getBodyCB(fixture) {  
 if(fixture.GetBody().GetType() != b2Body.b2_staticBody) {  
 if(fixture.GetShape().TestPoint(fixture.GetBody().GetTransform(), mousePVec)) {  
 selectedBody = fixture.GetBody();  
 return false;  
 }  
 }  
 return true;  
 }

</code></pre>

**Step 3**, insert the following codes **inside** update() function:

<pre><code>

if(isMouseDown && (!mouseJoint)) {  
 var body = getBodyAtMouse();  
 if(body) {  
 var md = new b2MouseJointDef();  
 md.bodyA = world.GetGroundBody();  
 md.bodyB = body;  
 md.target.Set(mouseX, mouseY);  
 md.collideConnected = true;  
 md.maxForce = 300.0 * body.GetMass();  
 mouseJoint = world.CreateJoint(md);  
 body.SetAwake(true);  
 }  
 }

if(mouseJoint) {  
 if(isMouseDown) {  
 mouseJoint.SetTarget(new b2Vec2(mouseX, mouseY));  
 } else {  
 world.DestroyJoint(mouseJoint);  
 mouseJoint = null;  
 }  
 }  
 </code></pre>

**Step 4**, add following codes in the end:

<pre><code>  
 //helpers

//http://js-tut.aardon.de/js-tut/tutorial/position.html  
 function getElementPosition(element) {  
 var elem=element, tagname=””, x=0, y=0;

while((typeof(elem) == “object”) && (typeof(elem.tagName) != “undefined”)) {  
 y += elem.offsetTop;  
 x += elem.offsetLeft;  
 tagname = elem.tagName.toUpperCase();

if(tagname == “BODY”)  
 elem=0;

if(typeof(elem) == “object”) {  
 if(typeof(elem.offsetParent) == “object”)  
 elem = elem.offsetParent;  
 }  
 }

return {x: x, y: y};  
 }  
 </code></pre>

That’s it, have fun~ ^ ^

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

**旋转连接器**

我目前觉得“旋转连接器”是最有用的一种连接器，同时它的设置也非常简单。在此之前，我先将车身的形状改成凸多边形，并且将车轮创建为独立物体而不再仅仅是车的一部分。

<pre><code>

//  造车  
 //  造轮  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 var fixDef = new b2FixtureDef;  
 fixDef.density = 30;  
 fixDef.friction = 10;  
 fixDef.restitution = 0.1;  
 fixDef.shape = new b2CircleShape(0.3)  
 // 前轮

var wheel1=world.CreateBody(bodyDef)  
 wheel1.CreateFixture(fixDef);  
 // 后轮  
 var wheel2=world.CreateBody(bodyDef)  
 wheel2.CreateFixture(fixDef);

// 车身（凸多边形）  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 bodyDef.position.Set(24,9)  
 // 只重新定义fixDef中的形状，其他属性不变  
 fixDef.shape = new b2PolygonShape  
 fixDef.shape.SetAsArray([  
 new b2Vec2(1 , -1.2),  
 new b2Vec2(1.5, -0.5),  
 new b2Vec2(1.3 , 0),  
 new b2Vec2(-1.3, 0),  
 new b2Vec2(-1.5, -0.5),  
 new b2Vec2(-0.3 , -1.2)  
 ]);

var car = world.CreateBody(bodyDef);  
 car.CreateFixture(fixDef);

// 连接器  
 var myjoint = new b2RevoluteJointDef();  
 myjoint.bodyA = car;  
 myjoint.bodyB = wheel1;  
 myjoint.localAnchorA.Set(-0.7,0);  
 myjoint.enableMotor = true;  
 myjoint.maxMotorTorque = 55;  
 myjoint.motorSpeed=-10;  
 world.CreateJoint(myjoint);

myjoint.bodyA = car;  
 myjoint.bodyB = wheel2;  
 myjoint.localAnchorA.Set(0.8,0);  
 world.CreateJoint(myjoint);  
 </code></pre>

我们来看看从 39 行开始的连接器部分吧，一个连接器通常连接着两个物体。连接后你可以用 <span style="text-decoration: underline;">localAnchor</span>  来定义节点在各物体的具体什么位置。 马达是连接器中一个非常有趣的功能，马达速度是以弧度为单位并且顺时针为正。 看到下面的小车无法爬上陡峭的“山坡”了吗？ 这是因为马达的  <span style="text-decoration: underline;">maxMotorTorque</span>  设置的不够大。大家使用的时候别忘了在代码开头加上  b2RevoluteJointDef = Box2D. Dynamics. Joints. b2RevoluteJointDef  哦。

<center>  
<iframe height="240" scrolling="no" src="https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/project/box2d_example/studynotes3.5.html" style="width: 600px; height: 330px;" width="320"></iframe></center>**鼠标连接器** 

也许你还没发现，其实你完全可以用鼠标任意拖拽上面的小车哦！这都要归功于强大的鼠标连接器，不过它的创建方法如果现在就介绍还是过于复杂了，所以这里我只把它的使用代码贴一下，大家就勉为其难先知其然，迟些再知其所以然吧：

**步骤 1**, 先确认你的文件开头有下面几行代码：

<pre><code>

var b2Vec2 = Box2D.Common.Math.b2Vec2  
 , b2BodyDef = Box2D.Dynamics.b2BodyDef  
 , b2Body = Box2D.Dynamics.b2Body  
 , b2FixtureDef = Box2D.Dynamics.b2FixtureDef  
 , b2World = Box2D.Dynamics.b2World  
 , b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape  
 , b2CircleShape = Box2D.Collision.Shapes.b2CircleShape  
 , b2RevoluteJointDef=Box2D.Dynamics.Joints.b2RevoluteJointDef  
 , b2MouseJointDef = Box2D.Dynamics.Joints.b2MouseJointDef  
 , b2DebugDraw = Box2D.Dynamics.b2DebugDraw  
 , b2Fixture = Box2D.Dynamics.b2Fixture  
 , b2AABB = Box2D.Collision.b2AABB;

</code></pre>

**步骤 2**, 将下面的代码加到  <span style="text-decoration: underline;">window.setInterval(update, 1000 / 60);  </span>的后面：

<pre><code>

//鼠标

var mouseX, mouseY, mousePVec, isMouseDown, selectedBody, mouseJoint;  
 var canvasPosition = getElementPosition(document.getElementById(“canvas”));

document.addEventListener(“mousedown”, function(e) {  
 isMouseDown = true;  
 handleMouseMove(e);  
 document.addEventListener(“mousemove”, handleMouseMove, true);  
 }, true);

document.addEventListener(“mouseup”, function() {  
 document.removeEventListener(“mousemove”, handleMouseMove, true);  
 isMouseDown = false;  
 mouseX = undefined;  
 mouseY = undefined;  
 }, true);

function handleMouseMove(e) {  
 mouseX = (e.clientX – canvasPosition.x) / 30;  
 mouseY = (e.clientY – canvasPosition.y) / 30;  
 };

function getBodyAtMouse() {  
 mousePVec = new b2Vec2(mouseX, mouseY);  
 var aabb = new b2AABB();  
 aabb.lowerBound.Set(mouseX – 0.001, mouseY – 0.001);  
 aabb.upperBound.Set(mouseX + 0.001, mouseY + 0.001);

// 遍历寻找重合物体

selectedBody = null;  
 world.QueryAABB(getBodyCB, aabb);  
 return selectedBody;  
 }

function getBodyCB(fixture) {  
 if(fixture.GetBody().GetType() != b2Body.b2_staticBody) {  
 if(fixture.GetShape().TestPoint(fixture.GetBody().GetTransform(), mousePVec)) {  
 selectedBody = fixture.GetBody();  
 return false;  
 }  
 }  
 return true;  
 }

</code></pre>

**步骤 3**, 将下面的代码放进 update() 方法中:

<pre><code>

if(isMouseDown && (!mouseJoint)) {  
 var body = getBodyAtMouse();  
 if(body) {  
 var md = new b2MouseJointDef();  
 md.bodyA = world.GetGroundBody();  
 md.bodyB = body;  
 md.target.Set(mouseX, mouseY);  
 md.collideConnected = true;  
 md.maxForce = 300.0 * body.GetMass();  
 mouseJoint = world.CreateJoint(md);  
 body.SetAwake(true);  
 }  
 }

if(mouseJoint) {  
 if(isMouseDown) {  
 mouseJoint.SetTarget(new b2Vec2(mouseX, mouseY));  
 } else {  
 world.DestroyJoint(mouseJoint);  
 mouseJoint = null;  
 }  
 }  
 </code></pre>

**步骤 4**, 在文件最后加入下面的代码:

<pre><code>  
 //帮助

//http://js-tut.aardon.de/js-tut/tutorial/position.html  
 function getElementPosition(element) {  
 var elem=element, tagname=””, x=0, y=0;

while((typeof(elem) == “object”) && (typeof(elem.tagName) != “undefined”)) {  
 y += elem.offsetTop;  
 x += elem.offsetLeft;  
 tagname = elem.tagName.toUpperCase();

if(tagname == “BODY”)  
 elem=0;

if(typeof(elem) == “object”) {  
 if(typeof(elem.offsetParent) == “object”)  
 elem = elem.offsetParent;  
 }  
 }

return {x: x, y: y};  
 }  
 </code></pre>

大功告成了~  ^ ^

放一个无关紧要的有趣例子吧（没有节操的童鞋是看不到的哦）：

<center>  
<iframe height="240" scrolling="no" src="https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/project/box2d_example/temple(big).html" style="width: 600px; height: 450px;" width="320"></iframe></center>
