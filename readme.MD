# Django Application

Welcome to the Django Application repository! This project is built with Django and provides a robust backend for handling various functionalities. This README will guide you through setting up, running, and contributing to the project.

## Table of Contents

- [Django Application](#django-application)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Documentation](#api-documentation)
  - [Contributing](#contributing)

## Installation

To get started with this Django application, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ayomidetobi/flat-booking-api.git
    ```

2. **Navigate into the project directory:**

    ```bash
    cd Flat Booking
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Your application should now be running at `http://localhost:8000/`.

## Usage

Provide a brief description of how to use your application. This could include how to interact with different parts of the application, how to perform common tasks, or any other relevant information.

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