# _*_ encoding:utf-8 _*_
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path



from users.views import LoginView,RegisterView,ActiveView,ForgetPasswdView,ResetView,ModifyPwdView
from articles.views import HomeArricle,DetailArticle,CategoryView,TagView,TimeLine,AboutMe,ArticleTheme


urlpatterns = [
    path(r'',HomeArricle.as_view(),name='home_page'),
    path(r'login/',LoginView.as_view(),name='login_page'),
    path(r'register/',RegisterView.as_view(),name='register_page'),
    path(r'admin/', admin.site.urls),
    path(r'captcha/',include('captcha.urls')),
    re_path(r'active/(?P<active_code>.*)',ActiveView.as_view(),name='user_active'),
    path(r'forget/',ForgetPasswdView.as_view(),name='forget_passwd'),
    re_path(r'reset/(?P<active_code>.*)',ResetView.as_view(),name='reset_passwd'),
    path(r'modifypwd/',ModifyPwdView.as_view(),name='modify_pwd'),
    path(r'detail/<str:article_name>',DetailArticle.as_view(),name='article_detail'),
    path(r'category/<str:category_name>/<int:index>',CategoryView.as_view(),name='article_category'),
    path(r'tag/<str:tag_name>/<int:index>',TagView.as_view(),name='article_tag'),
    path(r'theme/<str:article_theme>/<int:index>  ',ArticleTheme.as_view(),name='theme_article'),
    path(r'line/<int:index>',TimeLine.as_view(),name='time_line'),
    path(r'about/',AboutMe.as_view(),name='about_me')
]
