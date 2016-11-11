from django.contrib import admin
from src.apps.blog.models import BlogPost, KeyWord
from pagedown.widgets import AdminPagedownWidget
from django.db import models

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ('title', 'posted', 'description', 'content', 'slug', 'keywords')}),
	]

	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget },
	}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(KeyWord)