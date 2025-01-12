from django.contrib import admin
from .models import Categories, News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'publish_time', 'created_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'    
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']
    
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']