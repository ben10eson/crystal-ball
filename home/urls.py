from django.conf.urls import url
from home.views import HomeView
from . import views


urlpatterns=[
    url(r'$',HomeView.as_view(),name='home'),
    # url(r'$',views.home,name='home'),
    url(r'^result/$',views.result, name='result'),

    url(r'^profile/$',views.profile,name='profile'),


]