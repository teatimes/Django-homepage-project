from django.db import models
from django.utils.text import slugify
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class KeyWord(models.Model):
	keyword = models.CharField(max_length=20, unique=True)
	
	def __str__(self):
		return self.keyword

	def posts_with_keyword(self):
		return self.blogpost_set.all();

	def create_key(self, keyword):
		instance = self.create(keyword=keyword)
		return instance

class BlogPost(models.Model):
	title = models.CharField(max_length=100, unique=True)
	posted = models.DateField('date published', default=datetime.datetime.now)
	description = models.CharField(max_length=500)
	content = models.TextField(max_length=2000)
	slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
	keywords = models.ManyToManyField(KeyWord, blank=True)
	
	def __str__(self):
		return self.title

	#def save(self, *args, **kwargs):
	#	if self.slug == "":
	#		self.slug = self.title.replace(" ", "_")
	#	super(BlogPost, self).save(self, *args, **kwargs)
	
	def get_keywords(self):
		return self.keywords.all()

@receiver(pre_save, sender=BlogPost)
def create_slug(sender, instance, *args, **kwargs):
	if instance.slug == "":
		instance.slug = instance.title.replace(" ", "_")
		instance.save()

#pre_save.connect(create_slug, sender=BlogPost)