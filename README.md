# MedX 🩺

## Overview

Welcome to MedX, an innovative platform that leverages cutting-edge technology to provide instant medical analysis. Our application allows users to drag and drop medical images such as X-rays and MRIs to receive quick diagnostic results.

**Check out the live application [here](https://mvp.medinnov.tech).**

## Features

- **🖼️ Easy Upload**: Drag and drop your medical images for seamless analysis.
- **⚡ Instant Results**: Get diagnostic results in seconds.
- **🔍 Disease Detection**: Supports multiple conditions including:
  - Skin Cancer
  - Brain Tumour
  - Parkinson's Disease
  - Diabetes Prediction
  - Heart Attack Prediction

## Table of Contents

- Installation
- Frontend Setup (Laravel)
- Backend Setup (Django)
- Environment Variables
- Usage
- Contributing
- License

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/Darsh-8/MedX.git
cd MedX
```

## Frontend Setup (Laravel) 🚀

1. Navigate to the frontend directory:

    ```bash
    cd frontend
    ```

2. Install dependencies using Composer:

    ```bash
    composer install
    ```

3. Copy the `.env.example` file to `.env`:

    ```bash
    cp .env.example .env
    ```

4. Configure your environment variables in the `.env` file.

5. Generate the application key:

    ```bash
    php artisan key:generate
    ```

6. Run database migrations (if applicable):

    ```bash
    php artisan migrate
    ```

7. Run the Laravel development server:

    ```bash
    php artisan serve
    ```

## Backend Setup (Django) 🐍

1. Navigate to the backend directory:

    ```bash
    cd backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

## Usage

Access the application frontend at `http://localhost:8000` and the backend API at `http://localhost:8000/api`.

## Contributing 🤝

We welcome contributions! Please fork the repository and submit a pull request.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
