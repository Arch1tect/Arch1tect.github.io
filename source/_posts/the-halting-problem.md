---
date: '2013-03-13 04:01:08'
title: The Halting Problem
---

<iframe allowfullscreen="" frameborder="0" height="315" src="http://www.youtube.com/embed/fsE1bFWXlJQ" width="560"></iframe>  
 ATM= { <m,w> | M is a TM and M accepts w}  
 Theorem: ATM is undecidable.  
 Proof:  
 Assume ATM is decidable.  
 Suppose H is a decider for ATM.  
 H(<m,w>) = { accept if M accepts w, reject otherwise }  
 Construct a new TM D that calls H to determine what M does when M is its own input.  
 D = “On input :  
 Run H on input <m, <m=””> >.  
 Output the opposite of what H outputs.  
 Example of D:  
 D() = { accept if M does not accept  
 {reject if M accepts  
 Run D with itself as input:  
 D() = {accept if D does not accept  
 {reject if D accepts  
 No matter what D does, it is forced to do the opposite ⇒ contradiction.  
 Thus, neither D nor H can exist.  
 Therefore, ATM is undecidable.


