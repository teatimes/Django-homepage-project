from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from src.apps.homepage.forms import ContactForm
from django.views.generic import ListView
from django.core.mail import send_mail
from src.apps.homepage.models import GuestPost
from src.apps.blog.models import BlogPost

class HomeView(TemplateView):
	template_name = "homepage/home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		try:
			context["post"] = BlogPost.objects.order_by("posted")[0]
		except IndexError:
			pass
		return context

class PageOneView(TemplateView):
	template_name = "homepage/page_one.html"

class ContactView(FormView):
	template_name = "homepage/contact.html"
	form_class = ContactForm
	success_url = "/sendt/"
	
	def form_valid(self, form):
		subject = form.cleaned_data.get('subject')
		"""
		message = "%s / %s sent you the following message: ", % (
			form.cleaned_data.get('senders_name'),
			email=form.cleaned_data.get('senders_email')
		)
		"""
		message = "\n\n{0}".format(form.cleaned_data.get('message'))
		sender = form.cleaned_data.get('senders_email')
		recipients = ['test@gmail.com']
	
		send_mail(subject, message, sender, recipients)
		return super(ContactView, self).form_valid(form)

class SendtView(TemplateView):
	template_name = "homepage/sendt.html"
	
class PageTwoView(TemplateView):
	template_name = "homepage/page_two.html"

class PageThreeView(TemplateView):
	template_name = "homepage/page_three.html"

class FromGuestsView(ListView):

	model = GuestPost
	template_name = "homepage/from_guests.html"

	def get_context_data(self, **kwargs):
		context = super(FromGuestsView, self).get_context_data(**kwargs)
		context["guest_posts"] = GuestPost.objects.all()
		return context

class PageFourView(TemplateView):
	template_name = "homepage/page_four.html"

