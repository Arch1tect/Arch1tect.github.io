---
date: '2012-12-05 17:19:54'
title: Big-O Notation Study Note
---

This will be the first post for my CS category. : )

##### Definition 1

> Let f and g be functions from the set of integers or the set of real numbers to the set of real numbers. We say that f (x) is O(g(x)) if there are constants C and k such that
> 
> |f (x)| ≤ C|g(x)|  
>  whenever x > k. [This is read as “f (x) is big-oh of g(x).”]
> 
>  

###### Remark: Intuitively, the definition that f (x) is O(g(x)) says that f (x) grows slower that some fixed multiple of g(x) as x grows without bound.

<div>
<b>Witnesses</b>

The constants C and k in the definition of big-O notation are called witnesses to the relationship f(x) is O(g(x)). To establish that f(x) is O(g(x)) we need only one pair of witnesses to this relationship. That is, to show that f (x) is O(g(x)), we need find only one pair of constants C and k, the witnesses, such that |f (x)| ≤ C|g(x)| whenever x > k.

Note that when there is one pair of witnesses to the relationship f (x) is O(g(x)), there are infinitely many pairs of witnesses. To see this, note that if C and k are one pair of witnesses, then any pair C′ and k′, where C < C′ and k < k′, is also a pair of witnesses, because |f (x)| ≤ C|g(x)| ≤ C′|g(x)| whenever x > k′ > k.

The big-O symbol is sometimes called a Landau symbol after the German mathematician Edmund Landau.

</div>

[![](/content/images/uploads/2012/12/Screen-Shot-2012-12-05-at-4.54.55-PM-300x93.png "Screen Shot 2012-12-05 at 4.54.55 PM")](/content/images/uploads/2012/12/Screen-Shot-2012-12-05-at-4.54.55-PM.png)

<div> 

[![](/content/images/uploads/2012/12/Screen-Shot-2012-12-05-at-4.55.45-PM-300x40.png "Screen Shot 2012-12-05 at 4.55.45 PM")](/content/images/uploads/2012/12/Screen-Shot-2012-12-05-at-4.55.45-PM.png)

</div> 

Suppose that f1(x) is O(g1(x)) and that f2(x) is O(g2(x)). Then (f1+f2)(x) is O(max(|g1(x)|, |g2(x)|)).

Suppose that f1(x) and f2(x) are both O(g(x)). Then (f1 + f2)(x) is O(g(x)).

Suppose that f1(x) is O(g1(x)) and f2(x) is O(g2(x)). Then (f1f2)(x) is O(g1(x)g2(x)).

 

[![](/content/images/uploads/2012/12/Screen-Shot-2012-12-05-at-5.25.04-PM-300x32.png "Screen Shot 2012-12-05 at 5.25.04 PM")](/content/images/uploads/2012/12/Screen-Shot-2012-12-05-at-5.25.04-PM.png)

All materials are from

<address>Discrete Mathematics and Its Applications : Kenneth H. Rosen</address>
