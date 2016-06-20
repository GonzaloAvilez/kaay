from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from . import forms
from . import models
from django.http import HttpResponse

from django.utils import timezone
from django.shortcuts import render
from .models import Post
from .forms import ShopFor,PostForm
import shop.models  



class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    
    http_method_names = ['get' ]

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        return super(ShowProfile, self).get(request, *args, **kwargs)

    


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "detalles de perfil almacenados")
        return redirect("profiles:show_self")




#add new product for sell
def post_new(request):
        if request.method == "POST":
            form = ShopFor(request.POST,
                         request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect("profiles:show_self")
        else:
            form = ShopFor()
        return render(request, 'profiles/product_add.html', {'form': form})

# def post_new(request):
#         if request.method == "POST":
#             form = PostForm(request.POST)
#             if form.is_valid():
                
#                 post = form.save(commit=False)
#                 post.author = request.user
#                 post.published_date = timezone.now()
#                 post.save()
#                 return redirect('/')
#         else:
#             form = PostForm()
#         return render(request, 'profiles/product_add.html', {'form': form})