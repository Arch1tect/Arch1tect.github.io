---
date: '2015-11-02 06:46:50'
title: Migrate images from Wordpress to Ghost without 3rd party hosting
---
Ghost made it easy to migrate posts from Wordpress through some json import/export, however, the images can't be migrated that way. I found some tutorials about uploading images to 3rd party like Cloudinary and AWS S3. But I don't want to go to 3rd party at all. This is how I managed to migrate my images to Ghost:

I copied my images from my Wordpress site at `/wp-content/uploads` and pasted to Ghost at `/content/images`, now the entire `uploads` folder is sitting at `/content/images/uploads` under Ghost folder.

Because the image links in the posts were migrated as they were, they still point to the location at Wordpress site, i.e.
`http://oldWPSite.com/wp-content/uploads/2001/01/abc.jpg` 
, and the new address I want it to point to is
`http://newGhostSite.com/content/images/uploads/2001/01/abc.jpg`

Therefore, the solution is very clear now. I just need to replace the old links with new links. This can be done by running some simple SQL queries. I did it with the code below:

<pre><code>
update posts 
set markdown= replace(markdown, 'http://oldWPSite.com/wp-content/', '/content/images/');

update posts 
set html= replace(html, 'http://oldWPSite.com/wp-content/', '/content/images/');

update posts 
set image= replace(image, 'http://oldWPSite.com/wp-content/', '/content/images/');

</code></pre>

(Before you run this script, open the sqlite database with sqlite3 first, the database is located at `/content/data/`)

Now you should be able to shut down the old Wordpress site safely.


Update 2019/09
table schema has changed, update `html` and `mobiledoc` columns instead!
