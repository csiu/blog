---
layout: post
author: csiu
title: "Blog setup"
date: 2015-09-13
categories: update
tags: setup
header-img: img/home-bg.jpg
header-img-source: Ryan McGuire
---
For my first entry, it's only fitting to disclose how this blog was setup.
Previously, I was aware that this can be done using [GitHub Pages](https://pages.github.com), but it was only this weekend that I decided to sit down and do this.

The blog setup consists of 2 core steps: Setup and Customization.
Obviously, Setup is necessary whereas Customization is not
due to the list of default themes provided by GitHub.

# Setup
In Setup, you will need a GitHub account
to create a new GitHub repository named `username.github.io`
where `username` refers to your Github username.

Your site should then be found at **http://username.github.io**

To make the site less blank, you can then
[launch the automatic page generator](https://help.github.com/articles/creating-pages-with-the-automatic-generator/)
(found under Settings > GitHub Pages: Launch automatic page generator).

# Customize
In my cause, I didn't like the selection in the automatic page generator.
I wanted something different and so I turned to [Jekyll](https://jekyllrb.com),
a simple, blog-aware static site generator
[supported by GitHub Pages](https://help.github.com/articles/using-jekyll-with-pages).

Initially, I needed to download jekyll:
<pre>
~ $ gem install jekyll
</pre>

To test jekyll, I followed [jekyll's quick-start guide](http://jekyllrb.com/docs/quickstart/) and did:

<pre>
~ $ jekyll new myblog
~ $ cd myblog
~/myblog $ jekyll serve
</pre>

Going to **http://localhost:4000** would then present a preview of the new site.

## A different theme
To customize the theme, I picked [clean blog](http://startbootstrap.com/template-overviews/clean-blog/) from [jekyllthemes.org](http://jekyllthemes.org)

## A different header
To customize the header image, I used an image from [Ryan McGuire](http://www.gratisography.com/)'s collection.
In an [article by Casey Ark](http://www.entrepreneur.com/article/238646),
other amazing free stock photo websites can be found.

