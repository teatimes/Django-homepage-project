from django.db import models

class GuestPost(models.Model):
	title = models.CharField(max_length=100, unique=True)
	posted = models.DateField('date published')
	content = models.TextField(max_length=2000)
	author = models.CharField(max_length=200)

	def __str__(self):
		return self.title

	