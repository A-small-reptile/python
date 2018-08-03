# _*_ encoding:utf-8 _*_
from django.contrib import admin

from operation.models import (ArticleComment,UserFavorite,VisitHistroy,UserMasseger)

@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):

    list_display = ['article','user','temporary_user','comment','judge_user','add_time',]
    search_fields = ['article__title','comment']
    list_filter = ['user','temporary_user']
    list_per_page = 50



@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):

    list_display = ['user','article','add_time']
    search_fields = ['user__nick_name', 'article__title']
    ordering = ['-add_time']
    list_per_page = 50

@admin.register(VisitHistroy)
class VisitHistoryAdmin(admin.ModelAdmin):

    list_display = ['user','article','visit_time']
    search_fields = ['user__nick_name', 'article__title']
    ordering = ['-visit_time']
    list_per_page = 50

@admin.register(UserMasseger)
class UserMassegerAdmin(admin.ModelAdmin):

    list_display = ['user','masseger','has_read','send_time']
    list_per_page = 50
    search_fields = ['masseger']
    list_filter = ['has_read']
    list_editable = ['has_read']

    actions = ['make_published']
    def make_published(self,request,queryset):
        queryset.update(has_read=True)
    make_published.short_description = '设置用户消息已读'






