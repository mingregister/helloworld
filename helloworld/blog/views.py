# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.messages.views import SuccessMessageMixin

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

def redirect_blog(request):
    return redirect('/blog/1')


class BlogList(ListView):
    model = Blog
    queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/index.html'
    # paginate_by = 5

    # def get_context_data(self, **kwargs):
    #     kwargs['board'] = self.board
    #     return super().get_context_data(**kwargs)

    # def get_queryset(self):
    #     self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
    #     queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    #     return queryset


decorators = [login_required]   
@method_decorator(decorators, name='dispatch')
class PostView(SuccessMessageMixin, View):
    success_message = 'Congratulations!!!'           # it does not work now!!!
    # success_url = reverse_lazy('blog:author-list') # FormMixin

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

