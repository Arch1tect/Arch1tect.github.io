---
date: '2015-10-27 19:56:00'
title: Syntax Highlighting with Highlight.js
---
I notice that the grayliner theme I'm using loads this highlight.js library which seems to be able to detect what language I'm typing in automatically and highlight syntax according to that specific language. Let's see how it looks.

Just wrap the code in &lt;pre&gt; &lt;code&gt; &lt;/code&gt; &lt;/pre&gt;


C++
<pre><code>
#include <iostream>

int main()
{
    std::cout << "Hello, world!\n";
}

</code></pre>

Java
<pre><code>
public class HelloWorld {

    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        System.out.println("Hello, World");
    }

}
</code></pre>

JavaScript
<pre><code>
alert('Hello, World!')
</code></pre>

Python
<pre><code>
print("Hello, world")
</code></pre>

---
The result looks pretty good, except &lt;iostream&gt; is swallowed in my C++ snippet, probably by ghost not highlight.js. I can change the tags into `&lt;` and `&gt;` manually, not sure if there's better way. 