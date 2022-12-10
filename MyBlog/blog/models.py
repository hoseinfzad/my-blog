from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    # tags = TaggableManager() 
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_date']
    
    def __str__(self) -> str:
        return f"{self.title} - {self.id}"
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.published_date.year,
                                                 self.published_date.month,
                                                 self.published_date.day,
                                                 self.slug])
        
        
        
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default=None)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    email = models.EmailField(default=None)
    
    def __str__(self):
        return self.email