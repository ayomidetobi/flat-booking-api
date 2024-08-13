# Flat Booking Application

Welcome to the Flat Booking Application repository! This project is built with Django and provides a robust backend for handling simple flat booking functionalities. This README will guide you through setting up, running, and contributing to the project.

## Table of Contents

- [Flat Booking Application](#flat-booking-application)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Documentation](#api-documentation)
  - [Contributing](#contributing)
  - [Login Credentials](#login-credentials)

## Installation

To get started with this Django application, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ayomidetobi/flat-booking-api.git
    ```

2. **Navigate into the project directory:**

    ```bash
    cd flat-booking-api
    ```
3. **Ensure you have Python 3.12.3 installed:**
    This project requires Python version 3.12.3. You can download and install it from the [official Python website](https://www.python.org/downloads/).


4. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

5. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

6. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

7. **Configure the environment variables:**

    - Create a `.env` file at the root of the project and add the following code:

      ```plaintext
      DEBUG=True
      SECRET_KEY=django-insecure-0y@huwu-7*k#d4t**r5a+_m0qh&r=^)p47==!4d=qzd8#8oi=3
      DATABASE_URL=********
      ```

8. **Database Configuration:**

    - By default, the project is configured to use a PostgreSQL database. To switch to using SQLite, follow these steps:

      - Open the `settings.py` file in the `Booking` application.
      - Comment out the PostgreSQL configuration.
      - Uncomment the SQLite database configuration.
      
      **Before:**
      ```python
      DATABASES = {
        'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
        )
        }
      ```

      **After:**
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.sqlite3',
              'NAME': BASE_DIR / 'db.sqlite3',
          }
      }
      ```

    - Apply database migrations:

      ```bash
      python manage.py migrate
      ```

9. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Your application should now be running at `http://localhost:8000/`.

    - Visit `http://localhost:8000/admin` to access the Django admin panel.

## Usage

This API is used to manage a simple flat booking system, allowing users to create, update, and view bookings for available flats. It handles booking requests and provides details on current and past reservations.

## API Documentation

You can find the API documentation for this project at the following link:

[API Documentation](https://app.swaggerhub.com/apis-docs/AYOMIDESTOBSY10/flat-api/1.0.0#/Bookings)

Here is a preview of the API documentation:

![API Documentation](https://res.cloudinary.com/db3jcvkrw/image/upload/v1723285645/flat-api-doc_fidii6.jpg)

## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Login Credentials

- **Username:** `admin`
- **Password:** `admin`

If the login fails, run the following command to load the initial data:

```bash
python manage.py loaddata data.json
```
If it still doesn't work, create a superuser:

```
python manage.py createsuperuser
```
Access URLs
Django Admin: http://localhost:8000/admin
API Base URL: http://localhost:8000/api