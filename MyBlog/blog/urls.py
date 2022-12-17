from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
                                        views.post_details,
                                        name='post_detail'),
    path('cagetory/<str:cat_name>', views.index, name='category'),
    path('author/<str:author_username>', views.index, name='author'),
    path('search/', views.blog_search, name='search'),
]