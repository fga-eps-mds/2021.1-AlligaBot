---
layout: page_capivaras
title: Equipe Capivaras
permalink: /Capivaras/
share: false
---
{% for post in site.posts %}
<div class="article-wrapper">
    <article>
        <section class="post-content">
            {% if post.tag == "capivaras" %}
            {% assign size = post.content | split: site.excerpt_separator | size %}
            
            {{ post.excerpt }}
           
            {% else %}
            
            {% endif %}
        </section>
    </article>
</div>

{% if forloop.last != true %}

{% endif %}
{% endfor %}