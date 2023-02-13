---
layout: single
# author_profile: true
classes: wide
title: Travel
permalink: /travel/
---

{% for post in site.categories.Travel %}
 <li><span>{{ post.date | date: site.date_format }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a> <br>
 {{ post.excerpt }}</li>
{% endfor %}