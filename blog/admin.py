from django.contrib import admin

from .models import Author, Tag, Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title", "excerpt", "image", "author", "data", "slug", "content")


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
