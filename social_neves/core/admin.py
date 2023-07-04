from django.contrib import admin
from .models import Profile, Post, LikePost, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    date_hierarchy = 'created'