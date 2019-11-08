

def handle_uploaded_file(f):
    uploadfilename = '/tmp' + '/' + f.name
    with open(uploadfilename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
