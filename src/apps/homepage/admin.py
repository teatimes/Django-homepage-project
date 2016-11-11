from django.contrib import admin
from src.apps.homepage.models import GuestPost

class GuestPostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ('title', 'posted', 'content', 'author')}),
	]

admin.site.register(GuestPost, GuestPostAdmin)