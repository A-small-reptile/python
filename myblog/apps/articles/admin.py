# _*_ encoding:utf-8 _*_
from django.contrib import admin

from articles.models import Article,Category,Tag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display= ['title','author','category','create_time']
    search_fields = ['title','content','category__name','author__nick_name']
    list_filter = ['category','tags']
    ordering = ['-create_time']
    list_editable = ['category']
    list_per_page = 50
    filter_horizontal = ['tags']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','categroy_num',]
    search_fields = ['name']
    ordering = ['-categroy_num']
    list_per_page = 20

@admin.register(Tag,)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20