# chunkuploader/serializers.py
from rest_framework import serializers
from .models import UploadedFile, FileChunk

class FileChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileChunk
        fields = ['chunk_number', 'data', 'is_last']

class UploadedFileSerializer(serializers.ModelSerializer):
    chunks = FileChunkSerializer(many=True, read_only=True)
    
    class Meta:
        model = UploadedFile
        fields = ['id', 'file_name', 'total_chunks', 'total_size', 'upload_date', 'chunks']
