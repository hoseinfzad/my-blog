from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ContactForm, CommentForm
from django.contrib import messages

def index(request, **kwargs):
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
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
    
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '.نظر شما با موفقیت ارسال شد و پس از تایید ثبت خواهد شد')
        else:
            messages.error(request, 'درخواست نامعتبر')
            messages.error(request, form.errors)
            
    
    posts = get_object_or_404(Post, slug=post, status=True, published_date__year=year,
                                published_date__month=month, published_date__day=day)
        
    comments = posts.comments.filter(approved=True)
    form = CommentForm()
    context = {'posts': posts, 'comments': comments, 'form': form}
    return render(request, 'details.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context ={'posts': posts}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '.پیام شما با موفقیت ارسال شد')
        else:
            messages.error(request, 'درخواست نامعتبر')
            messages.error(request, form.errors)
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')