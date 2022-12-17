from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request, **kwargs):
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
        
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts }
    return render(request, 'index.html', context)


def post_details(request, year, month, day, post):
    posts = get_object_or_404(Post, slug=post, status=True, published_date__year=year,
                              published_date__month=month, published_date__day=day)
    
    return render(request, 'details.html',{'posts': posts})

def blog_search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context ={'posts': posts}
    return render(request, 'index.html', context)


