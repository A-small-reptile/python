"""
Django settings for MyBlog project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+(oeo*^l41=4*+%zydu9#p4)e!cxlbd@si+g)4pu%tuof13hs^'

# SECURITY WARNING: don't run with debug turned on in production!

#开发者模式与工厂模式
DEBUG = True

#允许的连入主机地址
ALLOWED_HOSTS = []




#app注册
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'MyBlog',
    'app_01',

]
#中间件的
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
# 'django.middleware.csrf.CsrfViewMiddleware',
#urls路径
ROOT_URLCONF = 'MyBlog.urls'

#模板路径和方法设置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
        'APP_DIRS': [
                     os.path.join(BASE_DIR,'templates/base'),
                     os.path.join(BASE_DIR,'templates/blog'),
                     os.path.join(BASE_DIR,'templates/search'),
                     ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyBlog.wsgi.application'


#数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SiteBlog',
        'USER':'root',
        'PASSWORD':'love512105'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


###时区和语言设置

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#静态文件和相关方法设置
STATIC_URL = "/static/"
STATIC_ROOT=os.path.join(BASE_DIR, 'static')
STATICFILES_DIR=[('css',os.path.join(STATIC_ROOT,'css/')),
                ('img',os.path.join(STATIC_ROOT,'images/')),
                ('js',os.path.join(STATIC_ROOT,'js/')),
                 ]
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",   #在项目下查找静态文件
    "django.contrib.staticfiles.finders.AppDirectoriesFinder", #在每个应用下查找文件
)

#全文搜索引擎配置
HAYSTACK_CONNECTIONS={
    'default':{
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        'PATH':os.path.join(BASE_DIR, 'templates/search/indexes/../whoosh_index'),
    }
}
#自动更新索引
HAYSTACK_SIGNAL_PROCESSOR ='haystack.signals.RealtimeSignalProcessor'
#索引每页的显示
HAYSTACK_SEARCH_RESULTS_PER_PAGE  = 8


