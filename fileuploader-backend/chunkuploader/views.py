from django.http import JsonResponse
from rest_framework.views import APIView
from .models import UploadedFile, FileChunk
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class FileChunkUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_id = request.POST.get('file_id')
        chunk_number = int(request.POST.get('chunk_number'))
        is_last = request.POST.get('is_last', 'false') == 'true'
        chunk_data = request.FILES['chunk'].read()

        uploaded_file, created = UploadedFile.objects.get_or_create(
            id=file_id,
            defaults={'file_name': request.POST.get('file_name'), 'total_chunks': int(request.POST.get('total_chunks'))}
        )
        uploaded_file.chunks_received += 1
        uploaded_file.save()

        FileChunk.objects.create(
            uploaded_file=uploaded_file,
            chunk_number=chunk_number,
            data=chunk_data,
            is_last=is_last
        )

        if is_last:
            all_chunks = FileChunk.objects.filter(uploaded_file=uploaded_file).order_by('chunk_number')
            complete_file_data = b''.join([chunk.data for chunk in all_chunks])
            file_path = default_storage.save(f'media/{uploaded_file.file_name}', ContentFile(complete_file_data))
            uploaded_file.total_size = default_storage.size(file_path)
            uploaded_file.save()

        return JsonResponse({'status': 'success', 'file_id': uploaded_file.id})

class FileListView(APIView):
    def get(self, request, *args, **kwargs):
        files = UploadedFile.objects.all()
        return JsonResponse({'files': list(files.values('id', 'file_name', 'total_size', 'upload_date'))}, safe=False)

    def delete(self, request, *args, **kwargs):
        file_id = request.GET.get('file_id')
        try: 
            file = UploadedFile.objects.get(id=file_id)
            file.chunks.all().delete()
            file.delete()
            return JsonResponse({'status': 'success', 'message': 'File deleted successfully'})
        except UploadedFile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)
