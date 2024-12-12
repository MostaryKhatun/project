# Personal Poetry Platform

A web-based platform to showcase personal poems, manage user registrations, and provide wishlist functionality for poems. This project is built using Django as the backend framework.

## Project Structure

```
MY_PROJECT/
├── PersonalPoetryPlt/
│   ├── __pycache__/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── poems/
│   ├── __pycache__/
│   ├── migrations/
│   │   ├── __pycache__/
│   │   ├── 0001_initial.py
│   │   ├── 0002_rename...
│   │   ├── 0003_poem_c...
│   ├── templates/poems/
│   │   ├── base.html
│   │   ├── create_poem.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── poem_detail.html
│   │   ├── poem_list.html
│   │   ├── register.html
│   │   ├── wishlist.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── media/
│   ├── poem_images/
│   ├── poems/
├── static/
│   ├── poems/
│   │   ├── style.css
├── staticfiles/
├── venv/
├── db.sqlite3
├── manage.py
├── requirements.txt
```

## Features

- **User Authentication:**
  - User registration
  - Login/Logout functionality
  
- **Poem Management:**
  - Create, view, and manage personal poems.
  - View poem details and comments.

- **Wishlist Functionality:**
  - Add poems to the wishlist.
  - View and remove poems from the wishlist.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd MY_PROJECT
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run migrations:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```bash
   python manage.py runserver
   ```

9. Access the application at `http://127.0.0.1:8000/`.

## Static Files

Ensure that static files are collected and served:
1. Add static files to `static/poems/style.css`.
2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
3. Update `settings.py` to configure the `STATICFILES_DIRS` and `STATIC_ROOT` appropriately.

## Key Files

### `settings.py`
- Contains the project configurations.
- Set `DEBUG = True` for development and configure the `DATABASES` for your database.

### `urls.py`
- Maps URLs to the corresponding views in the application.

### `views.py`
- Handles the logic for user authentication, poem management, and wishlist functionality.

### `models.py`
- Defines the database structure for Poems, Comments, and Wishlist items.

### `templates/`
- Contains HTML templates for the platform.

### `static/`
- Contains CSS and other static resources.

## License
This project is licensed under the MIT License.

