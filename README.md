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
