<h1 align="center"> MedX </h1>
<p align="center"> Empowering Health Decisions with AI-Driven Diagnostics </p>

<p align="center">
  <img alt="Build" src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge">
  <img alt="Issues" src="https://img.shields.io/badge/Issues-0%20Open-blue?style=for-the-badge">
  <img alt="Contributions" src="https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>
<!-- 
  **Note:** These are static placeholder badges. Replace them with your project's actual badges.
  You can generate your own at https://shields.io
-->

---

## Table of Contents
- [⭐ Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🛠️ Tech Stack & Architecture](#️-tech-stack--architecture)
- [🚀 Getting Started](#-getting-started)
- [🔧 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)

---

## ⭐ Overview

MedX is an innovative, AI-powered platform designed to provide accessible and preliminary diagnostic insights for a range of critical medical conditions.

> The increasing prevalence of chronic diseases and the complexity of medical diagnosis often lead to delays, misinterpretations, and a heavy burden on healthcare systems. Accessible and accurate early detection is crucial for effective treatment and improved patient outcomes.

MedX offers an elegant solution by leveraging state-of-the-art machine learning models to assist in the early identification of potential health issues. Our platform empowers users with preliminary information, fostering proactive health management and facilitating timely medical consultations.

### Inferred Architecture
MedX is structured as a robust, full-stack application designed for scalability and maintainability. It comprises:
*   **Frontend:** A dynamic and interactive user interface built with the **Laravel** framework, featuring modern web technologies like **Vite** and **Tailwind CSS**. This layer handles user interactions, data presentation, and integrates an intelligent chatbot for guided assistance.
*   **Backend:** A powerful **Django REST API** serving as the core intelligence hub. This backend hosts and exposes a suite of advanced **Machine Learning models** specialized in various medical diagnostic predictions. It manages data processing, model inference, and secure API endpoints.

This decoupled architecture ensures that the user experience is fluid and responsive, while the diagnostic capabilities are robust, high-performing, and easily extensible.

---

## ✨ Key Features

MedX is engineered to provide a comprehensive and user-centric diagnostic experience:

*   **Multi-Modal AI Diagnostics:** Leverages diverse machine learning models to provide predictions and insights for a range of conditions including:
    *   **Heart Attack Risk Prediction:** Utilizing models like KNN for data-driven risk assessment.
    *   **Skin Cancer Detection:** Employing image processing and deep learning for preliminary lesion analysis.
    *   **Parkinson's Disease Prediction:** Harnessing SVM models for early indication based on input data.
    *   **Brain Tumour Detection:** Utilizing advanced deep learning models (e.g., ResNet50, Keras models) for image-based anomaly detection.
    *   **Diabetes Prediction:** Applying ML models like SVM for risk evaluation.
*   **Intuitive User Interface:** A modern, responsive web application built with Laravel and styled with Tailwind CSS, ensuring a seamless and engaging user experience across devices.
*   **Intelligent Chatbot Integration:** An integrated BotMan-powered chatbot provides interactive assistance, guides users through the diagnostic process, and offers quick access to information.
*   **Scalable & Modular Backend:** A well-structured Django REST Framework API allows for easy integration of new machine learning models and ensures high availability and performance for diagnostic requests.
*   **Robust Data Management:** Secure and efficient handling of user data and diagnostic inputs, ensuring privacy and reliability throughout the prediction process.

---

## 🛠️ Tech Stack & Architecture

MedX is built upon a foundation of cutting-edge technologies, carefully selected for performance, reliability, and developer experience.

| Technology            | Purpose                                   | Why it was Chosen                                                                      |
| :-------------------- | :---------------------------------------- | :------------------------------------------------------------------------------------- |
| **Laravel (PHP)**     | Frontend Web Framework                    | For its robust MVC architecture, rapid development capabilities, and extensive ecosystem. |
| **Django (Python)**   | Backend Web Framework                     | Provides a "batteries-included" approach, excellent REST API support, and seamless ML integration. |
| **Python**            | Backend Logic & Machine Learning          | The industry-standard language for AI/ML development, offering powerful libraries and tools. |
| **TensorFlow/Keras**  | Deep Learning Framework                   | For building and deploying high-performance neural network models, especially for image-based diagnostics. |
| **Scikit-learn**      | Machine Learning Library                  | Essential for traditional machine learning algorithms used in predictive modeling (e.g., SVM, KNN). |
| **Django REST Framework** | API Development                           | For building powerful, flexible, and scalable RESTful APIs that expose ML model functionalities. |
| **Vite**              | Frontend Build Tool                       | Delivers blazing-fast development server performance, hot module replacement, and optimized production builds. |
| **Tailwind CSS**      | Utility-First CSS Framework               | Enables rapid UI development with highly customizable classes, ensuring consistent and modern styling. |
| **BotMan (PHP)**      | Chatbot Framework                         | For easily integrating and managing conversational interfaces, enhancing user interaction within the frontend. |
| **SQLite**            | Development/Local Database                | A lightweight, file-based database ideal for local development and testing, requiring minimal setup. |

---

## 🚀 Getting Started

Follow these steps to get MedX up and running on your local machine.

### Prerequisites

Ensure you have the following software installed:

*   **Python:** Version 3.8+
*   **Node.js:** Version 18+ (includes `npm`)
*   **Composer:** PHP dependency manager
*   **PHP:** Version 8.1+
*   **Git:** Version Control System

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/MedX.git
    cd MedX
    ```

2.  **Backend Setup:**
    ```bash
    cd Backend

    # Create and activate a Python virtual environment
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    # venv\Scripts\activate

    # Install Python dependencies (Note: A requirements.txt is not provided in source,
    # so we infer common dependencies. You might need to adjust based on your exact setup.)
    pip install django djangorestframework numpy pandas scikit-learn tensorflow scikit-image pillow

    # Apply database migrations
    python manage.py makemigrations
    python manage.py migrate

    cd .. # Navigate back to the root directory
    ```

3.  **Frontend Setup:**
    ```bash
    cd Frontend

    # Install PHP dependencies
    composer install

    # Install Node.js dependencies
    npm install

    # Configure environment variables
    cp .env.example .env
    # Open the .env file and set up your application's base URL (APP_URL)
    # and ensure API_BASE_URL points to your Django backend (e.g., http://localhost:8000)

    # Generate an application key
    php artisan key:generate

    # Build frontend assets for production (optional for dev server)
    npm run build

    cd .. # Navigate back to the root directory
    ```

---

## 🔧 Usage

Once installed, you can start the MedX backend API and frontend application.

1.  **Start the Backend Server:**
    ```bash
    cd Backend
    source venv/bin/activate # Activate virtual environment if not already active
    python manage.py runserver
    # The Django backend API will typically be available at http://localhost:8000/
    ```

2.  **Start the Frontend Development Server:**
    ```bash
    cd Frontend
    npm run dev
    # The Laravel frontend development server will usually be available at http://localhost:5173/ (or similar Vite port)
    # Open this URL in your web browser to access MedX.
    ```

    *   For a production setup, you would typically run `php artisan serve` or configure a web server like Nginx/Apache to serve the `public/` directory after running `npm run build`.

### Example API Request (Skin Cancer Detection)

To interact with the backend API directly (e.g., for image-based diagnostics), you can use `curl` or any API client. Here's an example for the inferred Skin Cancer prediction endpoint:

```bash
# Ensure your backend server is running (http://localhost:8000/)
# Replace 'path/to/your/image.jpg' with the actual path to a skin lesion image file.
curl -X POST \
  -H "Content-Type: multipart/form-data" \
  -F "image=@path/to/your/image.jpg" \
  http://localhost:8000/skinCancer/predict/
```
*Note: The exact API endpoints may vary based on your backend's `urls.py` configuration.*

---

## 🤝 Contributing

We welcome and encourage contributions to MedX! Whether it's adding new diagnostic models, improving the UI, fixing bugs, or enhancing documentation, your efforts are highly appreciated.

To contribute:

1.  **Fork** the repository on GitHub.
2.  **Clone** your forked repository: `git clone https://github.com/your-username/MedX.git`
3.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name`
4.  **Make your changes**, ensuring code quality and adherence to best practices.
5.  **Test your changes** thoroughly.
6.  **Commit your changes** with clear and descriptive messages.
7.  **Push** your branch to your forked repository.
8.  **Open a Pull Request** to the `main` branch of the original MedX repository, describing your changes and their benefits.

Please ensure your code adheres to the project's coding standards.

---

## 📝 License

MedX is distributed under the MIT License. See the `LICENSE` file in the root of the repository for more information.

---
