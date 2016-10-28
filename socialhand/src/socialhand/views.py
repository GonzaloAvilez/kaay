from django.views import generic

from django.shortcuts import render_to_response
from django.shortcuts import render
from .forms import ContactForm 

# Elasticsearch 
# from .forms import PostSearchForm


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get(self,request,*args,**kwargs):
    	form_class = ContactForm
    	kwargs['form'] = form_class
    	return super(HomePage,self).get(request,*args,**kwargs)


class AboutPage(generic.TemplateView):
    template_name = "about.html"

def contact(request):
	form_class= ContactForm
	return render(request,"contact.html",{'form':form_class},)
	

#view for elasticsearch 
# def notes(request):
#     form = PostSearchForm(request.GET)
#     posts = form.search()
#     return render_to_response('notes.html', {'posts': posts})


