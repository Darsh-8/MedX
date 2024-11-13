// Elements for file upload and result display
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const outputTextBox = document.getElementById('outputTextBox');
const diseaseDropdown = document.getElementById('diseaseDropdown');
const submitButton = document.getElementById('submitButton');
const progressBar = document.getElementById('progressBar');
const progressContainer = document.querySelector('.progress-container');

// New container for disease-specific fields
const formContainer = document.createElement('div');
formContainer.setAttribute('id', 'formContainer');
formContainer.style.display = 'none';
uploadArea.parentNode.insertBefore(formContainer, uploadArea);

// Function to dynamically create input fields based on selected disease
function createFields(fields) {
    formContainer.innerHTML = ''; // Clear any previous fields
    fields.forEach(field => {
        let input;
        
        // Check if the field is 'sex' and create a dropdown
        if (field === 'sex') {
            input = document.createElement('select');
            input.name = field;
            input.classList.add('form-control', 'custom-select');

            // Create 'Male' option (value 0)
            const maleOption = document.createElement('option');
            maleOption.value = '0';
            maleOption.textContent = 'Male';
            input.appendChild(maleOption);

            // Create 'Female' option (value 1)
            const femaleOption = document.createElement('option');
            femaleOption.value = '1';
            femaleOption.textContent = 'Female';
            input.appendChild(femaleOption);
        } else {
            // Default input field for other fields
            input = document.createElement('input');
            input.type = 'text';
            input.placeholder = field;
            input.name = field;
            input.classList.add('form-control', 'custom-input');
        }

        // Add margin to create space between fields
        input.style.marginBottom = '10px';
        input.style.marginLeft = '10px';

        formContainer.appendChild(input);
    });
}

// Event listener for dropdown selection
diseaseDropdown.addEventListener('change', () => {
    const selectedDisease = diseaseDropdown.value;
    uploadArea.style.display = 'none';
    formContainer.style.display = 'none';

    if (selectedDisease === 'heart-attack-prediction') {
        createFields(['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']);
        formContainer.style.display = 'block';
    } else if (selectedDisease === 'diabetes-prediction') {
        createFields(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']);
        formContainer.style.display = 'block';
    } else if (selectedDisease === 'parkinson-disease') {
        createFields(['MDVP_Fo_Hz', 'MDVP_Fhi_Hz', 'MDVP_Flo_Hz', 'MDVP_Jitter_percent', 'MDVP_Jitter_Abs', 'MDVP_RAP', 'MDVP_PPQ', 'Jitter_DDP', 'MDVP_Shimmer', 'MDVP_Shimmer_dB', 'MDVP_APQ', 'Shimmer_DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']);
        formContainer.style.display = 'block';
    } else {
        uploadArea.style.display = 'block'; // Show upload area for other diseases
    }
});

// Update submit button to handle form data or file upload
submitButton.addEventListener('click', async () => {
    const selectedDisease = diseaseDropdown.value;
    if (formContainer.style.display === 'block') {
        // Collect data from form fields including dropdowns
        const data = {};
        Array.from(formContainer.querySelectorAll('input, select')).forEach(input => {
            data[input.name] = input.value;
        });

        // Send data to the appropriate backend endpoint
        try {
            const response = await fetch(`https://mvp.medinnov.tech/api/${selectedDisease}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            console.log('Backend Response:', result); // Log the response to debug

            // Handle specific responses based on selected disease
            if (response.ok) {
                if (selectedDisease === 'heart-attack-prediction' && result.hasOwnProperty('heart_attack')) {
                    const prediction = result.heart_attack ? "True" : "False";
                    outputTextBox.textContent = `Heart Attack Prediction: ${prediction}`;
                } else if (selectedDisease === 'diabetes-prediction' && result.hasOwnProperty('prediction')) {
                    const prediction = result.prediction === 0 ? "False" : "True";
                    outputTextBox.textContent = `Diabetes Prediction: ${prediction}`;
                } else if (selectedDisease === 'parkinson-disease' && result.hasOwnProperty('prediction')) {
                    outputTextBox.textContent = `Parkinson's Disease Prediction: ${result.prediction}`;
                } else {
                    outputTextBox.textContent = result.error || "An error occurred during prediction.";
                }
            } else {
                outputTextBox.textContent = result.error || "An error occurred during prediction.";
            }
        } catch (error) {
            console.error('Error processing data:', error);
            outputTextBox.textContent = "An error occurred. Please try again later.";
        }
    } else if (selectedDisease) {
        // File upload flow for other diseases
        const file = fileInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('image', file);

            try {
                const response = await fetch(`https://mvp.medinnov.tech/api/${selectedDisease}/`, {
                    method: 'POST',
                    body: formData,
                });

                const result = await response.json();
                console.log('Backend Response:', result); // Log the response to debug

                if (response.ok && result.prediction) {
                    outputTextBox.textContent = `Prediction: ${result.prediction}, Confidence: ${result.confidence}`;
                } else {
                    outputTextBox.textContent = result.error || "An error occurred during prediction.";
                }
            } catch (error) {
                console.error('Error uploading file:', error);
                outputTextBox.textContent = "An error occurred. Please try again later.";
            }
        } else {
            outputTextBox.textContent = "Please select an image file to upload.";
        }
    }
});


