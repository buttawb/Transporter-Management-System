# HGGC Transporter Management System

**Project Duration:** May 2024 - Present

## Overview

The HGGC Transporter Management System is designed to streamline transport operations for HGGC Transporters. This system facilitates the logistical requirements of procuring fuel from various oil marketing companies such as Total Parco, Go, and others, and distributing it to pumps nationwide. The primary focus of the project includes managing drivers, vehicles, oil marketing companies, vehicle manufacturers, trip records, and expenses.

## Project Details

### Key Features
- **Driver Management:** Comprehensive module for managing driver information and assignments.
- **Vehicle Management:** Detailed tracking of vehicles, including maintenance records and assignments.
- **Oil Marketing Companies:** Integration with multiple oil marketing companies for streamlined fuel procurement.
- **Vehicle Makers:** Database management of vehicle manufacturers for better inventory control.
- **Trip Records:** Logging and managing trip data to ensure accurate tracking and reporting.
- **Expense Management:** Monitoring and recording of expenses related to transportation operations.

### Development Progress
- **Architecture and Schema Design:** Completed. Provides a robust foundation for the system.
- **Digitization of Paperwork:** Existing paperwork is being digitized into MySQL for a seamless transition.
- **Driver Management Module:** Nearing completion, enabling efficient driver assignment and management.
- **Vehicle Management Module:** Underway, focusing on comprehensive vehicle tracking and maintenance.
- **Trip and Expense Management:** Currently in progress, aimed at providing detailed oversight of transportation activities and related costs.

## Technology Stack
- **Backend Framework:** Django
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Version Control:** Git

## How to Run

### Prerequisites
- Python 3.x installed
- MySQL installed and running
- Git installed (optional, for version control)

### Installation
1. **Clone the repository:**
- git clone https://github.com/buttawb/HGGC-WebApp.git
- cd HGGC-WebApp

2. **Install Python dependencies:**
- pip install -r requirements.txt

3. **Set up MySQL database:**
- Create a MySQL database for the project.
- Update `settings.py` with your database credentials.

4. **Apply database migrations:**
- python manage.py migrate

5. **You might need a superuser to Log In:**
- python manage.py createsuperuser
- Follow the prompts to enter a username, email address, and password for the superuser account.


### Running the Project
1. **Start the Django development server:**
- python manage.py runserver

2. **Open your web browser:**
- Go to `http://localhost:8000/` to view the application.

3. **Login:**
- Log In using the credentials of superuser you just created.
