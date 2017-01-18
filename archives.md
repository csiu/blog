---
layout: page
permalink: /archives/
title: "Archives"
description: "Previous posts"
---
<style>
a.taglink {
  color: #aaa;
  text-decoration: underline;
}
</style>

<ul>
  {% for post in site.posts %}

    {% if post.tags.size > 0 %}
      {% capture tags_content %}
      Tagged with {% if post.tags.size == 1 %}<i class="fa fa-tag"></i>{% else %}<i class="fa fa-tags"></i>{% endif %} {% endcapture %}

      {% for post_tag in post.tags %}
        {% assign tag = site.data.tags[post_tag] %}
        {% if tag %}
          {% capture tags_content_temp %}{{ tags_content_tags }}<a class="taglink" href="{{ site.baseurl }}/tag/{{ tag.slug }}">{{ tag.name }}</a>{% if forloop.last == false %}, {% endif %}{% endcapture %}
          {% assign tags_content_tags = tags_content_temp %}
        {% endif %}
      {% endfor %}

      <!-- for when post list tags not in _data/tags.yml -->
      {% if tags_content_tags != %}
        {% capture tags_content %}{{ tags_content }}{{ tags_content_tags }}{% endcapture %}
        {% assign tags_content_tags = "" %}
      {% else %}
        {% assign tags_content = '' %}
      {% endif %}

    <!-- for when post have no tags -->
    {% else %}
      {% assign tags_content = '' %}
    {% endif %}

    <li class="list-unstyled">
      <div style="line-height:60%">

        <span style='color: #aaa; font-family: Monaco, "Courier New", monospace; font-size: 60%;'>
          {{ post.date | date: "%d %b %Y" }} »
        </span>
        <a href="{{ site.baseurl }}/{{ post.url }}">{{ post.title }}</a>

        {% if post.tags.size > 0 %}
        <br>
        <span style='color: #aaa; font-family: Monaco, "Courier New", monospace; font-size: 60%;'>
        <span class="tagcontent">{{ tags_content }}</span>
        {% endif %}
        </span>

      </div>
    </li>
    <br>
  {% endfor %}
</ul>
