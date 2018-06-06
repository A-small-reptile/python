from haystack import indexes
from app_01.models import Posts
import datetime

class PostsIndex(indexes.SearchIndex,indexes.Indexable):
    text=indexes.NgramField(document=True,use_template=False)
    user=indexes.CharField(model_attr='author')
    create_time=indexes.DateTimeField(model_attr='create_time')
    def get_model(self):#获取模块
        return Posts

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(create_time=datetime.datetime.now())