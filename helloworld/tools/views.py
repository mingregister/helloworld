from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView

from .forms import UploadFileForm
from .forms import FileFieldForm

from .utils import handle_uploaded_file

# Create your views here.

def index(request):
    # return HttpResponse('hello tools')
    return render(request, 'tools/index.html')


def function1(request):
    return render(request, 'tools/f1.html')

# # 上传文件
# https://blog.csdn.net/qq_26914391/article/details/90667323
# https://cloud.tencent.com/developer/ask/50896
# http://blog.chinaunix.net/uid-21633169-id-4349787.html
def uploadFile(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('fileField', None)
        if upload_file is None: 
            return HttpResponse('No file get')
        else:
            handle_uploaded_file(upload_file)
            return HttpResponse('upload file %s success' % upload_file.name)
    else:
        form = UploadFileForm()
        # return render(request, 'tools/f1.html')
    return render(request, 'tools/f1.html', {'form': form})


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'tools/f1.html'
    # success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                # Do something with each file.
                handle_uploaded_file(f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def function2(request):
    return HttpResponse('function 2')


def function3(request):
    return HttpResponse('function 3')
