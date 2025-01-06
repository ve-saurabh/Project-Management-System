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

1. Clone the repository:
```bash
git clone https://github.com/ve-saurabh/Project-Management-System.git

3. Navigate to the project directory
```bash
cd Project-Management-System

4. Setup a virtual environment
```bash
python -m venv env

5. Activate the virtual environment
```bash
env\Scripts\activate

6. Apply database migrations
```bash
python manage.py migrate

7. Create SuperUser
```bash
python manage.py createsuperuser

8. Run the server
```bash
python manage.py runserver
