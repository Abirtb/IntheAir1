import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FileList = () => {
    const [files, setFiles] = useState([]);

    useEffect(() => {
        const fetchFiles = async () => {
            const response = await axios.get('http://localhost:8000//chunk-uploads/files/');
            setFiles(response.data.files);
        };
        fetchFiles();
    }, []);

    const handleDelete = async (fileId) => {
        await axios.delete(`http://localhost:8000/chunk-uploads/files/?file_id=${fileId}`);
        setFiles(files.filter(file => file.id !== fileId));
    };

    return (
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Size</th>
                    <th>Upload Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {files.map(file => (
                    <tr key={file.id}>
                        <td>{file.file_name}</td>
                        <td>{file.total_size}</td>
                        <td>{new Date(file.upload_date).toLocaleDateString()}</td>
                        <td><button onClick={() => handleDelete(file.id)}>Delete</button></td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default FileList;
