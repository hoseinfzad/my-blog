from django import template
from blog.models import Post, Category

register = template.Library()

@register.filter
def snippet(value, arg=20):
    return value[:arg]

@register.inclusion_tag("recent_posts.html")
def recent_posts():
    posts = Post.objects.filter(status=True).order_by("published_date")[:3]
    return {'posts': posts}

@register.inclusion_tag("latest_posts.html")
def latest_posts():
    posts = Post.objects.filter(status=True).order_by("published_date")[:6]
    return {'posts': posts}

@register.inclusion_tag("categories.html")
def post_categories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}        