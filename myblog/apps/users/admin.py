# _*_ encoding:utf-8 _*_
from django.contrib import admin

from users.models import UserProfile,EmailVerifyRecord,TemporaryUser

"""
class MyAdminSite(admin.AdminSite):
    site_header = u'水木年华的后台管理系统'
    site_title = u'水木年华'
"""
class UserAdmin(admin.ModelAdmin):
    list_display = ['nick_name','is_superuser','email','is_staff','is_active','date_joined','last_login']
    search_fields = ['nick_name','email']
    list_filter = ['is_staff','is_active']
    list_per_page = 50
    list_editable = ['is_superuser','is_staff','is_active']


class EmailVrifyRecordAdmin(admin.ModelAdmin):
    list_display = ['email','send_type','code','send_time']
    search_fields = ['email']
    ordering = ['-send_time']
    list_filter = ['send_type']
    list_per_page = 50
    list_editable = ['send_type']
    actions = ['make_published']
    def make_published(self,request,queryset):
        queryset.update(send_type='register')
    make_published.short_description = u'更改邮箱验证类型'

class TemporaryUserAdmin(admin.ModelAdmin):
    list_display = ['username','email','add_time']
    search_fields = ['username','email']
    ordering = ['-add_time']
    list_per_page = 50



"""admin_site=MyAdminSite(name='admin')"""
admin.site.site_header=u'平凡,致简的后台管理系统'
admin.site.site_title=u'平凡,致简'
admin.site.index_title='管理列表'
admin.site.register(UserProfile,UserAdmin)
admin.site.register(EmailVerifyRecord,EmailVrifyRecordAdmin)
admin.site.register(TemporaryUser,TemporaryUserAdmin)


