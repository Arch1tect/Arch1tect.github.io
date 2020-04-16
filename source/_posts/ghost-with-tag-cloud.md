---
banner_img: /content/images/2015/11/Screenshot--4-.png
date: '2015-11-07 21:13:05'
index_img: /content/images/2015/11/Screenshot--4-.png
title: Ghost with Tag Cloud
---
Ghost is great, lightning fast and doesn't over complicate anything. However, to me there are three crucial parts missing:

1. Search 
2. Comment
3. Tag Cloud

It seems the Ghost development team has been looking for help with  implementing the search functionality eagerly and they suggest Ghost users to use disqus for comment system. But I don't see any news about adding the tag cloud any time soon, so I found myself the following code to add this functionality.

Create `core/server/helpers/tag_cloud.js` with content below:


<pre><code>
// # Tag cloud helper
// Usage: `(tag_cloud limit="5")`
// Defaults to limit="5"

var _               = require('lodash'),
    template        = require('./template'),
    config          = require('../config'),
    api             = require('../api'),
    tag_cloud;

tag_cloud = function (options) {
    var tagCloudOptions = (options || {}).hash || {};
    var limit = (_.has(tagCloudOptions, 'limit') && !/all/i.test(tagCloudOptions.limit))? parseInt(tagCloudOptions.limit, 10) : 'all';

    tagCloudOptions = _.pick(tagCloudOptions, ['limit']);
    tagCloudOptions = {
        limit: 'all',
        include: ['post_count'].join(','),
        context: 'internal'
    };

    return api.tags.browse(tagCloudOptions).then(function(tags){
        var sortedTags = _.sortBy(tags.tags, 'post_count').reverse();

        if(limit !== 'all') {
            sortedTags = sortedTags.slice(0, limit);
        }

        sortedTags.forEach(function(){
            this.url = config.urlFor('tag', {tag: this}, false);
        });

        return template.execute('tag_cloud',  {tags:sortedTags});
    });
};

module.exports = tag_cloud;




</code></pre>

Create `core/server/helpers/tpl/tag_cloud.hbs` with content below:
<pre><code>
&lt;ul class="tag-cloud">  
    (#foreach tags)
    &lt;a href="(url)" class="tag-item">(name)&lt;span class="post-count">(post_count)&lt;/span>&lt;/a>
    (/foreach)
&lt;/ul> 
</code></pre>

Add `coreHelpers.tag_cloud = require('./tag_cloud');` and `registerAsyncThemeHelper('tag_cloud', coreHelpers.tag_cloud);` to `core/server/helpers/index.js`

Check [here](https://github.com/ghostchina/Ghost-zh/blob/master/core/server/helpers/index.js) to see the right place to add these two lines.


Finally place `(tag_cloud limit=10)` in the theme you are using. (10 is the number of tags you want to show)  

This is how my tag cloud look, you can style it the way you want.
![](/content/images/2015/11/Screenshot--4-.png)


The code in this post is all taken from [GhostChina](http://www.ghostchina.com/output-tag-cloud/). 




 