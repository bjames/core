---
title: Nginx Server Setup
publication_date: 2020-06-20
tags:
- core
- usage
- instructions
author: Brandon James
---

The following is based on the [uWSGI instructions found on digital ocean's blog](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04). At present these are rough notes and will be fully fleshed out as part of a future release. 

This website is hosted on a $5/mo digital ocean droplet running Ubuntu 18.04.3

1. Follow the initial server setup instructions [here](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04). Be sure to actually read the instructions. _Don't just copy and paste_.
2. Follow the uWSGI setup instructions [here](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04). _Read the following before step 2_:
- Step 2, 3 and 4 of the of the uWSGI setup should be skipped and replaced with the following. Note that these steps should be performed with a user other than root.
    1. Clone `core` `git clone https://github.com/bjames/core`. I usually just clone it into my service account's home directory
    2. cd into the `core` directory and create a new virtual environment. `python3.6 -m venv venv`
    3. Install requirements `venv/bin/python3 -m pip install -r requirements.txt`
- When performing step 5 and 6 of the uWSGI setup use `core` instead of myproject
    - As an example, `core.service` on this site looks like the following:
    ```
    [Unit]
    Description=uWSGI instance to serve core
    After=network.target

    [Service]
    User=core
    Group=www-data
    WorkingDirectory=/home/core/core
    Environment="PATH=/home/core/core/core/bin"
    ExecStart=/home/core/core/venv/bin/uwsgi --ini core.ini

    [Install]
    WantedBy=multi-user.target
    ```

    