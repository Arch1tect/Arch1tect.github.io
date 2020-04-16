---
date: '2013-04-30 02:05:20'
title: "Minimum Spanning Tree Animation | \u6700\u5C0F\u751F\u6210\u6A39\u52D5\u756B"
---

Finished my Data Structure and Algorithm final exam today, I decided to code a small project just for fun!

Prim algorithm is used here but implemented in a rather slow way.

Since I limited the total node number to be less than 1000, that won’t be a problem.

(I still have two more exams and have to review tmr, so not much spare time really…)

And the animation is made with my favorite physics engine (Box2d).

 

First check out the static version below, it’s the traditional spanning tree.

<iframe frameborder="0" height="530" scrolling="no" src="/content/images/project/mst/mst_static.html" width="650"></iframe>

Then I come up with the idea that the edges can be elastic and nodes are movable…

I decide to name it “Dynamic Minimal Spanning Tree”!

Notice that the FPS can get quite slow in this version

<iframe frameborder="0" height="530" scrolling="no" src="/content/images/project/mst/mst_dynamic.html" width="650"></iframe>

That’s all, Let me know what you think of these tiny projects! ^ ^

---
考完了最重要的兩門，今晚不想複習了，於是做了上面關於最小生成樹的動畫。

最小生成樹的實際應用比方說：

大雪封路，清雪車的效率和數量都有限，我們想把城市裡的主要幾個樞紐之間的道路清理好，就要找到總路程最短，

同時可以連結所有樞紐的路徑 ﹣ 最小生成樹 （這個中文為啥要把spanning翻譯成“生成”，好奇怪）

Anyway，我發現圖論還是很有意思的，以後慢慢發現它的更多趣味吧~

就這樣啦~！

 

後記：

和wx吃飯的時候我給他看了這個小project，我們注意到這個Graph最終會聚到一個點，而這個點的位置恰恰應該是一開始質點系的質心位置。（高中好像叫質心不動定理？因為不受任何外力。） 同時因為我設置讓每個點隨機出現在長方形區域的任意位置，當點的數量足夠多，（一百左右開始比較準確）這個質點系的質心位置便應該與長方形的幾何中心相重合。所以最後Graph會會聚到長方形的正中心位置，為了驗證，我專門將起始點放置在了左下角而非原來的中心位置。

另外，當MST生成過程中，如果某（些）點與四壁發生了碰撞，則最終會聚位置不一定是長方形幾何中心，根據質心動能定理便可簡單推導出。

實驗結果與理論相符。 ：）


