"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from pro import views
import home
from accounts import views as accounts_views
urlpatterns = [
    url(r'^$', views.Home_page, name='Home_page'),
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('accounts.urls',namespace='accounts')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^info/',include('info.urls',namespace='info')),


]
