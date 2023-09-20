# Django Application README

This README provides instructions for building and running the Django application using venv (virtual environment) and Docker.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python (3.9 or higher)
- Docker

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:


git clone <https://calvin147.github.io/Country_comp>

2. Create a Virtual Environment (Optional, but Recommended)
It's a good practice to use a virtual environment to isolate dependencies. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"

3. Install Dependencies
Install Python dependencies from the requirements.txt file:
pip install -r requirements.txt

4. Configure Django Settings
Ensure that your Django settings (e.g., country_comp/settings.py) are correctly configured, including the database settings and secret key. Refer to your Django project's specific configuration for details.

5. Apply Migrations (if applicable)
If your Django project includes database models, apply migrations:
python manage.py migrate

6. Start the Development Server
Run the Django development server:
python manage.py runserver
The application should now be accessible at http://127.0.0.1:8000/ in your web browser.

Running with Docker
1. Build the Docker Image
Build the Docker image from the project directory (where your Dockerfile is located):

docker build -t my-django-app .
2. Run the Docker Container
Run the Docker container, exposing port 8000 (adjust as needed):

docker run -p 8000:8000 my-django-app
The application should now be accessible at http://127.0.0.1:8000/ in your web browser.

Usage
Access the Django application in your web browser by navigating to http://127.0.0.1:8000/ (or the appropriate URL).
Follow the application's functionality to interact with it (e.g., voting for countries).
Contributing
If you'd like to contribute to this project, please follow our Contribution Guidelines.