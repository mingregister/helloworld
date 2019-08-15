from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
# from django.core.urlresolvers import reverse

# Create your views here.

def home(request):
    return redirect(reverse('rootindex', args=[]))

def index(request):
    return render(request,'index.html')
