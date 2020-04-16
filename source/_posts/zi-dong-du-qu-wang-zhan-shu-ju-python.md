---
date: '2015-10-29 06:52:09'
title: "\u81EA\u52A8\u6293\u53D6\u7F51\u7AD9\u6570\u636E (Python)"
---
Luna最近做研究的一个sub task是要从某个基因网站上读取40个结果记录下来，这个过程非常枯燥，而且人工去做又容易出错。于是我用Python写了下面的程序帮她完成这个任务。


<pre><code>
import urllib.request
import codecs
import json
import traceback


#put your rs numbers into the list below
rsList = [10994397, 10994398, 10994399, 10994400, 10994401, 10994402]

for rs in rsList:
    print ('rs: ', rs, end="\t")
    url = 'http://www.ncbi.nlm.nih.gov/projects/SNP/snp_gene.cgi?rs='+str(rs)+'&connect='
    try:
        with urllib.request.urlopen(url) as response:
            
            reader = codecs.getreader("utf-8")
            obj = json.load(reader(response))
            print ('Chr Pos: ', obj['assembly']['GRCh37.p13'][0]['chrPosTo'])
            
    except Exception: #error handling
        print ('Failed because: ', traceback.format_exc())
</code></pre>

程序不难写，因为地址返回的是JSON格式，所以可以很方便的找到需要的数据。然而一开始要找到这个返回JSON的地址却不容易，因为Luna本来是在另外一个主页面进行的搜索，她需要的这个数据是那个页面发出的20多个request中的一个，而Chrome的dev tool的Network tab貌似不能直接在Request的Reponse中查找内容。。。