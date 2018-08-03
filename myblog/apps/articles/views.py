# _*_ encoding:utf-8 _*_
from datetime import datetime
import logging

from django.shortcuts import render
from django.views import View
from django.db.models.query import QuerySet
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from articles.models import Article,Category,Tag
from operation.views import CommentHandler,ArticleComment
from operation.forms import CommentFrom
from users.models import UserProfile,TemporaryUser

class QueryError(Exception):
    pass

logging.basicConfig(level=logging.WARNING,
                    filename='/log/log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

#查询的类
class ArticleQuery():

    def __init__(self):
        self.articles = Article.objects.all()
        self.categorys=Category.objects.all()
        self.tags=Tag.objects.all()
        self.category_articles =self.category_counts()
        self.tags = self.tags


    #实现字段排序查询
    def _order_queryset(self,order_field):
        try:
            order_article=Article.objects.order_by(order_field)
            if order_article:
                return order_article
            else:
                msg_error='查询【{0}】字段,查询数据为空'.format(order_field)
                return msg_error
        except QueryError as e:
            msg_error='查询【{0}】字段,字段未找到'.format(order_field)
            return msg_error

    #查询状态处理
    def _order_query_status(self,order_field='-click_nums'):
        results = self._order_queryset(order_field)
        if isinstance(results, QuerySet):
            return results
        else:
            logging.WARNING(results)
            results = None
            return results

    #查询内容设置
    def _order_queryset_results(self,choice_num=None,space_num=None,start_place=0,order_field='-click_nums'):
        results= self._order_query_status(order_field)
        if results:
            num = results.count()
            if choice_num !=None and space_num !=None and choice_num<=space_num:
                if start_place !=0:
                    max_num = start_place + choice_num
                    if  max_num<=num :
                        results=results[start_place:]
                        article=self._partition_queryset(results,choice_num,space_num)
                        return article
                    else:
                        raise QueryError('超出了查询集的索引范围')
                else:
                    article=self._partition_queryset(results,choice_num,space_num)
                    return article
            elif choice_num ==None and space_num !=None:
                if start_place !=0:
                    max_num=start_place+space_num
                    if max_num<=num:
                        results=results[start_place:]
                        article = self._partition_queryset(results, choice_num, space_num)
                        return article
                    else:
                        raise QueryError('超出了查询集的索引范围')
                else:
                    if space_num<=num:
                        article = self._partition_queryset(results, choice_num, space_num)
                        return article
                    else:
                        raise QueryError('超出了查询集的索引范围')

            elif choice_num !=None and space_num==None:
                if start_place !=0:
                    max_num=start_place+choice_num
                    if max_num<=num:
                        article=results[start_place:max_num]
                        return article
                    else:
                        raise QueryError('超出了查询集的索引范围')
                else:
                    if choice_num<=num:
                        article=results[:choice_num]
                        return  article
                    else:
                        raise QueryError('超出了查询集的索引范围')


            else:
                if start_place<=num:
                    article=results[start_place:]
                    return  article
                else:
                    raise QueryError('超出了查询集的索引范围')
        else:
            article=None
            msg_waring='查询内容为空'
            logging.WARNING(msg_waring)


    #具体内容的获取
    def _partition_queryset(self,results,space_num,choice_num=None,):
        num=len(results)
        if choice_num != None:
            if num <= space_num and num >= choice_num:
                article = results[:choice_num]
                return article
            elif num > space_num:
                from random import sample
                article = sample(list(results[:space_num]), choice_num)
                return article
            else:
                article = results
                return article
        else:
            if num < space_num:
                raise QueryError('超出了查询集的索引范围')
            else:
                article = results[:space_num]
                return article


    #默认查询结果
    def default_content(self):

        return self.categorys,self.tags,self.articles
    #博客分类处理
    def category_counts(self):
        categorys_counts = {}
        self.category_num=self.categorys.count()
        for qset_num in range(0, self.category_num):
            count = 0
            num=self.categorys[qset_num].id
            category_name = self.categorys[qset_num].name
            for i in range(self.articles.count()):
                article_categ = self.articles[i].category_id
                if article_categ== category_name:
                    count += 1
                else:
                    continue
            categorys_counts[category_name] = count
        return categorys_counts


    # 每类博客的列表
    def _category_articles(self, category_name):
        category_obj = Article.objects.filter(category=category_name)
        return category_obj

    def _tag_article(self,tag_name):
        id_num = self.tags.values().get(name=tag_name)['id']
        tag_articles =Article.objects.filter(tags=id_num)
        return tag_articles

    def _article_tags(self,article_name):
        tag_obj=Article.objects.get(title=article_name).tags
        article_tags=tag_obj.values()
        return article_tags


#评论添加处理
class CommentAddHamdler():
    def __init__(self,request,article_name):
        self.msg_error=None
        self.comment_profile = CommentFrom(request.POST)
        if self.comment_profile.is_valid():
            self.article_title = article_name
            self.user_name = request.POST.get('name', '')
            self.comment = request.POST.get('comment', '')
            self.email = request.POST.get('email', '')
            if UserProfile.objects.filter(username=self.user_name):
                if UserProfile.objects.filter(email=self.email):
                    judge_user=0
                    self.user_comment_handler(judge_user)
            else:
                judge_user=1
                self.temporary_user_handler()
                self.user_comment_handler(judge_user)
        else:
            self.msg_error='提交的信息有误，请重新提交'

    def user_comment_handler(self,judge_user):
        commment_add = ArticleComment()
        commment_add.comment = self.comment
        commment_add.add_time = datetime.now()
        commment_add.article_id = self.article_title
        if judge_user==0:
            commment_add.user_id = self.user_name
            commment_add.temporary_user_id = '--'
            commment_add.judge_user='0'
        else:
            commment_add.user_id = '--'
            commment_add.temporary_user_id =self.user_name
            commment_add.judge_user='1'

        commment_add.save()

    def temporary_user_handler(self):
        user=TemporaryUser.objects.filter(username=self.user_name)
        if not user:
            commment_add = TemporaryUser()
            commment_add.username = self.user_name
            commment_add.email = self.email
            commment_add.add_time = datetime.now()
            commment_add.save()
        else:
            pass


class PaginatorHandler():
    def __init__(self,paginator_obj,page_num,orphans=0,allow_empty_first_page = True):
        self.paginator=Paginator(paginator_obj,page_num,orphans=orphans,allow_empty_first_page=allow_empty_first_page)
        self.num_pages=self.paginator.num_pages
    def page_handler(self,page=1):
        try:
            page = self.paginator.page(page)
        except PageNotAnInteger:
            page = self.paginator.page(1)
        except EmptyPage:
            page = self.paginator.page(1)
        return page



#主页视图处理
class HomeArricle(View):

    def get(self,request,):
        roll_articles=article_handler._order_queryset_results(choice_num=3)
        next_ariticles=article_handler._order_queryset_results(choice_num=2,start_place=3)
        click_articles=article_handler._order_queryset_results(choice_num=8)
        update_articles=article_handler._order_queryset_results(choice_num=10,order_field='create_time')
        context={'roll_articles':roll_articles,'next_ariticles':next_ariticles,'click_articles':click_articles,
                 'update_articles':update_articles,'category_articles':article_handler.category_articles,'tags':article_handler.tags}
        return render(request,'index.html',context)

#详情页面的处理
class DetailArticle(View):


    def get(self,request,article_name):
        articles, comment_detail, comment_count=self.article_handler(article_name)

        click_articles = article_handler._order_queryset_results(choice_num=8)
        article_tags=article_handler._article_tags(article_name)
        context={'tags':article_handler.tags,'category_articles':article_handler.category_articles,
                     'articles':articles,'comment_detail':comment_detail,'comment_count':comment_count,
                 'click_articles':click_articles,'article_tags':article_tags}

        return render(request,'info.html',context)

    def post(self,request,article_name):
            user_table_handler=CommentAddHamdler(request,article_name)
            articles, comment_detail, comment_count = self.article_handler(article_name)
            context={'tags': tags,'categorys': categorys,'featrue_articles': featurn_articles,
                         'articles':articles,'comment_detail':comment_detail,'comment_count':comment_count}

            if not user_table_handler.msg_error:
                return render(request, 'single.html', context)

            else:
                context['mag_error'] = user_table_handler.msg_error
                return render(request, 'single.html', context)

    def article_handler(self, article_name):
        article = Article.objects.get(title=article_name)
        article.click_nums +=1
        article.save()
        try:
            up_article=Article.objects.filter(create_time__lt=article.create_time)[:1]
        except:
            up_article=None
        try:
            down_article=Article.objects.filter(create_time__gt=article.create_time)[:1]
        except:
            down_article=None
        articles={'article':article,'up_article':up_article,'down_article':down_article}
        comment_obj = CommentHandler(article_name)
        comment_detail = comment_obj.comment_handler()
        comment_count = comment_obj.count
        return articles, comment_detail, comment_count





#分类模块的处理
class CategoryView(View):
    def get(self,request,category_name,index):
        self.category_list=article_handler._category_articles(category_name)
        if hasattr(self,'paginator_handler'):
            pass
        else:
            self.paginator_obj()
        judge = judge_paginator(self.paginator_handler.num_pages)
        page_obj=self.paginator_handler.page_handler(index)
        click_articles = article_handler._order_queryset_results(choice_num=8)
        context={'category_list':page_obj,'category_articles':article_handler.category_articles,
                 'tags':article_handler.tags,'click_articles':click_articles,'page_nums':self.paginator_handler.num_pages,
                 'category_name':category_name,'judge':judge}
        return render(request,'list.html',context)

    def paginator_obj(self,page_num=5):
        self.paginator_handler = PaginatorHandler(self.category_list,page_num)
        return self.paginator_handler

#分类标签处理
class TagView(View):
    def get(self,request,tag_name,index):
        click_articles = article_handler._order_queryset_results(choice_num=8)
        self.tag_list=article_handler._tag_article(tag_name)
        if hasattr(self,'paginator_handler'):
            pass
        else:
            self.paginator_obj()
        judge=judge_paginator(self.paginator_handler.num_pages)
        page_obj=self.paginator_handler.page_handler(index)
        context = {'tag_list': page_obj, 'category_articles': article_handler.category_articles,
                   'tags': article_handler.tags, 'click_articles': click_articles,'':tag_name,
                   'page_nums': self.paginator_handler.num_pages,'judge':judge}

        return render(request,'list.html',context)

    def paginator_obj(self,page_num=5):
        self.paginator_handler = PaginatorHandler(self.tag_list,page_num)
        return self.paginator_handler


class ArticleTheme(View):
    def get(self,request,article_theme,index):
        self.theme_articles = Article.objects.filter(mean=article_theme)
        if hasattr(self,'paginator_handler'):
            pass
        else:
            self.paginator_obj()
        judge = judge_paginator(self.paginator_handler.num_pages)
        page_obj=self.paginator_handler.page_handler(index)
        click_articles = article_handler._order_queryset_results(choice_num=8)
        context = { 'click_articles': click_articles,'tags': article_handler.tags,
                   'page_obj': page_obj, 'category_articles': article_handler.category_articles,
                   'page_nums':self.paginator_handler.num_pages,'article_theme':article_theme,'judge':judge}
        return render(request,'list1.html',context)

    def paginator_obj(self,page_num=10):
        self.paginator_handler = PaginatorHandler(self.theme_articles,page_num)
        return self.paginator_handler


class TimeLine(View):
    def get(self,request,index):
        self.articles=article_handler.articles
        if hasattr(self,'paginator_handler'):
            pass
        else:
            self.paginator_obj()
        judge = judge_paginator(self.paginator_handler.num_pages)
        page_obj=self.paginator_handler.page_handler(index)
        return render(request,'time.html',{'articles':page_obj,
                                           'page_nums': self.paginator_handler.num_pages,'judge':judge})

    def paginator_obj(self,page_num=20):
        self.paginator_handler = PaginatorHandler(self.articles,page_num)
        return self.paginator_handler

class AboutMe(View):
    def get(self,request):
        return render(request,'about.html')


def judge_paginator(page_nums):
    if page_nums>1:
        judge=True
        return judge
    else:
        judge=False
        return judge

article_handler=ArticleQuery()