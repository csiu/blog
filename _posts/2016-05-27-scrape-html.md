---
layout: post
author: "csiu"
date: 2016-05-27
title: "Scraping HTML"
categories: update
tags: setup
excerpt: "The concept is simple, but getting the data required a bit more work"
header-img-http: https://pixabay.com/static/uploads/photo/2015/10/19/13/36/extension-996004_960_720.jpg
header-img-source: RUINS@pixabay
---

In the [previous post]({{ site.baseurl }}/update/2016/05/22/noodlers-ink.html), I took rating data from [The Goulet Pen](http://www.gouletpens.com/bottled-ink/c/14/?sortBy=productName+asc&facetValueFilter=Tenant~Brand%3Anoodlers) website to look for the highest rated item matching a shortlist of items. The concept is simple, but getting the data required a bit more work.

Normally I would use Hadley Wickham’s [`rvest`](https://github.com/hadley/rvest) package to scrape websites with R, but I found that this method did not work: I could get the item names, but not the item ratings.

```r
library(rvest)

read_html(THE_GOULET_PEN_URL) %>%
  html_nodes("div.mz-productlisting") %>%
  html_text()
```

I was confused.

When I open the URL in a browser and inspect the elements, I could clearly see the ratings embedded in the HTML. And, not knowing any better, I then proceeded to try python’s [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).

```python
from bs4 import BeautifulSoup
from urllib import urlopen

f = urllib.urlopen(THE_GOULET_PEN_URL)
soup = BeautifulSoup(f)

soup.findAll("div", class_="mz-productlisting")[0].get_text()
```

Still nothing.

Eventually -- after opening the URL in a javascript disabled browser and not seeing any ratings -- I realized the ratings were dynamically generating by javascript.

Now that I knew what to look for (and finding Ross Kippenbrock's post on [Shot Blocking in the NHL Playoffs](http://blog.yhat.com/posts/hockey-shot-blocking.html)), I was able to scrape the javascript generated content using [`selenium`](http://selenium-python.readthedocs.io) and [`chromedriver`](http://chromedriver.storage.googleapis.com/index.html).

<script src="https://gist.github.com/csiu/7e942470f807aae5529e8eccfc3aea24.js"></script>
