# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView

# from django.contrib.auth.models import User
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q,Subquery

from ..models import Blog, Comments, Follow
from ..forms import BlogForm, CommentForm, FollowForm

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
    paginate_by = 5
    # extra_context = None
    # page_kwarg = 'page'

    def get_queryset(self):
        # self.blog = get_object_or_404(Blog, pk=self.kwargs.get('pk'))
        # queryset = self.blog.objects.order_by('-modified_time').annotate(replies=Count('posts') - 1)
        # queryset = Blog.objects.order_by('-modified_time')

        # the_users_i_have_follow = Follow.objects.filter(user_id=self.request.user.id)
        # the_uesrs_i_have_follow_uuid = [ user.follow_id for user in the_users_i_have_follow ]

        # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#values-list
        # https://stackoverflow.com/questions/8556297/how-to-subquery-in-queryset-in-django
        # flat=True只能在只有一个值的情况下使用，会返回list而不是tuple.
        the_users_i_have_follow = Follow.objects.filter(user_id=self.request.user.id).values_list('follow_id', flat=True)
        # 仅显示已关注的人或者自已发的微博
        queryset = Blog.objects.filter(Q(post_by__in=the_users_i_have_follow)|Q(post_by=self.request.user.id)).order_by('-modified_time')

        return queryset

    def get_context_data(self, **kwargs):
        # 现在还用不上curpath这个参数。
        curpath = self.request.path
        context = super(BlogList, self).get_context_data(**kwargs)
        context['curpath'] = curpath
        return context

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
    # initial = {'belong_to_blog': blogid}

    # # def get(self, request, blogid, *args, **kwargs):
    # def get(self, request, *args, **kwargs):
    #     blogid = self.kwargs['blogid']
    #     return super(CommentView, self).get(request, *args, **kwargs)

    def get_form(self, form_class=None):
		# blogid是在url中捕获的。
        blogid = self.kwargs['blogid']
        commenterid = self.request.user.id

        form = super(CommentView, self).get_form(form_class)
        # 限制'belong_to_blog'的可选项,和BlogForm的__init__函数的实现原理相同，
        # 都是通过限制对应的queryset来达到目的。
        form.fields['belong_to_blog'].queryset = Blog.objects.filter(id=blogid)
        form.fields['comment_by'].queryset = User.objects.filter(id=commenterid)
        return form 
   
    def get_initial(self):
        blogid = self.kwargs['blogid']
        commenterid = self.request.user.id
        initial = {'belong_to_blog': blogid, 'comment_by': commenterid}
        return initial

  
decorators = [login_required]   
@method_decorator(decorators, name='dispatch')
class SearchView(ListView):
    model = Blog
    # queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/index.html'
    # # todo: 搜索结果的分布还不行.
    # paginate_by = 5
   
    def get_queryset(self):
        conditions = self.request.GET['search']
        queryset = Blog.objects.filter(
            Q(title__icontains=conditions) | Q(body__icontains=conditions)
        )
        return queryset

    def get_context_data(self, **kwargs):
        # curpara = self.request.GET # it's a dict.
        curpath = self.request.path
        context = super(SearchView, self).get_context_data(**kwargs)
        context['curpath'] = curpath
        return context


decorators = [login_required]   
@method_decorator(decorators, name='dispatch')
class FollowView(CreateView):
    model = Follow
    form_class = FollowForm 
    success_url = reverse_lazy('blog-index')
    template_name = 'blog/follow.html'
    # initial = {'belong_to_blog': blogid}

    def get_form(self, form_class=None):
        current_user = self.request.user

        form = super().get_form(form_class)
        form.fields['user'].queryset = User.objects.filter(id=current_user.id)
        # # 为form增加一个current_user属性，把当前用户传递到forms.py中
        # form.current_user = current_user

        # if self.request.method == 'POST':
        #     # form.other_user: uuid, string
        #     form.other_user = self.request.POST['follow']
        return form 

    def get_initial(self):
        userid = self.request.user.id
        initial = {'user': userid}
        return initial

    def post(self, request, *args, **kwargs):
        self.object = None

        form = self.get_form()
        if form.is_valid() and not self.is_follow():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def is_follow(self):

        current_user = self.request.user
        other_user = self.request.POST['follow']

        have_i_follow_this_guy = Follow.objects.filter(follow_id=other_user,user_id=current_user)
        if len(have_i_follow_this_guy) > 0:
            # toDo: 把这个错误返回到页面.
            print('# 你已经关注过这个用户了,不需要再关注了。')
            return True
        return False


