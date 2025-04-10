from django.contrib import admin
from .models import HelpCategory, HelpArticle

@admin.register(HelpCategory)
class HelpCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(HelpArticle)
class HelpArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'date', 'lastmod')
    list_filter = ('is_published', 'tags')  # ⬅️ removed 'category'
    search_fields = ('title', 'summary', 'body', 'tags', 'note', 'tips')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-date',)