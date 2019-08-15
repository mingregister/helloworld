# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Blog
from .forms import BlogForm

# Create your views here.

# class IndexView(View):
#     
#     def get(self, request):
#         blogs = Blog.objects.all()
#         context = {'blogs': blogs}
#         return render(request, 'blog/index.html', context)

# # it is equal to IndexView
class BlogList(ListView):
    model = Blog
    queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/index.html'


decorators = [login_required]   
@method_decorator(decorators, name='dispatch')
class PostView(View):

    def get(self, request):
        form = BlogForm()
        return render(request, 'blog/post_blog.html', {'form': form})

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            publisher = form.save()
            return redirect("/blog")
            # return redirect("/publisher/{pk}/detail".format(pk=publisher.pk))
        else:
            return HttpResponse('form is illeagle')

