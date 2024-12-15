# **Django REST API with Swagger Documentation**
## **Features**
\- Django REST Framework: Simplifies API development.
\- Swagger Documentation: Automatically generated interactive API docs.
\- Virtual Environment: Ensures an isolated development environment.
## **Prerequisites**
Ensure the following tools are installed on your machine:
\- Python (3.8 or higher)
\- Git
## **Setup Instructions**
Follow the steps below to set up and run this project on your local machine:
### **Step 1: Clone the Repository**
Run the following commands:

git clone <repository\_url>
cd <project\_directory>
### **Step 2: Create and Activate a Virtual Environment**
On Windows:

1\. Create a virtual environment:
`python -m venv venv`

2\. Activate the virtual environment:
`venv\Scripts\activate`
### **Step 3: Install Dependencies**
Install all required packages listed in requirements.txt:

`pip install -r requirements.txt`
### **Step 4: Apply Database Migrations**
Set up the database:
Create a database and user in MySQL.

Update settings.py with the database details:

`DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': '<database_name>',
'USER': '<username>',
'PASSWORD': '<password>',
'HOST': 'localhost',
}
}`

Apply migrations:
python manage.py migrate
### **Step 5: Run the Development Server**
Start the Django development server:

python manage.py runserver

The application will be available at: http://127.0.0.1:8000
### **Step 6: Access API Documentation**
\- Swagger UI: http://127.0.0.1:8000/swagger/

\- ReDoc UI: http://127.0.0.1:8000/redoc/

## **Common Commands**
To deactivate the virtual environment:
deactivate

To add new dependencies:
1\. Install the required package:

`pip install <package\_name>`

2\. Update requirements.txt:

`pip freeze > requirements.txt`


## audio snippets from json file
`curl -X POST -F "audio_file=@audio.mp3" -F "timestamps=[{\"start\":0,\"end\":10},{\"start\":12,\"end\":22}]" http://127.0.0.1:8000/api/audio-snippets/`