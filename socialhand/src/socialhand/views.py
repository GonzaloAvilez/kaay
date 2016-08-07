from django.views import generic

from django.shortcuts import render_to_response
# from .forms import PostSearchForm





class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

#view for elasticsearch 
# def notes(request):
#     form = PostSearchForm(request.GET)
#     posts = form.search()
#     return render_to_response('notes.html', {'posts': posts})


