# -*- coding:utf-8 -*-  

from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.core.urlresolvers import reverse

# Create your views here.

def home(request):
    return redirect(reverse('rootindex', args=[]))

def index(request):
    return render(request,'index.html')


# 实现是这样实现返回上一页了，但是是post还是get呢？不知道!
# 由于前端不会写
# Note that this will not work if the client disabled sending referrer information (for example, using a private/incognito browser Window). 
# In such a case it will redirect to /
class returnPreviousPage(View):
    def post(self):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))
