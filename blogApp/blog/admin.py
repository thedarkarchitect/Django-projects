from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.

#this is going to show the comments ryt below the each post for easy viewing and debuging reasons
class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


#add search to the admin page for post and category and comments
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category' ,'created_at', 'status']#this shows this information to help sort
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug' : ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug' : ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

admin.site.register(Post, PostAdmin,)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)