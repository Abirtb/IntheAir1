# IntheAir2

## Project Overview

This project is a file uploader system that allows users to upload large files in chunks. The system is composed of a backend and a frontend, both of which are containerized using Docker.

## Backend Setup

The backend is built using Django and Celery for handling asynchronous tasks. To set up the backend, follow these steps:

1. Navigate to the `fileuploader-backend` directory.
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - On Windows: `.\.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Run the Django development server: `python manage.py runserver`

## Frontend Setup

The frontend is built using React. To set up the frontend, follow these steps:

1. Navigate to the `fileuploader-frontend` directory.
2. Install the required packages: `npm install`
3. Start the development server: `npm start`

## Docker Usage

To run the entire application using Docker, follow these steps:

1. Ensure Docker is installed and running on your machine.
2. Navigate to the root directory of the project.
3. Build and start the Docker containers: `docker-compose up --build`
4. The backend will be available at `http://localhost:8000` and the frontend at `http://localhost:3000`.

## Project Structure

The project is structured as follows:

```
.
├── compose.yaml
├── fileuploader-backend
│   ├── chunkuploader
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_remove_uploadedfile_chunks_received.py
│   │   │   ├── 0003_uploadedfile_chunks_received.py
│   │   │   ├── 0004_uploadedfile_is_complete.py
│   │   │   ├── 0005_remove_uploadedfile_is_complete.py
│   │   │   ├── 0006_uploadedfile_file_data.py
│   │   │   ├── 0007_remove_uploadedfile_file_data.py
│   │   │   ├── 0008_uploadedfile_file_data.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── fileuploader
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
├── fileuploader-frontend
│   ├── public
│   │   ├── index.html
│   │   ├── manifest.json
│   │   ├── robots.txt
│   ├── src
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── components
│   │   │   ├── FileList.js
│   │   │   ├── FileUploader.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── logo.svg
│   │   ├── reportWebVitals.js
│   │   ├── setupTests.js
│   ├── package.json
│   ├── Dockerfile
│   ├── README.md
├── .gitignore
├── README.md
```

## Backend Models and Views

### Models

#### UploadedFile

The `UploadedFile` model represents a file that is being uploaded in chunks. It has the following fields:

- `file_name`: The name of the file.
- `total_chunks`: The total number of chunks the file is divided into.
- `chunks_received`: The number of chunks received so far.
- `total_size`: The total size of the file.
- `upload_date`: The date and time when the file was uploaded.
- `file_data`: The binary data of the file (optional).

#### FileChunk

The `FileChunk` model represents a chunk of a file. It has the following fields:

- `uploaded_file`: A foreign key to the `UploadedFile` model.
- `chunk_number`: The number of the chunk.
- `data`: The binary data of the chunk.
- `is_last`: A boolean indicating whether this is the last chunk of the file.

### Views

#### FileChunkUploadView

The `FileChunkUploadView` handles the uploading of file chunks. It processes the incoming chunks, updates the `UploadedFile` model, and creates `FileChunk` instances. When all chunks are received, it triggers a Celery task to combine the chunks into a complete file.

#### FileListView

The `FileListView` provides a list of all uploaded files. It supports both GET and DELETE requests. The GET request returns a list of files with their details, and the DELETE request allows deleting a specific file and its associated chunks.
