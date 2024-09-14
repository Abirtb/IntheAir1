import React, { useState } from 'react';
import axios from 'axios';

const FileUploader = () => {
    const [file, setFile] = useState(null);

    const onFileChange = event => {
        setFile(event.target.files[0]);
    };

    const onFileUpload = async () => {
        if (!file) return;
        const chunkSize = 1024 * 1024 * 5; // 5 MB
        let start = 0;
        const totalChunks = Math.ceil(file.size / chunkSize);
        const file_id = Date.now();

        while (start < file.size) {
            const chunk = file.slice(start, Math.min(start + chunkSize, file.size));
            const formData = new FormData();
            formData.append('chunk', chunk);
            formData.append('file_id', file_id);
            formData.append('file_name', file.name);
            formData.append('chunk_number', start / chunkSize);
            formData.append('total_chunks', totalChunks);
            formData.append('is_last', start + chunkSize >= file.size);

            await axios.post('http://localhost:8000/chunk-uploads/upload/', formData);
            start += chunkSize;
        }
    };

    return (
        <div>
            <input type="file" accept=".tif" onChange={onFileChange} />
            <button onClick={onFileUpload}>Upload File</button>
        </div>
    );
};

export default FileUploader;
