---
layout: page
title: Tags
permalink: /tags/
description: Find posts tagged with ...
---
<ul>
  {% assign sorted_tags = (site.tags | sort:0) %}
  {% for tag in sorted_tags %}
  <li class="list-unstyled">
    <span style='color: #aaa; font-family: Monaco, "Courier New", monospace; font-size: 60%;'>
      Tag »
    </span>
    <a href="{{ site.baseurl }}/tags/{{ tag | first }}/index.html">
      <u>{{ tag | first }}</u>
    </a>
  </li>
  {% endfor %}
</ul>
