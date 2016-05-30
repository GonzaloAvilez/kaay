from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me$', views.post_list),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
        name='show'),
    url(r'^me/add$', views.post_new, name='post_new'),
    
]
