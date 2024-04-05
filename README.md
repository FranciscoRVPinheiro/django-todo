## Installation

Clone the repository:

```bash
git clone https://github.com/FranciscoRVPinheiro/django-todo.git

```

Navigate to the project directory:

```bash
cd django-todo
```

## Usage/Examples

This project uses Docker and Docker Compose to manage its environment. To start the project, run:

```bash
docker-compose up
```

This will start the Django application and the PostgreSQL database. The Django application will be available at `http://localhost:8000`.

## Environment Variables

This project uses environment variables for configuration. These are stored in a `.env` file. You need to create this file in the project root and add the following variables:

```env
DB_PASSWORD=''
DB_NAME=''
USERNAME=''
SECRET_KEY=''
DEBUG=''
HOST=''
PORT=''
POSTGRES_DB=''
POSTGRES_USER=''
POSTGRES_PASSWORD=''
```

## Running Tests

To run tests, execute:

```bash
docker-compose run web python manage.py test
```
