# Generated by Django 2.0.1 on 2018-07-14 13:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300, verbose_name='评论')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('judge_user', models.CharField(choices=[('0', '注册用户'), ('1', '临时用户')], default='1', max_length=10, verbose_name='用户类别')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', to_field='title', verbose_name='文章')),
                ('temporary_user', models.ForeignKey(blank=True, default='-', on_delete=django.db.models.deletion.CASCADE, to='users.TemporaryUser', to_field='username', verbose_name='临时用户')),
                ('user', models.ForeignKey(blank=True, default='-', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏时间')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', to_field='title', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '文章收藏',
                'verbose_name_plural': '文章收藏',
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='UserMasseger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='接收用户')),
                ('masseger', models.CharField(max_length=500, verbose_name='消息内容')),
                ('has_read', models.BooleanField(default=False, verbose_name='消息是否读过')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
                'ordering': ['-send_time'],
            },
        ),
        migrations.CreateModel(
            name='VisitHistroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='查看时间')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', to_field='title', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '历史记录',
                'verbose_name_plural': '历史记录',
                'ordering': ['-visit_time'],
            },
        ),
    ]