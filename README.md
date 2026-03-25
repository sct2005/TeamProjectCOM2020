# AI Failures Museum

A Django web application for learning from real-world AI system failures: curated case studies, structured failure context, quizzes, discussion, and role-based content management. Built for **Team Project COM2020** (Group Java The Hutt), final coursework submission. Educational use only; not intended for commercial deployment.

**Coursework materials** (report, handover pack, ethics, testing evidence, slides) live under `GroupJava_The_Hutt_CW2/`.

---

## What the application does

- **Exhibit library** — Case studies with domain, deployment context, system description, failure narrative, contributing factors (including data, technical, and organisational angles where captured), lessons learned, optional image and supporting artefact links.
- **Browse, search, and filter** — List and detail pages with category-style filtering; bookmark exhibits when signed in.
- **Quizzes** — Multiple-choice questions per exhibit with feedback, explanations, and best-score tracking per user; curators can add, edit, and delete quiz questions in-app.
- **Comments** — Threaded comments and replies on exhibits; users can remove their own comments; admins have broader moderation tools.
- **Accounts and profiles** — Sign up, log in, profile (change username/password, clear quiz scores, delete account).
- **Roles (RBAC)** — **User** (browse, comment, quiz, bookmarks), **Curator** (create/edit/delete exhibits and manage quizzes), **Admin** (curator capabilities plus user management: roles, moderation, deleting users/scores). Implemented via `UserProfile.access_level` and decorators in `backend/exhibits/decorators.py`.
- **Django admin** — Standard admin for models; complements in-app curator flows.
- **Health check** — `GET /health/` returns JSON `{"status": "ok"}` for simple uptime checks.

---

## Tech stack

| Area | Choice |
|------|--------|
| Framework | Django 6.x (see `backend/requirements.txt` for pinned version) |
| Database | SQLite (`backend/db.sqlite3` by default) |
| Images | Pillow; files under `backend/media/` |
| Tests | Django `TestCase` and pytest-style tests under `backend/exhibits/tests/` |

---

## Prerequisites

- **Python 3.10+** and `pip`
- **Git** (if cloning from a remote)

---

## Quick start (local development)

### 1. Open a terminal in the repository root

The folder name may be `TeamProjectCOM2020`, `TeamProjectCOM2020-main`, or similar.

### 2. Create a virtual environment and install dependencies

```bash
cd backend
python -m venv venv
```

Activate it:

- **Windows:** `venv\Scripts\activate`
- **macOS / Linux:** `source venv/bin/activate`

Install packages (recommended: pinned set used for development and reporting):

```bash
pip install -r requirements.txt
```

A minimal install is also possible from the **repository root** with `pip install -r requirements.txt` (Django + Pillow only), but the full list in `backend/requirements.txt` matches the documented environment.

### 3. Database and seed data

Still inside `backend/` with the venv active:

```bash
python manage.py migrate
python manage.py seed_exhibits
```

Seed files are **`backend/exhibits/data/seed/exhibits.json`** and **`backend/exhibits/data/seed/quizzes.json`**. Exhibit images are expected under **`backend/media/exhibits/images/`** (see `backend/media/exhibits/images/README.md`).

### 4. Admin access (optional)

- **Django superuser** (admin site): `python manage.py createsuperuser`
- **Application “admin” role** (RBAC): after a user exists, run  
  `python manage.py set_admin <username>`  
  to set `UserProfile.access_level` to admin (needed for in-app admin user tools).

### 5. Run the development server

```bash
python manage.py runserver
```

- **Site:** http://127.0.0.1:8000/
- **Django admin:** http://127.0.0.1:8000/admin/
- **Health:** http://127.0.0.1:8000/health/

With `DEBUG=True`, Django serves uploaded media from `MEDIA_ROOT` automatically.

---

## Optional: VS Code / GitHub Codespaces

The `.devcontainer/` configuration uses **Python 3.11** and runs `pip install -r requirements.txt` from the **repository root** on container create. After the container is ready, open a terminal, `cd backend`, run `migrate`, `seed_exhibits`, and `runserver` as above. For the same dependency set as local development, install from `backend/requirements.txt` inside the container if needed.

---

## Project layout (high level)

```
TeamProjectCOM2020-main/
├── backend/
│   ├── manage.py
│   ├── museum/                 # Project settings, root urls, WSGI
│   ├── db.sqlite3              # Created after migrate (local dev)
│   ├── requirements.txt        # Pinned dependencies
│   ├── pytest.ini
│   └── exhibits/               # Main app
│       ├── data/seed/          # exhibits.json, quizzes.json
│       ├── management/commands/  # seed_exhibits, set_admin
│       ├── templates/, static/
│       └── tests/
├── docs/                       # security notes, licence decision, etc.
├── GroupJava_The_Hutt_CW2/     # CW2 submission (report, handover, ethics, tests PDFs, slides)
├── requirements.txt            # Minimal root deps (e.g. Codespaces)
└── README.md
```

---

## Useful commands

| Command | Description |
|--------|-------------|
| `python manage.py runserver` | Development server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py seed_exhibits` | Load/update exhibits and quizzes from JSON (DB aligned with seed) |
| `python manage.py createsuperuser` | Django admin superuser |
| `python manage.py set_admin <username>` | Promote user to application admin role |
| `python manage.py collectstatic` | Collect static files for production |
| `python manage.py test` | Run automated tests (from `backend/`) |

---

## Documentation and licence

- **Security checklist (summary):** `docs/security.md`
- **Licence decision (MIT):** `docs/decisions/licence-decision.md`
- **Handover pack (deployment, maintenance, index):** `GroupJava_The_Hutt_CW2/2_handover_pack/`

Developed for educational purposes; see `docs/decisions/licence-decision.md` for licensing and third-party notes.
