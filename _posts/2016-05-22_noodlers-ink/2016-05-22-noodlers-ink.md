---
layout: post
author: "csiu"
date: 2016-05-22
title: "Rating Noodler's Ink"
categories: update
tags: data-analysis
excerpt: "I find myself wanting a new ink for my fountain pen, but the problem I have is that I can't decide on which one."
header-img-http: https://pixabay.com/static/uploads/photo/2014/09/15/22/23/fountain-pen-447576_960_720.jpg
header-img-source: Andrys@pixabay
---

> A human being is a deciding being.<br>
> -- Viktor E. Frank

I find myself wanting a new ink for my fountain pen, but the problem I have is that I can't decide on which one.

Looking at a [2012 comparison of ink prices per volume](http://www.marcuslink.com/pens/ink/thebrands.html), Noodler's ink would be the most economical choice. In this line, there are [128 different inks with various ink properties](http://noodlersink.com/noodlers-ink-properties/) such as:

- **Bulletproof**: whether the ink is resistant to UV, industrial solvents, or bleaching agents
- **Eternal**: whether the ink is fade resistant -- good for archival purposes
- **Fluorescent**: whether the ink glows under UV light
- **Forgery Resistant**: whether the ink is impervious to lasers, alcohols, or solvents -- ideal for security documents
- **Freeze Resistant**: whether the ink resists freezing at extremely low temperatures
- **Lubricated**: whether the ink is lubricated (for use in piston mechanism)
- **Water Resistant**: whether the ink is waterproof

## Different inks have different properties

<img src="{{ site.baseurl }}/img/figure/2016-05-22/plot-ink-property-1.png" title="" alt="" width="672" />

In the plot, we can see the different values a property can take; and if we consider all possible combinations, there will be 4x4x4x4x2x3x4 = 6144 possibilities. Fortunately, I am able to narrow down the combination of properties to 27 choices, for I want an ink that:

1. is (or at least is partially) bulletproof,
2. will not [fade](http://hudsonvalleysketches.blogspot.ca/2012/12/lightfastness-test-results-on-noodlers.html), and
3. is (or at least is partially) waterproof

## Shortlist of 43 inks

After filtering Noodler's list of 128 inks, I am left with 43 matching inks.

<font color="silver"><em>&#35;41 Brown, 54th Massachusetts, Air Corp Blue Black, Bad Belted Kingfisher, Bad Black Moccasin, Bad Blue Heron, Bad Green Gator, Black, Blackrase, Blue Ghost, Bluerase, Blue Upon the Plains of Abraham, Dostoyevsky, Eel Black, El Lawrence, Empire Red, Fox Red, General of the Armies, Heart of Darkness, Henry Hudson Blue, Hunter Green, Kung Te-Cheng, La Reine Mauve, Lexington Gray, Luxury Blue, Manhattan Black, Manjiro Nakahama Whaleman's Sepia, Mata Hari's Cordial, Pasternak, Periwinkle, Polar Black, Polar Blue, Polar Brown, Polar Green, Rachmaninoff, Raven Black, Rome Burning, Socrates, Tchaikovsky, Upper Ganges Blue, Whiteness of the Whale, X-Feather, Year of the Golden Pig</em></font>

This is still a lot. I now need a way to prioritize this list and one way to do so is to consider [The Goulet Pen](http://www.gouletpens.com/bottled-ink/c/14/?sortBy=productName+asc&facetValueFilter=Tenant~Brand%3Anoodlers) [ratings \(taken on May 22, 2016\)](https://gist.github.com/csiu/7d53c19edc8ff10798aa773ac3508974).

## Ink ratings from The Goulet Pen

On the website, Goulet lists 129 bottles of Noodler's inks, 14 of which are duplicated in 3oz and 4.5oz options.

<img src="{{ site.baseurl }}/img/figure/2016-05-22/plot-dups-1.png" title="" alt="" width="672" />

When tested for whether the ratings were higher in 4.5oz option vs 3oz option, we found no significant differences (p-value = 0.4239502).

- H<sub>o</sub> : No difference in ratings between the 4.5oz group and the 3oz group
- H<sub>a</sub> : Ratings in the 4.5oz group is higher than the 3oz group

```
##
## 	Exact binomial test
##
## data:  A success is counted if the rating is higher in the 4.5oz group
## number of successes = 9, number of trials = 14, p-value = 0.424
## alternative hypothesis: true probability of success is not equal to 0.5
## 95 percent confidence interval:
##  0.3513801 0.8724016
## sample estimates:
## probability of success
##              0.6428571
```

Because the ratings were not significantly higher in the 4.5oz option, we took the ratings from the 3oz option.

## Noodler has an average of 4.5 out of 5 stars

In total, there are 99 unique inks listed in the Goulet Pen website; and on average, people gave Noodler's ink 4.5 out of 5 stars.

<img src="{{ site.baseurl }}/img/figure/2016-05-22/plot-ratings-1.png" title="" alt="" width="672" />

The inks with 4.9+ stars are:

|Ink                                                               | Rating|Bulletproof |Eternal |Water_Resistant |
|:-----------------------------------------------------------------|------:|:-----------|:-------|:---------------|
|[St. Patty's Eire](http://www.gouletpens.com/search?query=N19175) |    5.0|No          |No      |No              |
|[Sunrise](http://www.gouletpens.com/search?query=N19176)          |    5.0|No          |No      |No              |
|[Violet](http://www.gouletpens.com/search?query=N19007)           |    5.0|No          |No      |No              |
|[Navajo Turquoise](http://www.gouletpens.com/search?query=N19029) |    4.9|No          |No      |No              |
|[Shah's Rose](http://www.gouletpens.com/search?query=N19036)      |    4.9|No          |No      |No              |
|[Turquoise](http://www.gouletpens.com/search?query=N19005)        |    4.9|No          |No      |No              |

Unfortunately, none of the top rated inks are bulletproof, eternal, and/or water resistant.

## The top shortlisted inks

Here, I merged the Goulet Pen ratings with the shortlist of 43 inks and filtered for inks rated above average.

| Rank|Ink                                                                    | Rating|Bulletproof |Eternal   |Water_Resistant |
|----:|:----------------------------------------------------------------------|------:|:-----------|:---------|:---------------|
|    1|[Black](http://www.gouletpens.com/search?query=N19001)                 |    4.8|Yes         |Yes       |Yes             |
|    1|[Blue Ghost](http://www.gouletpens.com/search?query=N19190)            |    4.8|Yes         |Yes       |Yes             |
|    1|[General of the Armies](http://www.gouletpens.com/search?query=N19073) |    4.8|Yes         |Yes       |Yes             |
|    4|[Air Corp Blue Black](http://www.gouletpens.com/search?query=N19040)   |    4.7|Partially   |Partially |Yes             |
|    4|[Bad Black Moccasin](http://www.gouletpens.com/search?query=N19061)    |    4.7|Yes         |Yes       |Yes             |
|    4|[Lexington Gray](http://www.gouletpens.com/search?query=N19042)        |    4.7|Yes         |Yes       |Yes             |
|    4|[X-Feather](http://www.gouletpens.com/search?query=N19046)             |    4.7|Yes         |Yes       |Yes             |
|    8|[54th Massachusetts](http://www.gouletpens.com/search?query=N19071)    |    4.6|Yes         |Yes       |Yes             |
|    8|[Bad Belted Kingfisher](http://www.gouletpens.com/search?query=N19062) |    4.6|Yes         |Yes       |Yes             |
|    8|[El Lawrence](http://www.gouletpens.com/search?query=N19599)           |    4.6|Yes         |Yes       |Yes             |
|    8|[Polar Black](http://www.gouletpens.com/search?query=N19201)           |    4.6|Yes         |Yes       |Yes             |

From this list, it looks like I should get "Black", "Blue Ghost", or "General of the Armies": Black is an unexceptional colour and is easily found in regular ball point pens; Blue Ghost is an invisible ink and I want something I can see; and General of the Armies is a maybe.

p.s.

I have already have "Air Corp Blue Black".
