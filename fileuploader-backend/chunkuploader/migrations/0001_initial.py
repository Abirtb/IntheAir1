# Generated by Django 5.1 on 2024-08-25 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('total_chunks', models.IntegerField()),
                ('chunks_received', models.IntegerField(default=0)),
                ('total_size', models.IntegerField(default=0)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileChunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chunk_number', models.IntegerField()),
                ('data', models.BinaryField()),
                ('is_last', models.BooleanField(default=False)),
                ('uploaded_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chunks', to='chunkuploader.uploadedfile')),
            ],
        ),
    ]
