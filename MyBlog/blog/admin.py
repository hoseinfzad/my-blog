from django.contrib import admin
from .models import Post, Category, Contact, Newsletter
 
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('title', 'author','counted_view', 'status', 'created_date')
    empty_value_display = '-empty-'
    list_filter = ['status', 'author']
    prepopulated_fields = {'slug': ('title',)}
    
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'subject',)
    empty_value_display = '-empty-'
    list_filter = ['subject']
    
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
