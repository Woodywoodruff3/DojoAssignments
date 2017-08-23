from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^courses/destroy/(?P<user_id>\d+)$',views.destroy),
    url(r'^destroy/(?P<user_id>\d+)$', views.remove)
]