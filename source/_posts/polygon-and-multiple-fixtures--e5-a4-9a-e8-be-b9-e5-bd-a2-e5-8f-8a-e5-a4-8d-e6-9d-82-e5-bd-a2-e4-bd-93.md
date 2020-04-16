---
date: "2012-03-04 03:00:17"
title: "Polygon and Multiple Fixtures | \u591A\u8FB9\u5F62\u53CA\u7EC4\u5408\u4F53"
---

The previous two posts are supposed to show you the basic structure of creating world and objects in Box2d, it might take you some time to understand. But since they are so crucial that you have to grasp them in order to explore the upcoming cool features of Box2d. In this post, we are going to further study **fixture**.

在前两篇文章中我们学会了最重要的创世与造物，同时 Box2d 的基本运作方式已经介绍完了，倘若这时候你感觉到了吃力，那不妨花些时间好好巩固一下前面的内容。如果没问题，我们就继续深入学习 **fixture**。

**Polygon**

Following is the code of how an object with polygon shape is created, instead of <span style="text-decoration: underline;">SetAsBox</span>, we use <span style="text-decoration: underline;">SetAsArray</span> this time, the position of each polygon vertex is represented as a vector pointing from the position of the object to the <span style="color: #ff0000;">relative</span> position of vertex. (Notice I said ‘<span style="color: #ff0000;">relative</span>‘, the vector here is always relative to the position of the object not to the world. ) The default limit of vertex is eight and you should define them in clockwise order. And **you should never create concave polygons**.

<pre><code>  
 fixDef.shape = new b2PolygonShape;  
 fixDef.shape.SetAsArray([  
 new b2Vec2(0.05 , 0),  
 new b2Vec2(0.35, 0.15),  
 new b2Vec2(0.5, 0.2),  
 new b2Vec2(-1.5 , 1.2),  
 new b2Vec2(-0.35, 0.15),  
 new b2Vec2(-1.05, 0.0),  
 ]);  
 </code></pre>

<center>  
<iframe height="240" scrolling="no" src="/content/images/project/box2d_example/studynotes2.html" style="width: 610px; height: 500px;" width="320"></iframe></center>     You know what? Since I never like rules, I’m determined to make concave polygons. Now you can see how they are behaving weirdly above, the concave polygon sometimes goes into the ground and walls when it’s bouncing. See the body of that car on the right is also concave polygon? Now you know you should always stick to convex polygon.

About the car, did I mention that **one object can have multiple fixtures**?

**Multiple Fixtures**

The codes below are for creating the above car. It’s quite simple. Just create multiple fixtures then add them to the object. For circle shapes, you can use <span style="text-decoration: underline;">SetLocalPosition</span> with a vector (again relative to the position of the object not to the world) to indicate where this shape should go. For box shapes, you can use SetAsOrientedBox to do that. But for polygons that are defined by vertices, there isn’t any method to do that since the vertices are already relative to the position of the object. And a polygon defined by vertices doesn’t really have a position. (It has mass center position though)

<pre><code>  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 bodyDef.position.Set(12,6.5)

// ‘fixDef’ defines the car body  
 var fixDef = new b2FixtureDef;  
 fixDef.density = 30;  
 fixDef.friction = 0.1;  
 fixDef.restitution = 1;  
 fixDef.shape = new b2PolygonShape  
 fixDef.shape.SetAsArray([  
 new b2Vec2(0.5 , -1),  
 new b2Vec2(1, -0.5),  
 new b2Vec2(1.5, -0.5),  
 new b2Vec2(1.5 , 0),  
 new b2Vec2(-1.5, 0),  
 new b2Vec2(-1.5, -0.5),  
 new b2Vec2(-1., -0.5),  
 new b2Vec2(-0.5 , -1)  
 ]);

var wheel1 = new b2FixtureDef;  
 wheel1.shape = new b2CircleShape(0.2)  
 wheel1.shape.SetLocalPosition( new b2Vec2(-0.8 ,0.1))

var wheel2 = new b2FixtureDef;  
 wheel2.shape = new b2CircleShape(0.2)  
 wheel2.shape.SetLocalPosition( new b2Vec2(0.8 ,0.1))  
 //notice properties such as density isn’t defined,  
 //then value from fixDef above will be used.

var car = world.CreateBody(bodyDef)

//add three components above to the ‘car’ object  
 car.CreateFixture(fixDef);  
 car.CreateFixture(wheel1);  
 car.CreateFixture(wheel2);  
 </code></pre>

Click ‘restart’ to watch again, see that the wheels of the car aren’t rotating at all? Some people may guess that’s because they are overlapping with the car body. That’s a good guess but the truth is, as fixtures, wheels are totally fixed to the object as a whole, and can’t have any independent motion. Therefore **joint** is what you need to create a car with rolling wheels.

