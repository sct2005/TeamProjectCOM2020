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
