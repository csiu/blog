---
layout: post
author: "csiu"
date: 2016-06-11
title: Perfectionism
categories: update
tags: data-analysis
excerpt: More girls than guys?
header-img-http: https://pixabay.com/static/uploads/photo/2015/02/13/14/38/pretty-woman-635258_960_720.jpg
header-img-source: jil111@pixabay
---

<style>
blockquote p {
    margin: 0;
    padding: 0;
    font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-style: normal;
    color: silver;
}
blockquote li {
    font-family: "Courier New", Courier, monospace;
    font-style: normal;
    color: silver;
}
</style>

About three weeks ago, I -- along with 34 other people -- attended an “Overcoming perfectionism: Bring more ease & success into your life” workshop.

> **2 futile formulas:**
>
> - Self worth = Ability = Performance
> - Ordinary = Not outstanding = Not loved

Of the 35 who attended, 11 were male and 24 were female.

> **3 types of perfectionism:**
>
> - Self-orientated
> - Other-orientated
> - Socially-orientated

Seeing as there were more females than males, I wondered whether there was significantly more females than males present at this event. In other words, are females more likely concerned with overcoming perfectionism?

> **3 types of thinking traps:**
>
> - All or nothing thinking
> - Should/Must thinking
> - Minimization/Magnification

## Some "simple" statistics

To test for equal turnout of males and females, we apply the [exact binomial test of goodness-of-fit](http://www.biostathandbook.com/exactgof.html) to calculate the probability of getting a result like the observed result if the null hypothesis was true.

```
##
## 	Exact binomial test
##
## data:  24 and 35
## number of successes = 24, number of trials = 35, p-value = 0.04096
## alternative hypothesis: true probability of success is not equal to 0.5
## 95 percent confidence interval:
##  0.5071200 0.8314828
## sample estimates:
## probability of success
##              0.6857143
```

Here, we calculated a p-value of 0.04 for equal turnout of males and females. Because this probability is small (i.e. below the usual significant level of 0.05), we reject the null hypothesis and conclude there was significantly more females than males present at this event.
