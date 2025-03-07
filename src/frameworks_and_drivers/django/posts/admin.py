from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'generated_by_gpt', 'created_at')
    list_filter = ('status', 'generated_by_gpt')
    search_fields = ('title', 'content')
