

import json
from yaml import dump as yaml_dumps

foo = 1/0

# avoid running this script if possible
# because I'm manually updating old posts
with open('posts_before_2020.json') as f:
    data = json.load(f)
    for post in data:
        title = post['title']
        slug = post['slug']
        headers = {
            "date": post['created_at'],
            "title": title,
        }
        img = post['feature_image']
        if img:
            headers['index_img'] = img
            headers['banner_img'] = img
        try:
            md = json.loads(post['mobiledoc'])['cards'][0][1]['markdown']
        except:
            md = post['html']

        md = md.replace('{{', '(').replace('}}', ')')
        new_f = open(f"source/_posts/{slug}.md", "w")
        content = '---\n' + yaml_dumps(headers) + '---\n' + md
        new_f.write(content)

    pass
