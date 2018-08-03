#_*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models

from users.models import UserProfile,TemporaryUser
from articles.models import Article


class ArticleComment(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name=u'用户',on_delete=models.CASCADE,to_field='username',default='-',blank=True)
    temporary_user = models.ForeignKey(TemporaryUser, verbose_name=u'临时用户', on_delete=models.CASCADE,to_field='username',default='-',blank=True)
    article=models.ForeignKey(Article,verbose_name=u'文章',on_delete=models.CASCADE,to_field='title')
    comment=models.CharField(max_length=300,verbose_name=u'评论')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'评论时间')
    judge_user=models.CharField(choices=(('0','注册用户'),('1','临时用户')),verbose_name='用户类别',default='1',max_length=10)


    class Meta:

        verbose_name=u'用户评论'
        verbose_name_plural = verbose_name
        ordering=['-add_time']

    def __unicode__(self):
        return self.user,self.comment,self.article,self.temporary_user

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name=u'文章', on_delete=models.CASCADE,to_field='title')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'收藏时间')

    class Meta:
        verbose_name=u'文章收藏'
        verbose_name_plural=verbose_name
        ordering=['-add_time']

    def __unicode__(self):
        return self.user,self.article

class VisitHistroy(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name=u'文章', on_delete=models.CASCADE,to_field='title')
    visit_time=models.DateTimeField(default=datetime.now, verbose_name=u'查看时间')

    class Meta:
        verbose_name=u'历史记录'
        verbose_name_plural=verbose_name
        ordering=['-visit_time']

    def __unicode__(self):
        return self.article,self.article

class UserMasseger(models.Model):
    user=models.IntegerField(default=0,verbose_name='接收用户')
    masseger=models.CharField(max_length=500,verbose_name='消息内容')
    has_read=models.BooleanField(default=False,verbose_name='消息是否读过')
    send_time=models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name=u'用户消息'
        verbose_name_plural=verbose_name
        ordering=['-send_time']