from django.contrib import admin
from app_01.models import *

#创建一个基本的类
class BaseApp(admin.ModelAdmin):
    pass
class CategoryAdmin(BaseApp):
    list_display = ['name']
class TagsAdmin(BaseApp):
    list_display = ['name']
class PostsAdmin(BaseApp):
    list_display = ['title','category', 'author']

#管理员内容关联
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Posts,PostsAdmin)



