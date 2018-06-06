from django.db import models
from django.contrib.auth.models import User

#博客分类
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

#博客标签
class Tags(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

#博客详情
class Posts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    create_time=models.DateTimeField()
    excerpt=models.TextField(max_length=100,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    class Metaclass:
        ordering=['create_time']
    def __unicode__(self):
        return self.title,self.content,self.create_time,self.category

 