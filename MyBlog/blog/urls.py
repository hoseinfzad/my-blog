from django.urls import path
from . import views



app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
                                        views.post_details,
                                        name='post_detail'),
    path('cagetory/<str:cat_name>', views.index, name='category'),
    path('tags/<str:tag_name>', views.index, name='tag'),
    path('author/<str:author_username>', views.index, name='author'),
    path('search/', views.blog_search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
]