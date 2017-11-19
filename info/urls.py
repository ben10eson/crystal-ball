from django.conf.urls import url
from home.views import HomeView
from . import views
from info.views import infoview


urlpatterns=[
    # url(r'$',views.home,name='home'),
url(r'$',infoview.as_view(),name='home'),
    # url(r'^homepage/$', views.home_page, name='homepage'),

]