Btw don’t  worry too much about how they look aesthetically now, DebugDraw is just for checking if physics is working right. You can attach fancy images  to them easily later.

---

**多边形**

下面就是创建多边形物体的代码了，这次我们用 SetAsArray 的方法而不再是简单的 SetAsBox。多边形的每个顶点的位置都是用相对于物体位置的向量的形式来定义的。（注意“相对”二字，这里定义顶点的位置是相对于物体自身而非相对于世界）Box2dweb 默认不能创建超过 8 个顶点的多边形， 并且必须按顺时针的顺序定义它们的相对位置。还有，**不允许创建凹多边形。**

<pre><code>  
 fixDef.shape = new b2PolygonShape;  
 fixDef.shape.SetAsArray([  
 new b2Vec2(0.05 , 0),  
 new b2Vec2(0.35, 0.15),  
 new b2Vec2(0.5, 0.2),  
 new b2Vec2(-1.5 , 1.2),  
 new b2Vec2(-0.35, 0.15),  
 new b2Vec2(-1.05, 0.0),  
 ]);  
 </code></pre>

<center>  
<iframe height="240" scrolling="no" src="/content/images/project/box2d_example/studynotes2.html" style="width: 610px; height: 500px;" width="320"></iframe></center>     突然想到了鲁鲁修的叛逆，于是我故意违规创建了一个样子奇怪的凹多边形。你可以看见它在上面蹦跳的时候经常会一头扎进墙壁里或者窜到地下，完全无视碰撞的规矩。发现右边的小车车身也是凹多边形了吗？ 现在你应该看到创建凹多边形的不良后果了。

那个小车是怎么创建的？我好像忘了告诉大家**一个物体可以由多个形状组成**了。 ＝ ＝

**组合体**

下面就是创建小车童鞋的代码，其实很简单。 创建好几个形状后把它们加进物体中即可， 创建圆形形状的时候可以用 SetLocalPosition 来定义它在物体中具体什么位置，这和之前创建多边形顶点的时候很类似，都是相对位置。如果不设置就默认为（0，0）－－等同于物体自身的位置。创建简单的盒子形状则可以用 SetAsOrientedBox， 但是用顶点的方法定义出来的多边形却没有类似的命令。 原因是这种多边形本身就是由相对物体位置的顶点定义的，可以说它本身作为一个整体并没有一个单独存在的位置。（但是它的质心位置还是可以得到的）

<pre><code>  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody;  
 bodyDef.position.Set(12,6.5)

// ‘fixDef’ 定义车身  
 var fixDef = new b2FixtureDef;  
 fixDef.density = 30;  
 fixDef.friction = 0.1;  
 fixDef.restitution = 1;  
 fixDef.shape = new b2PolygonShape  
 fixDef.shape.SetAsArray([  
 new b2Vec2(0.5 , -1),  
 new b2Vec2(1, -0.5),  
 new b2Vec2(1.5, -0.5),  
 new b2Vec2(1.5 , 0),  
 new b2Vec2(-1.5, 0),  
 new b2Vec2(-1.5, -0.5),  
 new b2Vec2(-1., -0.5),  
 new b2Vec2(-0.5 , -1)  
 ]);

var wheel1 = new b2FixtureDef;  
 wheel1.shape = new b2CircleShape(0.2)  
 wheel1.shape.SetLocalPosition( new b2Vec2(-0.8 ,0.1))

var wheel2 = new b2FixtureDef;  
 wheel2.shape = new b2CircleShape(0.2)  
 wheel2.shape.SetLocalPosition( new b2Vec2(0.8 ,0.1))  
 //注意两个车轮的具体属性都没定义，Box2d会自动重复使用上面fixDef所定义的

var car = world.CreateBody(bodyDef)

//将上面定义的三个组件加入到物体‘car’中  
 car.CreateFixture(fixDef);  
 car.CreateFixture(wheel1);  
 car.CreateFixture(wheel2);  
 </code></pre>

按‘restart’再看一次，是不是发现小车的轮子根本没有转？有的童鞋可能以为是因为轮子和车身重叠导致它们不能转。不错的猜想，但事实上，在这里轮子是‘car’不可分割的一部分，任何一丁点独立的运动都是不可能发生的。因此无论你将它定义在一个离车身多远的位置，它都无法自转。如果你想拥有能转的轮子，你需要的是－－**节点**。

顺便一提，暂且别过多考虑 Debugdraw 绘制的东西是否美观，它只是暂时用来显示物理模拟的情况。最后你大可华丽丽地贴华丽的图。
