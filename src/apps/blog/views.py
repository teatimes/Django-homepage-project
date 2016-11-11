from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from src.apps.blog.models import BlogPost, KeyWord

class BlogHomeView(TemplateView):
	template_name = "blog/blogpost_list.html"

class BlogPostListView(ListView):
	
	model = BlogPost
	template_name = "blog/blogpost_list.html"
	
	def get_context_data(self, **kwargs):
		context = super(BlogPostListView, self).get_context_data(**kwargs)
		context["keyword_list"] = KeyWord.objects.all()
		context["blogpost_list"] = BlogPost.objects.all().order_by('-posted');
		return context

class BlogPostDetailView(DetailView):
	
	model = BlogPost
	template_name = "blog/blogpost_detail.html"

	def get_context_data(self, **kwargs):
		context = super(BlogPostDetailView, self).get_context_data(**kwargs)
		context["blogpost"] = BlogPost.objects.get(slug=self.kwargs["slug"])
		return context

class SearchView(ListView):

	model = KeyWord
	template_name = "blog/search.html"

	def get_context_data(self, **kwargs):
		context = super(SearchView, self).get_context_data(**kwargs)
		context["keyword"] = KeyWord.objects.get(keyword=self.kwargs["keyword"])		
		return context