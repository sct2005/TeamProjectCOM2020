# AI Failures Museum

A Django web application that helps people learn from real-world AI system failures. Instead of showcasing successful AI deployments, it focuses on where, how, and why AI-supported systems fail, so users can recognise limitations and potential warning signs in their own projects.

This project was developed for educational purposes (Team Project COM2020) and is not intended for commercial deployment.

---

## What the project does

- **Exhibit library** — Curated exhibits across domains (healthcare, tech, social media, finance, etc.) with structured failure context, system description, contributing factors, and lessons learned.
- **Browse & filter** — Home page with category filters and severity badges; each exhibit has a detailed page.
- **Interactive quizzes** — Multiple-choice quizzes per exhibit with randomised answers, immediate feedback, explanations, and score tracking (best score per user per exhibit).
- **Comments** — Visitors can post comments and nested replies on exhibits.
- **User accounts** — Sign up, login, profile (change username/password, delete scores, delete account).
- **Content management** — Curators create and edit exhibits (and quizzes via seed data) with Django admin; changes are logged for audit.

---

## Tech stack

- **Backend:** Django 6.x
- **Database:** SQLite (default; can be switched for production)
- **Media:** Local files (exhibit images under `backend/media/exhibits/images/`)

---

## Quick start (local development)

### 1. Prerequisites

- Python 3.10+
- pip

### 2. Clone and enter the project

```bash
git clone <repository-url>
cd TeamProjectCOM2020
```

### 3. Backend setup

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
```

*(If the repo has a root `requirements.txt` with only `django` and `Pillow`, use that or ensure Django and Pillow are installed.)*

### 4. Database and seed data

```bash
python manage.py migrate
python manage.py seed_exhibits
```

Seed data is read from `backend/exhibits/data/seed/exhibits.json` and `backend/exhibits/data/seed/quizzes.json`. Exhibit images are loaded from `backend/media/exhibits/images/` (see `backend/media/exhibits/images/README.md`).

### 5. Create a superuser (optional, for admin)

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in a browser.

- **Admin:** http://127.0.0.1:8000/admin/

---

## Deploying the website for others to use

To run the site so others can access it (e.g. on a server or cloud), follow these steps and adjust for your host.

### 1. Production settings

Before deployment:

- **Set a strong `SECRET_KEY`** — Do not use the default in `backend/museum/settings.py`. Use an environment variable, e.g. `SECRET_KEY = os.environ.get('SECRET_KEY', '')`.
- **Turn off debug:** `DEBUG = False`.
- **Set `ALLOWED_HOSTS`** to your domain(s) and/or IP, e.g. `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '123.45.67.89']`.
- **Use a real database** — For production, replace SQLite with PostgreSQL (or MySQL). Set `DATABASES` in settings and install the right driver (e.g. `psycopg2` for PostgreSQL).
- **Serve static and media files** — Either use your web server (Nginx/Apache) to serve `STATIC_ROOT` and `MEDIA_ROOT`, or use a separate static/media host. Run `python manage.py collectstatic` after setting `STATIC_ROOT` in settings.
- **Use HTTPS** — Configure SSL (e.g. Let’s Encrypt) and consider `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` in settings.

### 2. Example: run with Gunicorn (Linux/macOS)

From the **backend** directory:

```bash
pip install gunicorn
gunicorn museum.wsgi:application --bind 0.0.0.0:8000
```

Others can then reach the site at `http://<your-server-ip>:8000` (or your domain if DNS points there). For a proper deployment you would put Nginx (or another reverse proxy) in front of Gunicorn and serve static/media and HTTPS there.

### 3. Example: run on a Windows server

On Windows you can use **waitress** instead of Gunicorn:

```bash
pip install waitress
waitress-serve --listen=0.0.0.0:8000 museum.wsgi:application
```

Again, use a reverse proxy and HTTPS for a real deployment.

### 4. One-off setup on the server

On the deployment machine (from the **backend** directory):

```bash
python manage.py migrate
python manage.py seed_exhibits
python manage.py createsuperuser
python manage.py collectstatic --noinput   # after STATIC_ROOT is set
```

### 5. Checklist for “deploy for others to use”

| Item | Action |
|------|--------|
| Secret key | Use env var; never commit production key |
| Debug | `DEBUG = False` |
| Allowed hosts | Set to your domain(s) and/or server IP |
| Database | Prefer PostgreSQL/MySQL; run `migrate` |
| Static/media | Set `STATIC_ROOT` / `MEDIA_ROOT`, run `collectstatic`, serve via web server or CDN |
| HTTPS | Use SSL and secure cookie options in production |
| WSGI server | Use Gunicorn (Linux) or Waitress (Windows) behind a reverse proxy |

---

## Project structure (relevant parts)

```
TeamProjectCOM2020/
├── backend/
│   ├── manage.py
│   ├── museum/           # Django project (settings, urls, wsgi)
│   ├── exhibits/         # Main app (models, views, templates, urls)
│   │   ├── data/seed/    # exhibits.json, quizzes.json for seed_exhibits
│   │   ├── management/commands/
│   │   │   └── seed_exhibits.py
│   │   └── templates/exhibits/
│   └── media/exhibits/images/   # Exhibit images (referenced by seed or admin)
├── data/seed/            # Alternative seed location (if used)
└── requirements.txt     # Root deps (e.g. django, Pillow)
```

---

## Useful commands

| Command | Description |
|--------|-------------|
| `python manage.py runserver` | Run development server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py seed_exhibits` | Load/update exhibits and quizzes from JSON; removes DB questions no longer in JSON |
| `python manage.py createsuperuser` | Create admin user |
| `python manage.py collectstatic` | Gather static files into `STATIC_ROOT` (for production) |

---

## License and use

Developed for educational purposes. See repository and module documentation for any license or reuse terms.
