---
banner_img: https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/new_image.png
date: "2013-06-16 15:29:45"
index_img: https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/new_image.png
title:
    "\u7528PHP Imagick\u5728\u670D\u52A1\u5668\u7AEF\u5F97\u5230\u56FE\u7247\u5F71\
    \u5B50"
---

PHP 我过去一向是用到什么就查那部分的代码，改改直接用，一直未曾认真学习过。最近的 project 需要我在服务器端做一个小小的图片处理，于是这次我决定要好好搞懂用的代码！

But 结果发现其实就只是学会如何用 Imagick 库里的几个 method 而已，没什么算法需要自己想的。。╮(╯_╰)╭

其实想想用 photoshop 整天要抠图，自己写一个特别精准的抠图算法应该既有挑战性又很具实际意义，有空就写这个试试吧~

In short, 下面代码拿到 45 度角的阴影，半透明顺带模糊图片。

 <pre><code>
 $imgFile = ‘medium_squid.png’;//原图片  
 getShadow($imgFile);

 function getShadow($imgPath){  
     $im = new Imagick($imgPath);  
     $width = $im->getImageWidth();  
     $height = $im->getImageHeight();

     /* Set the image format to png */  
     $im->setImageFormat(‘png’);

     /* Fill new visible areas with transparent */  
     $im->setImageVirtualPixelMethod(Imagick::VIRTUALPIXELMETHOD_TRANSPARENT);

     /* Activate matte */  
     $im->setImageMatte(true);

     /* Control points for the distortion */  
     //图片四个顶点原来和改变后的位置  
     //下面的.7和.3使用45°对应的二分之根号二 约等于 0.707 约等于 0.7得到的  
     //想用其他的角度自己画个图算下就知道乘什么系数了。  
     $controlPoints = array( 0, 0,  
     $height*0.7, $height*0.3, 0, 
     $height, 0, $height, $width, 0,  
     $height*0.7+$width, $height*0.3,
     $width, $height,  
     $width, $height);

     /* Perform the distortion */  
     $im->distortImage(Imagick::DISTORTION_PERSPECTIVE, $controlPoints, true);

     $im->setImageBackgroundColor( new ImagickPixel( ‘black’ ) );

     /* Create the shadow */  
      //第一个参数是透明度  
     $im->shadowImage( 50, 30, 0, 0 );

     /* Ouput the image */  
     //被comment掉的是直接在网页上显示图片的方法  
     //header(“Content-Type: image/png”);  
     //echo $im;

    //这是保存这个影子图片的方法。  
     $im->writeImage(‘new_image.png’);

     $im->destroy();  
 }

</code></pre>

效果如下：

[![medium](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/medium-181x300.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/medium.png)没注意乌贼酱的原图已经有影子了= =[![new_image](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/new_image-300x168.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/new_image.png)

[![m_00000000-0b82-726a-2a63-1fff00000000-1](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000-1.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000-1.png) [![m_00000000-0b82-726a-2a63-1fff00000000shd](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000shd.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000shd.png) [![m_00000000-0b82-726a-2a63-1fff00000000-2](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000-2.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000-2.png) [![m_00000000-0b82-726a-2a63-1fff00000000shd-1](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000shd-1.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000shd-1.png) [![m_00000000-0b82-726a-2a63-1fff00000000](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/m_00000000-0b82-726a-2a63-1fff00000000.png) [![shd](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/shd.png)](https://architech-blog.s3-ap-southeast-1.amazonaws.com/content/images/uploads/2013/06/shd.png)

后记：

虽然上面的代码没问题，但在我需要用它的 project–FaceMap 里，影子相对于实体的定位比较麻烦，要设置一个 anchor point, 需要预先得到影子的尺寸还不太难，但 png 图片里的人物形象未必脚的位置正好可以碰到图片最低端, 不一定偏上了多少。 这个应该也是可以写代码解决的，找到有色块的位置然后 crop 生成新图片。

不过 google map android api 并没有提供影子这个功能，现在弄出来也只有浏览器上能显示，手机上还得手动想办法解决。。 所以最后我决定加影子这个美好愿望还是先放一放好了。╮(╯_╰)╭
