from django.urls import path
from app_media.views import model_form_upload, upload_files

urlpatterns = [
path('model_form_upload_file/', model_form_upload, name='model_form_upload_file'),    
path('upload_files', upload_files, name='upload_files'),    

]