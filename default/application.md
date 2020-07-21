---
title: Basic Application Setup
publication_date: 2020-06-20
tags:
- core
- usage
- instructions
author: Brandon James
---

`core` is a simple, markdown based blogging framework. To use core, simply create a new subdirectory in your `core` folder. I usually call it `raw`, but you can give it any name you like as long as the `input_directory` is updated in `config.py` to point to the new folder instead of `default`. 

```
├── default
|── raw
├── __pycache__
├── static
│   ├── favicon
│   ├── images
│   │   └── post
│   └── rendered
├── templates

```

Put your markdown files and any embedded photos into the raw directory. Here's an example from [neverthenetwork.com](https://neverthenetwork.com)

```
raw/
├── about.md
├── automation_concurrency.md
├── automation_config.md
├── bfd.md
├── bitwise_subnetting.md
├── c_extension_notes.md
├── conft_snmp.md
├── fhrp_authentication.md
├── fhrp_diagram1.png
├── ITBlogAwards_2019_Badge-Finalist-BestNewcomer.png
├── linux_cli.md
├── lisp.md
├── lisp_overview.png
├── me.jpg
├── mod_acl.md
├── netwatch.md
├── neverthenetwork.md
├── ntnv2.md
├── rp_hash.md
└── wlc_cli.md
```