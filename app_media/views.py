from django.db import models
from django.shortcuts import render, redirect
from app_media.forms import DocumentForm, MultiFilesForm
from app_media.models import File



def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'app_media/file_form_upload.html', {'form': form
    })


def upload_files(request):
    if request.method == 'POST':
        form = MultiFilesForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/')

    else:
        form = MultiFilesForm()
    return render(request, 'app_media/upload_files.html', {'form': form
    })
