# chunkuploader/urls.py

from django.urls import path
from .views import FileChunkUploadView, FileListView

urlpatterns = [
    path('upload/', FileChunkUploadView.as_view(), name='upload_chunk'),
    path('files/', FileListView.as_view(), name='list_files'),
]
