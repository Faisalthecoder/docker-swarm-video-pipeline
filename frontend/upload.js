document.getElementById('uploadForm').addEventListener('submit', async function(e){
    e.preventDefault();
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://api:5000/upload', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    alert(JSON.stringify(result));
});

