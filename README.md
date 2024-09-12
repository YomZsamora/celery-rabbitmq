# Django Celery Background Tasks

This project integrates Celery with Django to handle background tasks using RabbitMQ as the message broker. The setup is containerized with Docker for modularity and ease of deployment.

## Description

This Django application leverages Celery to manage asynchronous tasks efficiently. It uses RabbitMQ for message brokering, ensuring smooth communication between Django and Celery workers. The project setup is designed to be modular and easy to configure.

## Specifications

- **Celery Integration:** Background task management with Celery.
- **RabbitMQ:** Message broker for handling communication between Django and Celery.
- **Docker:** Containerized environment for modular and scalable deployment.

## Prerequisites

- Python (v3.8 or higher)
- Django (v3.2 or higher)
- Celery (v5.4.0 or higher)
- RabbitMQ (via Docker)
- Docker (for containerization)

## Technologies Used

- **MySQL Connector/Python:** MySQL adapter for Python.
- **pytest:** Testing framework for unit and integration tests.
- **Django:** High-level Python web framework for rapid development.
- **Celery:** Asynchronous task queue for handling background tasks.
- **RabbitMQ:** Message broker used for communication between Celery and Django.
- **Docker:** Containerization of services for development and deployment.
- **Docker Compose:** Tool for defining and running multi-container Docker applications.

## Docker Compose Setup

This project uses Docker containerization for streamlined deployment and management. Follow these steps to set up and run the application with Docker Compose:

1. Make sure you have Docker and Docker Compose installed on your machine.
2. In the app directory of the project, create a `.env` file and add the following environment variables:
    ```sh
    # Database settings
    MYSQL_ENGINE=MySQL engine type (e.g., mysql.connector.django)
    MYSQL_DATABASE=Database name for the application
    MYSQL_USER=MySQL username
    MYSQL_PASSWORD=Password for the MySQL user
    MYSQL_ROOT_PASSWORD=Root password for MySQL
    MYSQL_HOST=Hostname where MySQL is running (e.g., celery-app-db)
    MYSQL_PORT=Port on which MySQL is listening (default is 3306)

    # Celery Configurations
    CELERY_BROKER_URL=URL to connect to the Celery broker (e.g., amqp://guest:guest@rabbitmq:5672/)
    CELERY_ACCEPT_CONTENT=Content types accepted by Celery (e.g., application/json,application/x-python-serialize)

    # Email configurations
    EMAIL_BACKEND=Backend for sending emails (e.g., django.core.mail.backends.smtp.EmailBackend)
    EMAIL_HOST=SMTP server hostname (e.g., smtp.gmail.com)
    EMAIL_PORT=Port for SMTP server (e.g., 587)
    EMAIL_USE_TLS=True or False for TLS
    EMAIL_HOST_USER=Email address for SMTP server authentication
    EMAIL_HOST_PASSWORD=Password for the SMTP server
    DEFAULT_FROM_EMAIL=Default sender email address
    ```
3. Build and start the containers using Docker Compose:
    ```sh
    docker-compose up --build -d
    ```
4. The application should now be running inside Docker containers. Verify that the services are up and running by checking the Docker logs:
    ```sh
    docker-compose logs celery-app
    docker-compose logs rabbitmq
    docker-compose logs celery-worker
    ```
5. Access the Application
   - The Django application can be accessed at [http://localhost:8023/](http://localhost:8023/).
   - The RabbitMQ management dashboard is available at [http://localhost:15672](http://localhost:15672), with the default credentials `guest:guest`.

## Features

The project emphasizes utilizing Celery for asynchronous task management in Django. It showcases this through a registration feature where email notifications are sent asynchronously post-registration, enhancing user experience by leveraging Celery's delay() method to queue the notification tasks without blocking the main application flow.

Key Features:
- **Asynchronous Task Processing:** Utilizes Celery to handle background tasks asynchronously.
- **Efficient Email Notification:** Sends email notifications to users after registration without blocking the application flow.

### Development

Want to contribute? Great! Here's how you can help:

- Fork the repo
- Create a new branch (git checkout -b feature-name)
- Make the appropriate changes in the codebase.
- Test your changes to ensure they work as expected.
- Commit your changes (git commit -m 'Add feature')
- Push to the branch (git push origin feature-name)
- Create a Pull Request explaining your changes.

### Running Tests

This project includes unit and integration tests to ensure the correctness of the codebase.

To run the tests:
```sh
docker-compose exec celery-app pytest
```
To run tests with coverage:
```sh
docker-compose exec celery-app pytest --cov=.
```

### Known Bugs

If you encounter any bugs or issues while using the application, please open an issue on the GitHub repository here. Be sure to include details of the issue and steps to reproduce it.

### License

*MIT License*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


