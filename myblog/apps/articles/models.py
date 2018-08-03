#_*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from tinymce.models import HTMLField

from users.models import UserProfile

class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name=u'分类名称',unique=True)
    categroy_num=models.IntegerField(default=0,verbose_name=u'分类数量')
    class Meta:
        verbose_name=u"文章分类"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100,verbose_name=u'标签名称')

    class Meta:
        verbose_name=u"文章标签"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=100,verbose_name=u'文章标题',unique=True)
    content=HTMLField(verbose_name=u'文章内容')
    create_time=models.DateTimeField(default=datetime.now,verbose_name=u'创建时间')
    click_nums=models.IntegerField(default=0,verbose_name=u'查看数量')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=u'文章分类',to_field='name',)
    tags = models.ManyToManyField(Tag, blank=True,verbose_name=u'文章标签')
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name=u'文章作者')
    image=models.ImageField(upload_to='static/image/%Y/%m',max_length=100,verbose_name='文章图片',default='/static/images/p1.ipg')
    mean=models.CharField(max_length=10,choices=(('生活百态','生活'),('零一世界','编程')),verbose_name=u'文章类别',default='零一的世界')

    class Meta:
        verbose_name=u'文章内容'
        verbose_name_plural=verbose_name
        ordering=['-create_time']

    def __str__(self):
        return self.title


