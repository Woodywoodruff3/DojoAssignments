from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^users$', views.index), #Render Template index.html
    url(r'^users/new', views.new_user), #Render Template add_user.html
    url(r'^users/show/(?P<user_id>\d+)$', views.show), #Render Template show.html
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit), #Render Template edit.html
    url(r'^add_user', views.add_user), #Form path adding user
    url(r'^update_user/(?P<user_id>\d+)', views.update_user), #Form path for updating
    url(r'^users/delete/(?P<user_id>\d+)', views.destroy) #Deletes User
]