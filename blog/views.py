from django.views.generic import TemplateView
from django.views.generic.base import View
from . import models
from forms import *
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext



class IndexView(TemplateView):

	model = models.Post
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(*kwargs)
		context['posts'] = self.model.objects.all()
		return context


class PostView(TemplateView):
	model = models.Post
	template_name = 'post.html'

	def get_context_data(self, **kwargs):
		context = super(PostView, self).get_context_data(**kwargs)
		context['post'] = self.model.objects.filter(slug=context['slug'])
		return context

class MyView(View):
	form = PostForm
	template_name = 'form.html'
	def post(self, request):
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			form = PostForm()
		
		return render(request, self.template_name, {'form': form})

def PostWrite(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			#newdoc = Post(img = request.FILES['img'])
			#newdoc.save()
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = PostForm()

	return render_to_response('form.html',context_instance = RequestContext(request,locals()))


"""def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['info@example.com']
			if cc_myself:
			    recipients.append(sender)

			from django.core.mail import send_mail
			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm() # An unbound form

	return render(request, 'form.html', {
		'form': form,
    })"""

	