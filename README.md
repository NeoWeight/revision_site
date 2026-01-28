# Revision Goat

Revision Goat is a Django-based web application designed to support students and teachers with creating, managing, and reviewing revision cards.

The project was built to explore full-stack web development concepts including authentication, relational data modelling, and structured content delivery.

---

## Tech Stack
- **Python**
- **Django**
- **SQL**
- **Supabase** (database & authentication)
- HTML / CSS (Django templates)

---

## Key Features
- User authentication and account management
- Creation, editing, and organisation of revision cards and quizzes
- Structured data storage using a relational database
- Secure handling of environment variables
- Server-rendered web interface using Django templates

---

## Architecture Notes
- Uses Django apps to separate concerns (authentication, study features, forum)
- Revision resources are stored using relational models to support future expansion
- Environment variables are used to keep secrets and configuration out of source control

---

## Getting Started

### Prerequisites
- Python 3.10+
- Virtual environment (recommended)

### Installation
```bash
git clone https://github.com/NeoWeight/revision_site.git
cd revision-goat
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
