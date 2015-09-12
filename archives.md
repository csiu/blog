---
layout: page
permalink: /archives/
title: "Archives"
description: "Previous posts"
---
<ul>
	{% for post in site.posts %}
		<li class="list-unstyled">
			<span style='color: #aaa; font-family: Monaco, "Courier New", monospace; font-size: 60%;'>
				{{ post.date | date: "%d %b %Y" }} » 
			</span> 
			<a href="{{ post.url }}">{{ post.title }}</a>
		</li>
	{% endfor %}
</ul>