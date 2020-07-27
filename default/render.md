---
title: Markdown Renderer
publication_date: 2020-06-20
tags:
- core
- usage
- instructions
author: Brandon James
---

Core renders markdown through pandoc with the `--from=markdown-implicit_figures`[^1] argument. Pandoc renders markdown in a [pretty standard way](https://pandoc.org/MANUAL.html#pandocs-markdown). In general core just lets pandoc handle the conversion, but there are a couple of things that you should be aware of. 

1. Images - Any embedded images without a `/` in the path (ie are in the same folder as the markdown file) are updated to reflect the path that they'll reside in on the webserver.
2. Metadata - Certain meta tags are required for a post to be rendered. They are: title, publication_date, and author. tags and summary are optional meta tags. 
    - Leaving out any of the required tags will cause you file not to be rendered. This effectively prevents it from being published. I usually leave `publication_date` blank until I'm ready to publish. 
    - If tags isn't specified, the tag `unfiled` is added.
    - If a summary isn't provided, one is generated using the first paragraph. This summary is used both on your homepage and in search engine results. 
    - As an example, the following is the metadata block for this post. 

```
---
title: Markdown Renderer
publication_date: 2020-06-20
tags:
- core
- usage
- instructions
author: Brandon James
---
```

[^1]: This setting is configurable