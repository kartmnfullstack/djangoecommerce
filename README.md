### Project Name

This is a django based Ecommerce V1 site which is designed for a ecommerce store. It's part of my freelancing portfolio. Visit my website at https://karthickfreelancing.com/

### 🚀 Features in V1:

* **User Authentication:** Robust login, registration, and personalized profile.
* **REST API:** Fully integrated API endpoints built with Django REST Framework for fetching data.
* **Admin Dashboard:** In built Django admin interface with slight modifications for data management.
* **Docker Support:** Ready for containerized local development and deployment.
* **Database:** SQLite (local development).
* **AJAX:** To prevent reloading and for instant response.
* **Pagination and Filtering:** Using Django's in built functions for filtering, searching,and pagination.
* **Cart persistant and messaging:** Functionality for shopping cart and messages to indicate actions happened.
* **Testing:** Unit and Integration testing enabled.
* **Automation Emails:** Celery and Redis used for sending automation emails.

### 🚀 Upcoming features in V2(November 8th,2026):
* Complete Checkout and Order Cycle
* Dummy Payment Integration
* Wishlist in Products  
* Responsiveness for product display and a few other pages
* Implementing AJAX for filtering and search. 

### 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your local machine: 

* Python (3.10 or higher)
* Pip and Virtualenv
* Git

### 📦 Installation & Setup

Follow these steps to get your development environment running. 

### 1. Clone the Repository


git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


### 2. Set Up a Virtual Environment

Create and activate a virtual environment to isolate project dependencies: 

Terminal via Command Prompt or Powershell in Windows, bash in macOS/Linux.

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies

Terminal via Command Prompt or Powershell in Windows, bash in macOS/Linux.

pip install --upgrade pip
pip install -r requirements.txt


### 4. Docker install

Use Command Terminal inside the project directory in a IDE or use the terminal in Docker to configure the project.
Create a yml file docker-compose.yml in the root of the project. You can also use the one provided in the project. 
Create a Dockerfile in the main project directory. You can also use the one provided in the project. 
Create a entrypoint.sh file for executing any initial commands that are needed. 

To start build: 

docker compose up -d --build    

To remove container:
docker compose down  

### 5. Run Database Migrations

The command is python manage.py migrate. First, create the model in the database via python manage.py makemigrations. For example, Docker can run migrations everytime it starts. To enable it, edit the entrypoint.sh file in root directory.

### 6. Create a Superuser

Create an administrative account to access the Django admin panel: 

python manage.py createsuperuser. This is configured to use email instead of username. 


### 7. Start the Development Server

Go inside Docker container exec or use terminal in VSCode 

python manage.py runserver

The application will be accessible at http://127.0.0.1:8001/. Access the admin panel at http://127.0.0.1:8001/admin/. 

### 🧪 Running Tests

To run the built-in test suite, use the following command: 

bash

python manage.py test

Use code with caution.

### 📁 Project Structure

ecommapp
├── account/                 #reserved for future use of enchancing user dashboard
│   ├── __init__.py
│   ├── admin.py             # for adding models to backend
│   ├── apps.py              # Global URL configurations
│   ├── models.py            # for adding models to backend
│   ├── tests.py             # Global URL configurations
│   └── views.py             # Server entry points
├── cart/                    # cart configurations
│   ├── __init__.py
│   ├── admin.py             # for adding cart models to backend
│   ├── apps.py              # for adding models to backend
│   ├── cartinit.py          # contains cart functions
│   ├── models.py            # for adding cart models
│   ├── tests.py             # Global URL configurations
│   └── views.py             # contains logic and views functionality for various functions of cart
├── checkout/                #reserved for future use of checkout
│   ├── __init__.py
│   ├── admin.py             # for adding models to backend
│   ├── apps.py              # Global URL configurations
│   ├── models.py            # for adding models to backend
│   ├── tests.py             # Global URL configurations
│   └── views.py             # Server entry points
├── ecommapp/                  #Main project configuration directory
│   ├── __init__.py
│   ├── asgi.py                # Asynchronous Server Gateway Interface for deployment
│   ├── settings.py            # project settings
│   ├── urls.py                # Global URL configurations
│   └── wsgi.py                # Web Server Gateway Interface for deployment
├── frontend/                  #contains all things with respect to user UI/UX
│   ├── static/                #used for serving static files-configured in settings.py and urls.py in main app file.
│        ├── logo1.jpg         #logo image
│        ├── main.css          #main css file
│        ├── script.js         #JS file for mobile menu 
│   ├── templates/                                  
│            ├── pages/                        #used for creating pages in html that are used in display
│                     ├── base.html            #Base page from which html pages are extended
│                     ├── cart.html            #Cart page which displays cart summary- protected page.
│                     ├── contact.html         #Contact page for getting in touch
│                     ├── dashboard.html       #Profile page- protected page.
│                     ├── index.html           #Home page
│                     ├── login.html           #Login page for login.
│                     ├── products.html        #Products page fir displaying products
│                     ├── register.html        #Register page for sign up.
│   ├── __init__.py
│   ├── admin.py             # for adding models to backend
│   ├── apps.py              # Global URL configurations
│   ├── models.py            # for adding models to backend
│   ├── urls.py              # Global URL configurations
│   ├── tests.py             # Global URL configurations
│   └── views.py             # contains functions and logic of html pages.
├── account/               #reserved for future use of enchancing user dashboard
│   ├── __init__.py
│   ├── admin.py             # for adding models to backend
│   ├── apps.py              # Global URL configurations
│   ├── models.py            # for adding models to backend
│   ├── tests.py             # Global URL configurations
│   └── views.py             # Server entry points
├── account/               #reserved for future use of enchancing user dashboard
│   ├── __init__.py
│   ├── admin.py             # for adding models to backend
│   ├── apps.py              # Global URL configurations
│   ├── models.py            # for adding models to backend
│   ├── tests.py             # Global URL configurations
│   └── views.py             # Server entry points
├── account/               #reserved for future use of enchancing user dashboard
│   ├── __init__.py
│   ├── admin.py             # for adding models to backend
│   ├── apps.py              # Global URL configurations
│   ├── models.py            # for adding models to backend
│   ├── tests.py             # Global URL configurations
│   └── views.py             # Server entry points 
├── core/                  # Main project configuration directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # Global URL configurations
│   └── wsgi.py / asgi.py  # Server entry points
├── apps/                  # Directory containing Django applications
│   └── users/             # Example custom app
├── templates/             # Global HTML templates
├── static/                # Global static files (CSS, JS, Images)
├── .env.example           # Template for environment variables
├── .gitignore             # Files ignored by Git
├── manage.py              # Django command-line utility
└── requirements.txt       # Project dependencies
├── .env.example           # Template for environment variables
├── .gitignore             # Files ignored by Git
├── manage.py              # Django command-line utility
└── requirements.txt       # Project dependencies

Use code with caution.

### 🚀 Deployment

This project is configured to collect static files prior to deployment: 

bash

python manage.py collectstatic --noinput

Use code with caution.

### 📝 License

Distributed under the MIT License. See LICENSE for more information.