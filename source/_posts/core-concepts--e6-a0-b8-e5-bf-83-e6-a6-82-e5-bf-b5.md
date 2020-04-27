---
banner_img: https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/03/box2ddiagramnew.jpg
date: "2012-03-03 21:47:18"
index_img: https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2012/03/box2ddiagramnew.jpg
title: "Core Concepts | \u6838\u5FC3\u6982\u5FF5"
---

**Shape**, **body**, **fixture**, **joint** and **world** are the five concepts I find most important. Erin Catto’s definitions of these concepts in his [manual](http://box2d.org/manual.pdf "manual") are really terse and clear to me so I decide to quote them below:

**形状**、**刚体**、**定制器**、**连接器**以及**世界**在我看来是 Box2d 中最重要的五个概念。Erin Catto 在他的[手册](http://box2d.org/manual.pdf "手册")中对这几个概念的定义字字珠玑，因此我决定在下面直接引用他的原话：

> **shape**  
>  A 2D geometrical object, such as a circle or polygon.
>
> **rigid body**  
>  A chunk of matter that is so strong that the distance between any two bits of matter on the chunk is constant. They are hard like a diamond. In the following discussion we use body interchangeably with rigid body.
>
> **fixture**  
>  A fixture binds a shape to a body and adds material properties such as density, friction, and restitution.
>
> **joint**  
>  This is a constraint used to hold two or more bodies together. Box2D supports several joint types: revolute, prismatic, distance, and more. Some joints may have limits and motors.
>
> **world **  
>  A physics world is a collection of bodies, fixtures, and constraints that interact together. Box2D supports the creation of multiple worlds, but this is usually not necessary or desirable.

It’s pretty easy to understand right? The relation between these concepts can be tricky though. Therefore I made the diagram below to illustrate how a box is defined in a box2d world. Please take a careful look at it and I’ll further explain this in my next article.

![](http://box2dweb.com/core-concepts-%e6%a0%b8%e5%bf%83%e6%a6%82%e5%bf%b5/box2ddiagramnew/)

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

题外话：我在考虑 fixture 应该怎么翻译成中文的时候居然在百度文库里搜出了一篇 Box2d C++版手册的全文翻译，可是仔细一看却发现那份翻译材料中竟只字未提 fixture，原来那个老版本中 fixture 的功能都放在了 shape 里面，足见不同版本不同语言下的 Box2d 还是不尽相同的。最后我决定将 fixture 翻译为“定制器”，它主要掌管形状，密度、摩擦系数还有恢复系数等等。

> <span style="color: #000000;">**形状**  
> </span>一个 2D 的几何图形，比方说圆形或者多边形。
>
> **刚体**  
>  无比坚硬的物体，其中的任意两块物质间的距离都是固定不变的，就像钻石般坚硬。 在下文的讨论中我们直接称它物体。
>
> **定制器**  
>  定制器用于将一个特定的形状赋予物体同时它也用于定义物体的性质，比如：密度、摩擦系数还有恢复系数。
>
> **连接器  
> **连接器提供用于固定两个或更多物体的约束。 Box2D 支持多种连接器：旋转、平移、距离等等。 其中一些连接器可以设置限制与马达。
>
> **世界**  
>  一个物理世界就是一个各物体、定制器以及约束之间互动的集合。 Box2D 支持多个世界的创建，但一般情况下这既没必要也不适宜。

我想这几个概念应该都不难理解。不过这些概念之间的关系估计对于刚接触 Box2d 的朋友则没有那么容易理清。因此我画了下面这个简单的图表，它大概阐释了一个最基本的盒子是如何被定义在 Box2d 的物理世界中的。请狠狠看它几眼，我会在下文继续详细地介绍它。

![](http://box2dweb.com/core-concepts-%e6%a0%b8%e5%bf%83%e6%a6%82%e5%bf%b5/box2ddiagramnew/)
