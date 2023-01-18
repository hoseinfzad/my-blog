from django.contrib import admin
from .models import Post, Category, Contact, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('title', 'author','counted_view', 'status', 'created_date')
    empty_value_display = '-empty-'
    list_filter = ['status', 'author']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'subject',)
    empty_value_display = '-empty-'
    list_filter = ['subject']
    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('subject', 'name','approved', 'created_date')
    empty_value_display = '-empty-'
    list_filter = ['approved', 'email']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    
    
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)

