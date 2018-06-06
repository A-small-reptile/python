from django.shortcuts import render,redirect
from django.views.generic import View
from django.conf import settings
from django.contrib.auth import mixins,models
from django.shortcuts import render
from app_01.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from haystack.views  import SearchView



#限制对登录用户访问
"""@login_required(redirect_file_name,login_url)"""
class Request_Auth():
    def request_auth(self,request):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('%s?next=%s'%(settings.LOGIN_URL,request.path))
class Request_Auth2(mixins.LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to '

class BaseQueryset():
    def __init__(self):
        self.categorys = Category.objects.all()
        self.category_num =self.categorys.count()
        self.tags = Tags.objects.all()
        self.blogs = Posts.objects.all()
#博客类别处理
class CategoryBlogHandler(BaseQueryset):
    # 分类博客的数量
    def category_counts(self):
        categorys_counts = {}
        for qset_num in range(0, self.category_num):
            count = 0
            num = self.categorys[qset_num].id
            category_name = self.categorys[qset_num].name
            for i in range(BlogsHandler().blogs.count()):
                blog_categ_id = BlogsHandler().blogs[i].category_id
                if blog_categ_id == num:
                    count += 1
                else:
                    continue
            categorys_counts[category_name] = count
        return categorys_counts #每个类别对应的博客数量的字典
    # 每类博客的列表
    def category_blogs(self,category):
        catepory_id=Category.objects.get(name=category)
        category_obj=Posts.objects.filter(category_id=catepory_id)
        return category_obj #每类具体的查询对象

#博客标签处理
class TagsHandler(BaseQueryset):
    def tag_detail(self,tag_name):
        id_num=self.tags.values().get(name=tag_name)['id']
        tag_posts=Posts.objects.filter(tags=id_num)
        return tag_posts

#博客处理
class BlogsHandler(BaseQueryset):
   #随机博客的获取
    def range_blogs(self):
        from random import sample
        random_blogs = sample(list(self.blogs), 4)
        return random_blogs
    #分页处理
    def blog_paginator(self,request,page):
        paginator = Paginator(self.blogs, 7, 2)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(1)
        return contacts
    #博客内容处理
    def blog_detail(self,blog_title):
        blog_handler=Posts.objects.get(title=blog_title)
        return blog_handler

class SearchHandler(SearchView,View):

    def extra_context(self,):
        context=super(SearchHandler, self).extra_context()
        context['random_blogs']=Viewhandler().range_blogs()
        context['categorys_counts']=Viewhandler().category_counts()
        context['tags']=Viewhandler().tags
        print(self.results.count())
        return context

class Viewhandler(BlogsHandler,CategoryBlogHandler,TagsHandler,SearchHandler):
    pass

#主页视图处理函数
def get_page(request,page=1):
    assistant=Viewhandler()
    contacts=assistant.blog_paginator(request,page)
    return render(request,'base/home.html',{ 'contacts':contacts,
                                            'random_blogs': assistant.range_blogs(),
                                            'categorys_counts':assistant.category_counts(),
                                            'tags':assistant.tags})

#博客分类详情页面
def cgy_view(request,category_name):
    cgy_robot=Viewhandler()
    category_obj=cgy_robot.category_blogs(category_name)
    return render(request,'blog/category.html',{'category_name':category_name,
                                                'category_obj':category_obj,
                                                'random_blogs': cgy_robot.range_blogs(),
                                                'categorys_counts': cgy_robot.category_counts(),
                                                'tags': cgy_robot.tags
                                                })
#博客标签页面
def tag_view(request,tag_name):
    tag_robot=Viewhandler()
    tag_blogs=tag_robot.tag_detail(tag_name)
    return render(request,'blog/tag_blogs.html',{
                                                'tag_blogs':tag_blogs,
                                                'tag_name':tag_name,
                                                'random_blogs': tag_robot.range_blogs(),
                                                'categorys_counts': tag_robot.category_counts(),
                                                'tags': tag_robot.tags
                                                })
#博客内容详情页面
def blog_view(request,blog_title):
    robot_handler=Viewhandler()
    content_obj=robot_handler.blog_detail(blog_title)
    return render(request,'blog/blog_content.html',{'blog_title':blog_title,
                                                    'content_obj':content_obj,
                                                    'random_blogs': robot_handler.range_blogs(),
                                                    'categorys_counts': robot_handler.category_counts(),
                                                    'tags': robot_handler.tags,
                                                    })




def blogs(request):
    pass


