# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.messages.views import SuccessMessageMixin

from .models import Blog
from .models import Comments
from .forms import BlogForm, CommentForm

# Create your views here.

# # it is equal to BlogList(ListView)
# class IndexView(View):
#     
#     def get(self, request):
#         blogs = Blog.objects.all()
#         context = {'blogs': blogs}
#         return render(request, 'blog/index.html', context)


def redirect_blog(request):
    return redirect('/blog/1')


class BlogList(ListView):
    model = Blog
    # queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/index.html'
    paginate_by = 3
    # extra_context = None
    # page_kwarg = 'page'

    def get_queryset(self):
        # self.blog = get_object_or_404(Blog, pk=self.kwargs.get('pk'))
        # queryset = self.blog.objects.order_by('-modified_time').annotate(replies=Count('posts') - 1)
        queryset = Blog.objects.order_by('-modified_time')
        return queryset

    # def get_context_data(self, **kwargs):
    #     kwargs['board'] = self.board
    #     return super().get_context_data(**kwargs)

    # def get_context_object_name(self, object_list):
    #     """Get the name of the item to be used in the context."""
    #     if self.context_object_name:
    #         return self.context_object_name
    #     elif hasattr(object_list, 'model'):
    #         return '%s_list' % object_list.model._meta.model_name
    #     else:
    #         return None


decorators = [login_required]   
@method_decorator(decorators, name='dispatch')
class PostView(SuccessMessageMixin, View):
    success_message = 'Congratulations!!!'           # it does not work now!!!
    # success_url = reverse_lazy('blog:author-list') # FormMixin

    def get(self, request):
        userid = request.user.id
        form = BlogForm(initial={'blogger': userid},userid=userid)
        return render(request, 'blog/post_blog.html', {'form': form})

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            publisher = form.save()
            return redirect(reverse('blog-index', kwargs={}))
            # return redirect("/blog")
            # return redirect("/publisher/{pk}/detail".format(pk=publisher.pk))
        else:
            return HttpResponse('form is illeagle')


decorators = [login_required]   
@method_decorator(decorators, name='dispatch')
class CommentView(CreateView):
    model = Comments
    form_class = CommentForm
    success_url = reverse_lazy('blog-index')
    template_name = 'blog/comment.html'

    # # def get(self, request, blogid, *args, **kwargs):
    # def get(self, request, *args, **kwargs):
    #     blogid = self.kwargs['blogid']
    #     return super(CommentView, self).get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        blogid = self.kwargs['blogid']
        form = super(CommentView, self).get_form(form_class)
        # 限制'belong_to_blog'的可选项,和BlogForm的__init__函数的实现原理相同，
        # 都是通过限制对应的queryset来达到目的。
        form.fields['belong_to_blog'].queryset = Blog.objects.filter(id=blogid)
        return form 
