// src/App.js

import React from 'react';
import FileUploader from './components/FileUploader';
import FileList from './components/FileList';

function App() {
    return (
        <div className="App">
            <h1>File Upload System</h1>
            <FileUploader />
            <FileList />
        </div>
    );
}

export default App;
