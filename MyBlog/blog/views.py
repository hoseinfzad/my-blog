from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def index(request):
    posts = Post.objects.filter(status=True)
    context = {'posts': posts }
    return render(request, 'index.html', context)


def post_details(request, year, month, day, post):
    posts = get_object_or_404(Post, slug=post, status=True, published_date__year=year,
                              published_date__month=month, published_date__day=day)
    # categories = 
    return render(request, 'details.html',{'posts': posts})