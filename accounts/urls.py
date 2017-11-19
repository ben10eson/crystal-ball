from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views
urlpatterns=[
    url(r'^login/$',login,{'template_name':'accounts/login.html'},name='login'),

    url(r'^logout/$', logout, {'template_name': 'info/home_page.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    # url(r'$',views.welcome , name='welcome'),
    url(r'^data/$', views.data, name='data'),
    # url(r'^welcome/$', views.welcome, name='data'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^homepage/$',views.home_page,name='homepage'),
]