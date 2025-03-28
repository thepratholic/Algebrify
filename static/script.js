document.addEventListener('DOMContentLoaded', function() {
  // ===================
  // 1) FORM SUBMISSION
  // ===================
  const conversionForm = document.getElementById('conversionForm');
  if (conversionForm) {
    conversionForm.addEventListener('submit', function(event) {
      event.preventDefault();

      const resultText = document.getElementById('resultText');
      const resultBox = document.getElementById('result');
      const submitButton = conversionForm.querySelector('button');
      const expressionInput = document.getElementById('expression');
      const conversionSelect = document.getElementById('conversionType');

      // Validate required elements
      if (!resultText || !resultBox || !submitButton || !expressionInput || !conversionSelect) {
        console.error('One or more required elements are missing.');
        return;
      }

      // Trim input and validate
      const expression = expressionInput.value.trim();
      if (!expression) {
        resultText.textContent = "Please enter a valid expression.";
        return;
      }
      const conversionType = conversionSelect.value;

      // Show loading state
      resultText.textContent = "Converting...";
      resultBox.classList.remove('show');
      submitButton.disabled = true;

      // Send POST request to conversion endpoint
      fetch('/convert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ expression: expression, conversion_type: conversionType })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        resultText.textContent = data.result || "No result returned.";
        // Trigger fade-in effect
        setTimeout(() => {
          resultBox.classList.add('show');
        }, 50);
      })
      .catch(error => {
        console.error('Error during conversion:', error);
        resultText.textContent = "An error occurred. Please try again.";
      })
      .finally(() => {
        submitButton.disabled = false;
      });
    });
  } else {
    console.error('Conversion form not found.');
  }

  // =====================
  // 2) HELP MODAL TOGGLE
  // =====================
  const openGuideButton = document.getElementById('openGuide');
  const closeGuideButton = document.getElementById('closeGuide');
  const guideModal = document.getElementById('guideModal');

  if (openGuideButton && closeGuideButton && guideModal) {
    openGuideButton.addEventListener('click', () => {
      guideModal.classList.remove('hidden');
    });

    closeGuideButton.addEventListener('click', () => {
      guideModal.classList.add('hidden');
    });

    // Close modal if user clicks outside the content area
    guideModal.addEventListener('click', (e) => {
      if (e.target === guideModal) {
        guideModal.classList.add('hidden');
      }
    });
  } else {
    console.error('Guide modal elements not found.');
  }
});
