---
layout: page
permalink: /archives/
title: "Archives"
description: "Previous posts"
---
<ul>
  {% for post in site.posts %}

<!--     {% if post.tags.size > 0 %}
      {% capture tags_content %}
      Tagged with: {% endcapture %}

      {% for post_tag in post.tags %}
        {% assign tag = site.data.tags[post_tag] %}
        {% if tag %}
          {% capture tags_content_temp %}{{ tags_content }}<a href="/tag/{{ tag.slug }}/">{{ tag.name }}</a>{% if forloop.last == false %}, {% endif %}{% endcapture %}
          {% assign tags_content = tags_content_temp %}
        {% endif %}
      {% endfor %}
    {% else %}
      {% assign tags_content = '' %}
    {% endif %} -->

    <li class="list-unstyled">
      <div style="line-height:60%">

        <span style='color: #aaa; font-family: Monaco, "Courier New", monospace; font-size: 60%;'>
          {{ post.date | date: "%d %b %Y" }} »
        </span>
        <a href="{{ post.url }}/">{{ post.title }}</a>

        <br>
        <span style='color: #aaa; font-family: Monaco, "Courier New", monospace; font-size: 60%;'>
        Tagged with {% if post.tags.size == 1 %}<i class="fa fa-tag"></i>{% else %}<i class="fa fa-tags"></i>{% endif %}
        {% for tag in post.tags %}
          <a href="/tag/{{ tag }}" title="View posts tagged with &quot;{{ tag }}&quot;">
            <font color="#aaa"><u>{{ tag }}</u></font>
          </a>
        {% endfor %}
        </span>

      </div>
    </li>
    <br>
  {% endfor %}
</ul>
