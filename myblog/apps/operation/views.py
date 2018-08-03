# _*_ encoding:utf-8 _*_

from operation.models import ArticleComment
from users.models import UserProfile


class CommentHandler():
    def __init__(self,article_title=None):
        if article_title !=None:
            try:
                comment_details=ArticleComment.objects.filter(article=article_title)
                count=comment_details.count()
            except:
                comment_details=None
                count=0
        else:
            comment_details = None
            count=0
        self.comment=comment_details
        self.count=count

    def comment_handler(self):
        if self.comment !=None:
            comment_dict={}
            comment_list=[]
            for comment_detail in self.comment:
                comment_dict['comment'] = comment_detail.comment
                comment_dict['add_time'] = comment_detail.add_time
                if comment_detail.judge_user=='0':
                    user=comment_detail.user
                    user_detail=UserProfile.objects.get(username=user)
                    comment_dict['user']=user
                    comment_dict['image']=user_detail.image
                else:
                    user=comment_detail.temporary_user
                    comment_dict['user'] = user
                    comment_dict['image'] ='/static/image/gx.png'
                comment_list.append(comment_dict)
                comment_dict = {}

            return comment_list
        else:
            comment_list=None
            return comment_list









