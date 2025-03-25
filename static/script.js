document.getElementById('conversionForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const resultText = document.getElementById('resultText');
    const form = event.target;
    const submitButton = form.querySelector('button');
  
    // Show loading message and disable the button
    resultText.textContent = "Converting...";
    submitButton.disabled = true;
  
    const expression = document.getElementById('expression').value;
    const conversionType = document.getElementById('conversionType').value;
  
    fetch('/convert', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ expression, conversion_type: conversionType })
    })
    .then(response => response.json())
    .then(data => {
      resultText.textContent = data.result;
    })
    .catch(error => {
      console.error('Error:', error);
      resultText.textContent = "An error occurred. Please try again.";
    })
    .finally(() => {
      submitButton.disabled = false;
    });
  });
  