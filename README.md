# LaptopLearning - Local Development Setup Guide

## Prerequisites
- Python 3.9+
- pip (Python package manager)
- Git

## Quick Start

### 1. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create .env File (for secrets)
```bash
# Create .env in project root
echo "SECRET_KEY=your-secret-key-here" > .env
echo "DEBUG=True" >> .env
echo "ALLOWED_HOSTS=localhost,127.0.0.1" >> .env
```

Or manually create `.env`:
```
SECRET_KEY=django-insecure-change-me-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### 6. Load Sample Data (Optional)
```bash
# Create a management command or load fixtures
# This will be added in next phase
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit: `http://localhost:8000`
Admin: `http://localhost:8000/admin`

## Directory Structure
```
intro_informatica/
├── config/                    # Django config (settings, urls, wsgi)
├── learning_app/              # Main app (models, views, forms)
│   ├── migrations/
│   ├── templatetags/
│   ├── models.py              # Data models
│   ├── views.py               # Views/logic
│   ├── urls.py                # Route definitions
│   ├── admin.py               # Admin customization
│   └── forms.py               # Django forms
├── templates/                 # HTML templates
│   ├── base.html              # Base template
│   └── learning/              # App-specific templates
├── static/                    # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── manage.py                  # Django CLI
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (not in git)
├── .gitignore                 # Git ignore rules
└── db.sqlite3                 # SQLite database (not in git)
```

## Project Features

### ✅ Implemented
- **Models**: Topic, Chapter, UserProfile, UserProgress, Badge
- **Auth**: User signup/login with Django built-in auth
- **Views**: Dashboard, topic list, chapter detail, profile
- **Templates**: Responsive Tailwind CSS design with gamified UI
- **Admin Panel**: Django Admin for CRUD operations
- **Gamification**: XP system, level calculation, progress tracking

### 🔄 Next Steps
- [ ] Implement Tailwind CSS compilation
- [ ] Add htmx for dynamic chapter completion
- [ ] Create sample Topics & Chapters via fixtures or management command
- [ ] Custom admin UI (optional)
- [ ] Email notifications (optional)
- [ ] Tests & documentation
- [ ] Deploy to production (Heroku, Fly.io, etc.)

## Admin Panel Usage

1. Go to `http://localhost:8000/admin`
2. Login with your superuser account
3. Create Topics (title, description, icon, order)
4. Create Chapters under Topics (content in HTML)
5. Manage users and view progress

## Adding Sample Data

### Via Admin Panel
1. Go to `/admin`
2. Click "Topics" → "Add Topic"
3. Fill in details, save
4. Click "Chapters" → "Add Chapter", assign to topic

### Via Django Shell (Optional)
```bash
python manage.py shell
```

```python
from learning_app.models import Topic, Chapter

# Create topic
topic = Topic.objects.create(
    title="Email Basics",
    description="Learn how to send and receive emails",
    order=1
)

# Create chapter
Chapter.objects.create(
    topic=topic,
    title="Setting up Email",
    content="<h2>Email Setup</h2><p>...</p>",
    estimated_time=15,
    xp_reward=100,
    order=1
)
```

## Troubleshooting

### Import Error: No module named 'django'
- Ensure venv is activated
- Run `pip install -r requirements.txt`

### Database Error
- Run `python manage.py migrate`

### Static files not loading
- Run `python manage.py collectstatic`

## Environment Variables (.env)
```
SECRET_KEY=<your-secret-key>       # Django secret (change in production!)
DEBUG=True/False                    # Debug mode (False in production)
ALLOWED_HOSTS=localhost,127.0.0.1  # Allowed domains
DATABASE_URL=<db-connection>        # Optional: for production DB
```

## Commands Reference

| Command | Purpose |
|---------|---------|
| `python manage.py runserver` | Start dev server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py makemigrations` | Create migration files from models |
| `python manage.py createsuperuser` | Create admin user |
| `python manage.py shell` | Interactive Python shell |
| `python manage.py collectstatic` | Collect static files for production |

## Next Development Phase

After scaffold is verified:
1. **Tailwind CSS Setup** — Configure Tailwind build pipeline
2. **Htmx Integration** — Add dynamic chapter completion without page reload
3. **Sample Data** — Create 2-3 sample topics with chapters
4. **Testing** — Unit & integration tests
5. **Deployment** — Deploy to cloud (Heroku / Fly.io / DigitalOcean)

---

**Questions?** Check Django docs: https://docs.djangoproject.com
