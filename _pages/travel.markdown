---
layout: single
# author_profile: true
title: Travel
permalink: /travel/
---

{% assign locale = include.locale | default: site.locale %}
{% assign posts = site.categories.Travel | where_exp: "post", "post.hidden != true" %}

<div class="gallery">
    {% for post in posts %}
        {% include archive-single.html locale=locale type="grid" %}
    {% endfor %}
</div>
