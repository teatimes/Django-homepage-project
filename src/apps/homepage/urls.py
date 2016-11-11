""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from . import views

app_name= 'homepage'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^page_one/$', views.PageOneView.as_view(), name='page_one'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^sendt/$', views.SendtView.as_view(), name='sendt'),
    url(r'^page_two/$', views.PageTwoView.as_view(), name='page_two'),
    url(r'^page_three/$', views.PageThreeView.as_view(), name='page_three'),
    url(r'^from_guests/$', views.FromGuestsView.as_view(), name='from_guests'),
    url(r'^page_four/$', views.PageFourView.as_view(), name='page_four')
]