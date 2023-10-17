# Little Lemon Restaurant Website

Welcome to the Little Lemon Restaurant website project! This web application is designed to showcase the menu and menu items of a local neighborhood bistro. The project is built using the Django framework, providing a dynamic and interactive web experience for visitors.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Extras](#extras)

## Project Overview

Little Lemon is a local neighborhood bistro with a focus on providing a delightful dining experience. As part of their digital transformation, this website has been developed to enable visitors to view their menu and individual menu items. The project consists of two main parts:

1. **Menu Page**: This page displays the entire menu, including the name and price of each menu item. Visitors can browse through the available dishes.

2. **Menu Item Page**: This page allows visitors to view detailed information about a specific menu item. Visitors can click on an item from the Menu page to access this detailed view.

## Installation

To set up and run this project on your local machine, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/KwameNtaadu007/little-lemon-restaurant.git
```

2. Navigate to the project directory:

```bash
cd little-lemon-restaurant
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations to create the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Access the website by opening a web browser and visiting http://127.0.0.1:8000/.

8. To access the admin panel, visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

## Usage

### Menu Page

- Visit the home page to find the "Menu" link in the navigation menu.
- Click on the "Menu" link to access the Menu page.
- Browse through the list of menu items, including their names and prices.

### Menu Item Page

- From the Menu page, click on the name of a specific menu item to view more details.
- The Menu Item page will display the name, description, and price of the selected item.
- You can navigate back to the Menu page or other parts of the website using the provided links.

## Project Structure

The project structure includes the following key components:

- `littlelemon` (the project folder)
  - `restaurant` (the app folder)
    - `models.py`: Defines the database models for the Menu and Menu Item.
    - `views.py`: Contains view functions for rendering web pages.
    - `templates`: Stores HTML templates for the different pages.
    - `admin.py`: Registers models with the Django admin panel.
  - `settings.py`: Django project settings, including database configuration.
  - `urls.py`: URL routing for the project and the app.

## Contributing

Contributions to this project are welcome! If you find issues, have suggestions for improvements, or want to add new features, please open an issue or create a pull request.

## Extras

Creating a Django project involves several steps. Here's a guide on how to create a Django project:

1. **Prerequisites**:
   - Python: Ensure you have Python installed on your computer. You can download it from the official Python website (https://www.python.org/downloads/).

2. **Virtual Environment (Optional but Recommended)**:
   - It's a good practice to create a virtual environment to isolate your project's dependencies. To create a virtual environment, open your terminal or command prompt and run:

   ```bash
   # On macOS and Linux
   python3 -m venv myenv

   # On Windows
   python -m venv myenv
   ```

   Replace `myenv` with the name you want to give to your virtual environment. Activate the virtual environment:

   ```bash
   # On macOS and Linux
   source myenv/bin/activate

   # On Windows
   myenv\Scripts\activate
   ```

3. **Install Django**:
   - With your virtual environment activated, you can now install Django using pip:

   ```bash
   pip install Django
   ```

4. **Create a Django Project**:
   - To create a Django project, run the following command:

   ```bash
   django-admin startproject projectname
   ```

   Replace `projectname` with the name of your project. This will create a new directory with the project structure.

5. **Project Structure**:
   - Your project directory should now contain a structure like this:

   ```
   projectname/
   ├── manage.py
   └── projectname/
       ├── __init__.py
       ├── asgi.py
       ├── settings.py
       ├── urls.py
       └── wsgi.py
   ```

6. **Initialize the Database**:
   - Django uses a database to store data. To create the initial database structure, run the following commands:

   ```bash
   cd projectname
   python manage.py migrate
   ```

7. **Create an Admin User** (Optional):
   - You can create an admin user to manage the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set the username, email, and password.

8. **Run the Development Server**:
   - Start the Django development server with this command:

   ```bash
   python manage.py runserver
   ```

   You'll see output indicating that the server is running. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the Django "Welcome" page.

9. **Create Django Apps** (Optional):
   - You can create Django apps within your project to organize your code. For example, you can create an app for your website's blog, store, etc., using the `startapp` command:

   ```bash
   python manage.py startapp appname
   ```

10. **Configure URL Patterns**:
    - Define URL patterns for your project in the `urls.py` files.

11. **Create Models and Views**:
    - You can define database models in the `models.py` files and create views for your project in the `views.py` files.

12. **Create Templates and Static Files**:
    - You can create HTML templates and store static files (CSS, JavaScript, images) in the appropriate directories within your app.

13. **Run Migrations**:
    - When you define models, create migrations and apply them to the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

14. **Start Building Your Web Application**:
    - Now you can start building your web application by defining URL patterns, views, templates, and static files, as well as creating admin interfaces and handling data with Django's built-in ORM.



Happy Coding
