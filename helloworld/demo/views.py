from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return HttpResponse('demo response')

class MyView(View):
    
    def get(self, request):
        context = dict()
        return render(request, 'demo/cbv.html', context)

    def post(self, request):
        return HttpResponse('post it')

    def head(self, request):
        return HttpResponse('head it')

class MyTemplateView(TemplateView):
    template_name = 'demo/cbv.html'

    def post(self, request):

        return HttpResponse('post it2')
