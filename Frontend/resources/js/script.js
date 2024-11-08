const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const outputTextBox = document.getElementById('outputTextBox');

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#0056b3';
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.style.borderColor = '#007bff';
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#007bff';
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFileUpload(files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        handleFileUpload(file);
    }
});

function handleFileUpload(file) {
    // Here you would typically send the file to your server for processing
    // For demonstration, we'll just simulate an output
    outputTextBox.textContent = `Uploaded: ${file.name}. (Simulated output: No issues detected.)`;
}

