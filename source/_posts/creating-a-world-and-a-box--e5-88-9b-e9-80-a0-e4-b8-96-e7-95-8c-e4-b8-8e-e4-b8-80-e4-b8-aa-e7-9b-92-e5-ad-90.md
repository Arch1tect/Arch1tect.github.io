---
date: '2012-03-03 21:47:44'
title: "Creating a World and a Box | \u521B\u9020\u4E16\u754C\u4E0E\u4E00\u4E2A\u76D2\
  \u5B50"
---

Now we are ready to create our Box2d world. You will write a html file with *TextEdit* or *Notepad* or whatever you like.

我们马上就要开始创造Box2d world了！ 它将会是一个html文件， 你可以直接打开记事本或者其它随便什么顺手的文字处理工具。
![](/content/images/uploads/2012/03/box2ddiagramnew-1024x1024.jpg)
**Creating Box2d world**

     Remember the above diagram from last post? You can see that a world has two parameters which are <span style="text-decoration: underline;">gravity</span> and <span style="text-decoration: underline;">sleep</span>.  Gravity is self-evident, ‘sleep’ here means an object in this world will fall asleep if it’s not moving physically and there’s no other moving objects harass it for over 0.5 second (you can change this time as needed). We usually allow objects to sleep because when an object is sleeping it won’t be simulated by Box2d, so that energy of your device can be saved, meanwhile it can be woken up fast and easily.

  
` var world = new b2World(new b2Vec2(0,10), true);` 

     Believe it or not,  with this one line javascript code we just finish creating a Box2d world with gravity of 10m/s/s. And sleeping is allowed, that’s what ‘true’ in the parentheses means. Notice that gravity is set as a vector of (0,10)  instead of (0, -10), because in the coordinate system of Box2d, Y direction goes down. Box2D uses meters, kilograms, and seconds for units and radians for angles. What does ‘b2′ mean? It’s just a prefix to avoid name clashing. And you’ll see it everywhere soon.

**Creating a simple box**

     Again, look at the diagram above and see what’s inside the happy blue box. You can see that bodyDef and fixtureDef defines the object together.In ***bodyDef***, you can define the type of the object – either dynamic or static. The position of the body relative to the world is also decided in bodyDef. Then we use ***fixtureDef*** to define the properties of an object including density, friction and restitution, moreover, ***shape*** is also under the fixtureDef class and is used to define object’s shape and size. Now you should be able to understand how the following codes define a 1×1 box at the position of (2, 2).

<pre><code>  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody; //define object type  
 bodyDef.position.Set(2, 2); //define position

var fixDef = new b2FixtureDef;  
 fixDef.density = 10.0; //define density  
 fixDef.friction = 0.5; //define friction  
 fixDef.restitution =0.2; //define restitution

fixDef.shape = new b2PolygonShape; //define shape  
 fixDef.shape.SetAsBox(1, 1); //define size  
</code></pre>

     That’s all for creating a box? Almost, there is just one last step which is to add this box into the Box2d world we just created.

 
`world.CreateBody(bodyDef).CreateFixture(fixDef);`
     Well done! Wait, isn’t it a good idea to give this object a name, so we can find and manipulate it conveniently in the future. Alright, let’s just change the above code into this:

 `var happyBox = world.CreateBody(bodyDef);  
 happyBox.CreateFixture(fixDef);`

     Sweet, we have finished everything for now. Mr happyBox should be happy falling in our Box2d world, and you’ll be able to see how he’s doing in the following article. ^ ^

---

[![](/content/images/uploads/2012/03/box2ddiagramnew-1024x1024.jpg "box2ddiagramnew")](http://box2dweb.com/blog/2012/03/03/core-concepts-%e6%a0%b8%e5%bf%83%e6%a6%82%e5%bf%b5/box2ddiagramnew/)

**创造Box2d世界**

     还记得上面的图表吧？ 它告诉我们世界的定义主要包含重力与休眠两个参数。 重力毋需多说， “休眠”是指Box2d世界中的某物体如果超过0.5秒没有做物理运动，同时也没有别的运动物体与之接触， 它就会无聊得“睡着”（但是它不会变胖）。。。 0.5秒是默认时间，你可以随意修改。多数情况下我们允许物体休眠，因为当它们休眠时， Box2d会停止对它们的运算， 从而降低机器的负担。 而且即便睡着了，它们也灵敏不减。

  
 `var world = new b2World(new b2Vec2(0,10), true);`

     是的，仅上面这短短一行我们就完成了对一个新世界的定义： 这是一个重力竖直向下，大小等于10米每秒平方，并且允许物体睡觉的世界。重力是用矢量（0，10）定义的， 之所以不是（0，－10）是因为Box2d的坐标系中Y方向是向下的。Box2d使用米，千克，秒作为单位，用弧度来描述角的大小。那“b2” 又是什么意思呢？ 它只是一个用于避免此物理引擎中的名字和使用者其它文件的名字冲突的前缀，后面你会发现它到处都是，注意不要从右往左看它哦。至于括号里的“true”则表示允许物体睡觉。

**创造一个盒子**

请看看上图中那个快乐的蓝色盒子， 你会发现这个盒子是由 bodyDef 和 fixtureDef 共同定义的。 在bodyDef中，你可以设定物体的类型－动态的还是静态的， 你还可以设定物体的初始位置。fixtureDef则掌管物体的基本性质包括有密度、摩擦系数以及恢复系数等等，值得注意的是shape也在 fixtureDef下， 它决定物体的形状与大小。 好了， 现在你应该可以理解下面这段代码了，它定义了一个1×1大小的盒子，初始位置为（2，2）。

<pre><code>  
 var bodyDef = new b2BodyDef;  
 bodyDef.type = b2Body.b2_dynamicBody; //定义物体类型  
 bodyDef.position.Set(2, 2); //定义位置

var fixDef = new b2FixtureDef;  
 fixDef.density = 10.0; //定义密度  
 fixDef.friction = 0.5; //定义摩擦系数  
 fixDef.restitution =0.2; //定义恢复系数

fixDef.shape = new b2PolygonShape; //定义形状  
 fixDef.shape.SetAsBox(1, 1); //定义尺寸  
</code></pre>

     完成了？ 不， 还差最后一步， 我们要把这个定义好了的盒子添加进刚刚建好的那个世界中去。

 
 `world.CreateBody(bodyDef).CreateFixture(fixDef);`  
 

     这回的确大功告成了。可是等等， 如果我们给这个盒子起个名字， 以后在偌大的世界的茫茫“人”海中找起来就容易多了不是吗？ 我们只要把上面那行代码稍稍改进一下。
  
 `var happyBox = world.CreateBody(bodyDef);  
 happyBox.CreateFixture(fixDef);`  


     很好，任务圆满完成！ “快乐盒子” 童鞋现在应该正在 Box2d 世界中快乐的堕落着。 下文中我们就可以一睹他的庐山真面目了。 ^ ^ <span style="text-align: justify;"> </span>


