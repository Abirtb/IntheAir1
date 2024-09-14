from django.db import models

class UploadedFile(models.Model):
    file_name = models.CharField(max_length=255)
    total_chunks = models.IntegerField()
    chunks_received = models.IntegerField(default=0)
    total_size = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)

class FileChunk(models.Model):
    uploaded_file = models.ForeignKey(UploadedFile, related_name='chunks', on_delete=models.CASCADE)
    chunk_number = models.IntegerField()
    data = models.BinaryField()
    is_last = models.BooleanField(default=False)
