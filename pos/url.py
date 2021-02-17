# _*_coding:utf-8_*_
# 作者    :Rvica
# 日期    :2021/2/16
# 文件    :url.py
# IDE     :PyCharm
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.queryAll),
    url(r'^page/(\d+)$', views.queryAll),
    url(r'^post/(\d+)$', views.detail),
]