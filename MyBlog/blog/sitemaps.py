from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.contrib import sitemaps
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, obj):
        return reverse("blog:post_detail", args=[obj.published_date.year,
                                                 obj.published_date.month,
                                                 obj.published_date.day,
                                                 obj.slug])
    
    

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['blog:index', 'blog:about', 'blog:contact']

    def location(self, item):
        return reverse(item)
