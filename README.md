# Project Management System

A web-based **Project Management System** built using **Django** to efficiently manage projects, modules, and tasks. This system supports two user roles: **Manager** and **Developer**, each with unique features for task management and project tracking.

## Features

### For Managers
- **Project Creation**: Create and manage projects with ease.
- **Module Creation**: Divide projects into multiple modules for better tracking.
- **Task Assignment**: Assign tasks to developers and set deadlines.
- **Task Overview**: View the status of all tasks across various projects.
- **Dashboard**: Access an interactive dashboard showing all active projects, modules, and their progress.

### For Developers
- **Task Tracking**: View tasks assigned to you in various projects.
- **Task Status**: Update task status with options such as "Not Started," "In Progress," and "Completed."
- **Task Monitoring**: View details of tasks, deadlines, and project requirements.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostGreSQL

## Installation & Setup

### 1. Clone the repository:
git clone https://github.com/ve-saurabh/Project-Management-System.git

### 2. Navigate to the project directory
cd Project-Management-System

### 3. Setup a virtual environment
python -m venv env

### 4. Activate the virtual environment
env\Scripts\activate

### 5. Apply database migrations
python manage.py migrate

### 6. Create SuperUser
python manage.py createsuperuser

### 7. Run the server
```bash
python manage.py runserver
