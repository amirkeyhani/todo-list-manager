# Django Todo List

This folder contains project code for the building a todo-list manager app with Django.

## Setup Instructions

1. Navigate into the project directory (`source_code/`).
2. Create a virtual environment in a `env/` folder by typing `python -m venv env` in your console.
3. Activate the venv using `source env/bin/activate` (Linux, MacOS) or `env\Scripts\activate.bat` (Windows).
4. Install the dependencies with `python -m pip install -r requirements.txt`
5. Generate the empty SQLite database and tables using `python manage.py migrate`
5. Run the app with `python manage.py runserver`
6. Browse to the app home page at `http://localhost:8000/` to see the list of todo lists, which will initially be empty. 

You can now start using the UI to add your to-do lists and to-do items to the database. The data will be stored in a new `db.sqlite3` file in the root of your project directory.

You can also use Django's auto-generated admin interface at `http://localhost:8000/admin/` to view, add, and edit the data.
