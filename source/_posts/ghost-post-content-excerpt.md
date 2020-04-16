---
date: '2015-11-23 15:41:02'
title: Ghost post content excerpt without image
---
I don't like how the built-in `excerpt` helper of Ghost strips tags and styles. Therefore I prefer using the `content` helper with limit on length of characters to output instead of using `excerpt`. 
However, when a post contains multiple images, I want to see at most one image per post before opening the post, otherwise the excerpt of one post can take up a lot of space if it has many images.

This requires some hacking in the code. The content helper is [here](https://github.com/TryGhost/Ghost/blob/master/core/server/helpers/content.js), as you can see, when there's limit in words or characters, it uses a library called [downsize](https://www.npmjs.com/package/downsize )

The **Downsize** library is located at `/var/www/ghost/node_modules/downsize`

There's a switch case for `<` in the main parsing loop. I added some code to detect image tag and stop outputting content once an `<img>` tag is found:
 
    ...
    switch (text[pointer]) {

                case "<":
                    // Ooh look — we're starting a new tag.
                    // (Provided we're in uninitialised state and the next
                    // character is a word character, explamation mark or slash)

                    if (parseState === PARSER_UNINITIALISED &&
                        text[pointer + 1].match(/[a-z0-9\-\_\/\!]/)) {
                        if (isAtLimit()) {
                            exit = true;
                            break;
                        }
                   if(text.substring(pointer+1, pointer+4)==="img") {
                            exit = true;
                            parseState = PARSER_TAG_COMMENCED;
                            break;
                        }
                        parseState = PARSER_TAG_COMMENCED;
                        tagBuffer += text[pointer];
                    }

                    break;

                case "!":
                ...

Now no images from a post will output when using `content` helper with limit of words or characters. This won't affect the post cover image though, which isn't part of the post content.
 
I think **Downsize** library can be improved, it would be great if it can work for different languages at the same time, because I sometimes post in English and sometimes Chinese. The real length of 50 words in English and 50 words in Chinese are very different. And when I have a few English words in a Chinese post and I use character limit, English words are cut in the middle. Maybe I myself can improve this library or build a better one in the future.