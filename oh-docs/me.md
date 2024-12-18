# System Overview

## System Overview and Purpose
This project is a blog application designed to allow users to create, read, update, and delete blog posts. The system provides a web interface for managing blog content and is built using the Django web framework.

## Technology Stack
- **Programming Language**: Python
- **Web Framework**: Django
- **Database**: SQLite
- **Containerization**: Docker

## Directory Structure and File Roles

### Root Directory
- **Dockerfile**: Configuration file for Docker to containerize the application.
- **README.md**: Documentation file providing an overview and instructions for the project.
- **requirements.txt**: List of Python dependencies required for the project.
- **manage.py**: Django's command-line utility for administrative tasks.
- **db.sqlite3**: SQLite database file.

### blog Directory
- **__init__.py**: Initializes the blog module.
- **admin.py**: Configuration for the Django admin interface.
- **apps.py**: Configuration for the blog application.
- **models.py**: Defines the data models for the blog application.
- **tests.py**: Contains test cases for the blog application.
- **views.py**: Handles the logic for rendering web pages.
- **urls.py**: URL routing configuration for the blog application.

#### blog/migrations Directory
- **0001_initial.py**: Initial database migration script.
- **__init__.py**: Initializes the migrations module.

#### blog/templates Directory
- **base.html**: Base template for the blog application.
- **post_confirm_delete.html**: Template for confirming the deletion of a blog post.
- **post_form.html**: Template for creating and editing blog posts.
- **home.html**: Template for the home page.
- **post_detail.html**: Template for displaying a single blog post.
- **post_list.html**: Template for listing all blog posts.

### blog_project_20241012 Directory
- **__init__.py**: Initializes the blog_project_20241012 module.
- **asgi.py**: ASGI configuration for the project.
- **settings.py**: Configuration settings for the Django project.
- **urls.py**: URL routing configuration for the project.
- **wsgi.py**: WSGI configuration for the project.
