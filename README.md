# Git-Crawler-Using-Scrapy

To Run this Project we need Scrapy installed in  out Linux system , For that
we can do this

1) Import the GPG key used to sign Scrapy packages into APT keyring:

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7

2) Create /etc/apt/sources.list.d/scrapy.list file using the following command:

echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list

3) Update package lists and install the scrapy-0.24 package:

sudo apt-get update && sudo apt-get install scrapy-0.24

Or u can follow  this link - http://doc.scrapy.org/en/latest/topics/ubuntu.html#topics-ubuntu


After installing create project ,write Items and Spiders and extract data  which u want

-> Creating a project (link - http://doc.scrapy.org/en/latest/intro/tutorial.html)

Before you start scraping, you will have to set up a new Scrapy project. Enter a directory where you’d like to store your code and run:

scrapy startproject tutorial

This will create a tutorial directory with the following contents:

tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
            ...



-> Define Item (http://doc.scrapy.org/en/latest/intro/tutorial.html)
-> define Spieders (http://doc.scrapy.org/en/latest/intro/tutorial.html)
-> Then crawling 

  	To put our spider to work, go to the project’s top level directory and run:

	scrapy crawl dmoz


For more information go to scrapy tutorials page


