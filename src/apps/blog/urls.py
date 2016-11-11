from django.conf.urls import url
from . import views
from src.apps.blog.views import BlogPostDetailView, BlogPostListView

app_name = 'blog'

urlpatterns = [
	url(r'^blog/$', views.BlogPostListView.as_view(), name="blogpost-list"),
	url(r'^blogpost_list/$', views.BlogPostListView.as_view(), name="blogpost-list"),
	url(r'^(?P<slug>[-\w]+)/$', views.BlogPostDetailView.as_view(), name='blogpost_detail'),
	url(r'^search/(?P<keyword>[-\w]+)/$', views.SearchView.as_view(), name='search')
]