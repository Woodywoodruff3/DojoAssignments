from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.books),
    url(r'^add$', views.add),
    url(r'^create', views.create),
    url(r'^(?P<book_id>\d+)$', views.show),
    url(r'^(?P<book_id>\d+)/create_extra$', views.create_extra),
    url(r'^remove/(?P<user_id>\d+)$', views.remove),
    url(r'^users/(?P<user_id>\d+)$', views.user)
]