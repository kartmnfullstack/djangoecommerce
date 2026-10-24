
Django E-Commerce Store (V1)

A robust, feature-rich Django e-commerce platform designed as a core showcase item for my freelancing portfolio. This project implements modern backend architecture patterns, automated asynchronous task queues, REST APIs, and containerized deployment workflows.
🔗 Live Portfolio: karthickfreelancing.com
💼 Developer: Karthick

🚀 Features in V1


Backend & Core Logic

• User Authentication: Custom robust signup, login, and personalized user profile dashboards built on a modified authentication backend.
• Persistent Shopping Cart: Fully functional persistent shopping cart tracking items across sessions, equipped with context messaging alerts.
• Pagination & Advanced Filtering: Fast searching, sorting, and page splits handled dynamically through native Django queries.

API & Modern Stack

• REST API Endpoints: Integrated API structure built via Django REST Framework (DRF) for structured data extraction and frontend scalability.
• Asynchronous Email Workflows: Background tasks powered by Celery and Redis for automated transactional and marketing emails.
• Dynamic Frontend Actions: Leverages AJAX requests to allow seamless actions without hard browser reloads.
• UI/UX Foundations: Basic interfaces structured using HTML5, Vanilla CSS3, and Vanilla JavaScript, work still remaining.

DevOps & Reliability

• Dockerized Environments: Production-ready containerized structure for standardized local development and scaling.
• Comprehensive Testing Suite: Integrated Unit and Integration testing layers validating standard user flows and product display along with database.
• Admin Dashboard: Tailored Django Admin workspace with modified metrics for swift data management.
• Local Database: Light standalone development data management via SQLite.

🚀 Upcoming Features in V2

• Complete Checkout Flow & Order Processing Cycle
• Sandbox / Dummy Payment Gateway Integration
• Product Wishlists & User Favorites Tab
• End-to-End Responsive UI Refactoring for Mobile Layouts and completion of UI/UX
• Migrating Filter/Search Mechanics to full AJAX architectures

🛠️ Prerequisites

Before installing, ensure your development machine has the following tools installed globally:
• Python (v3.10 or higher)
• Pip & Virtualenv
• Git
• Docker Desktop (Optional, required for containerized workflows)

📦 Installation & Setup


1. Clone the Repository

bash
git clone https://github.com
cd djangoadvancedecommerce

2. Set Up a Virtual Environment (Local Run Only)

Isolate dependencies using standard virtual environment structures.
On macOS / Linux:
bash
python3 -m venv venv
source venv/bin/activate
On Windows:
bash
python -m venv venv
venv\Scripts\activate

3. Install Project Dependencies

bash
pip install --upgrade pip
pip install -r requirements.txt

4. Database Migrations

Set up your database tables by executing:
bash
python manage.py makemigrations
python manage.py migrate

5. Create an Administrative Superuser

The user model is configured to authenticate using Email instead of a standard username.
bash
python manage.py createsuperuser

6. Run the Development Server

bash
python manage.py runserver
• Main Application Endpoint: http://127.0.0
• Django Admin Panel: http://127.0.0

🐋 Working with Docker

You can use the pre-configured Dockerfile, docker-compose.yml, and entrypoint.sh scripts to run the stack smoothly inside isolated containers.
Build and Start Containers (Detached Mode):
bash
docker compose up -d --build
Note: The entrypoint.sh file can be configured to automatically run migrations every time the container spins up.
Stop and Remove Active Containers:
bash
docker compose down

🧪 Running Tests

Execute the full suite of Unit and Integration test validations:
bash
python manage.py test

📁 Project Structure

text
djangoadvancedecommerce/
├── ecommapp/               # Main project configuration (settings, URLs, Celery)
├── account/                # Future expansion workspace for user dashboard extensions
├── cart/                   # Business logic for session tracking & cart utilities
├── checkout/               # Staging directory for incoming order workflows
├── orders/                 # Order creation structures (reserved for V2)
├── products/               # Product schemas, views, and DRF API Serializers
├── users/                  # Custom AbstractUser configuration, Celery tasks, and email engines
├── frontend/               # UI components 
│   ├── static/             # Global CSS stylesheets, Javascript actions, and brand media
│   └── templates/          # HTML Layouts (Base structures, public views, and protected pages)
├── media/                  # Server storage directory for dynamic backend uploads
├── Dockerfile              # Docker structural image config
├── docker-compose.yml      # Orchestration file for app services (Web, Redis, Database)
├── entrypoint.sh           # Runtime lifecycle execution scripts for containers
├── manage.py               # Native Django management CLI utility
└── requirements.txt        # Tracked project library dependencies

🚀 Production Deployment

Before pushing to your staging or production environments, execute the static collector routine:
bash
python manage.py collectstatic --noinput

📝 License

Distributed under the MIT License. See the LICENSE file for more details.
