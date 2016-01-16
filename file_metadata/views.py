from django.http import JsonResponse

from file_metadata.forms import UploadFileForm

def upload_file(request):
    """This POST is safe since it causes no changes and file is discarded."""
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return JsonResponse({
                'name': request.FILES['file'].name,
                'size': request.FILES['file'].size,
                'type': request.FILES['file'].content_type
            })
    return JsonResponse({'file-metadata error': 'No File Uploaded'})