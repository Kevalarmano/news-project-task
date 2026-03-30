# News Project – Django Capstone

## Overview

This project is a Django-based web application developed as part of a HyperionDev
capstone assignment. It demonstrates how to build, structure, document, and deploy
a Django application using version control (Git), Sphinx documentation, and Docker.

---

## Project Structure

```
news-project/
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── capstone.txt
├── docs/                        # Root-level Sphinx documentation
│   ├── Makefile
│   ├── make.bat
│   ├── build/html/              # Generated HTML docs (open index.html)
│   └── source/
│       ├── conf.py
│       └── index.rst
└── news_project/                # Django project root
    ├── manage.py
    ├── requirements.txt
    ├── db.sqlite3
    ├── news_project/            # Django settings & URL config
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── news/                    # Core news app
    │   ├── models.py
    │   ├── views.py
    │   ├── admin.py
    │   └── migrations/
    ├── news_app/                # API app
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   └── migrations/
    └── docs/                    # Inner Sphinx docs (auto-generated)
        ├── Makefile
        ├── make.bat
        └── source/
            └── conf.py
```

---

## Technologies Used

- Python 3.11
- Django 4.2 LTS
- Sphinx 7.3 (documentation)
- Docker & Docker Compose

---

## Option 1 – Run Locally with a Virtual Environment

### Prerequisites

- Python 3.9 or higher installed
- `pip` available on your PATH

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Kevalarmano/news-project.git
cd news-project

# 2. Create and activate a virtual environment
python -m venv venv

# On macOS / Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r news_project/requirements.txt

# 4. Apply database migrations
cd news_project
python manage.py migrate

# 5. (Optional) Create a superuser to access the admin panel
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open your browser at: **http://127.0.0.1:8000/**

Admin panel: **http://127.0.0.1:8000/admin/**

### Environment Variables

This project uses a default `SECRET_KEY` for development. For any
environment beyond local development you **must** set your own secret key
via an environment variable so it is never committed to source control:

```bash
export SECRET_KEY="your-very-secret-key-here"
```

Then update `settings.py` to read:

```python
SECRET_KEY = os.environ.get("SECRET_KEY")
```

---

## Option 2 – Run with Docker (Recommended)

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
  and running

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Kevalarmano/news-project.git
cd news-project

# 2. Build and start the container
docker-compose up --build

# To run in the background:
docker-compose up --build -d
```

Open your browser at: **http://127.0.0.1:8000/**

To stop the container:

```bash
docker-compose down
```

### Docker Notes

- Migrations are applied automatically when the container starts.
- The `SECRET_KEY` environment variable can be overridden in
  `docker-compose.yml` or passed at runtime – **do not hard-code production
  secrets in the compose file** for public repositories.

---

## Viewing the Documentation

Sphinx-generated HTML documentation is included in the repository so
reviewers can access it without rebuilding:

```
docs/build/html/index.html
```

Open that file in any web browser.

To **rebuild** the documentation yourself:

```bash
# From the repo root
cd docs
make html   # macOS / Linux
make.bat html   # Windows
```

---

## Git Branch Structure

| Branch      | Purpose                                      |
|-------------|----------------------------------------------|
| `main`      | Stable, deployable code                      |
| `docs`      | Docstrings + Sphinx documentation added      |
| `container` | Dockerfile and docker-compose.yml added      |

---

## Author

Keval Armano Ramchander

---

## Repository

https://github.com/Kevalarmano/news-project.git
