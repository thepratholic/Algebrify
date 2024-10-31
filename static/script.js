document.getElementById('conversionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const expression = document.getElementById('expression').value;
    const conversionType = document.getElementById('conversionType').value;

    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression, conversion_type: conversionType })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultText').textContent = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});