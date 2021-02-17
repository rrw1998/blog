# _*_coding:utf-8_*_
# 作者    :Rvica
# 日期    :2021/2/17
# 文件    :search_indexes.py
# IDE     :PyCharm

from  haystack import indexes
from pos.models import *

#注意格式(模型类名+Index)
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #给title,content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')