# AI Plezmo (Ashutosh Intelligence Plezmo) - Plezmo Support & Blog Platform

A Django-based web application that serves as a plezmo support and blog platform with user authentication, project showcase, and interactive features.

## 🚀 Features

- **User Authentication System**
  - User registration with email verification
  - Secure login/logout functionality
  - Password reset via email
  - Profile management with avatar generation

- **Blog Platform**
  - Create and publish blog posts
  - Comment system with nested replies
  - Post management (edit/delete)
  - User-specific content

- **Project Showcase**
  - Display personal projects and applications
  - Project request system
  - Admin panel for project management

- **Interactive Elements**
  - Dynamic avatar generation based on username
  - Responsive design with Bootstrap
  - AOS (Animate On Scroll) animations
  - SweetAlert notifications

## 🛠️ Tech Stack

- **Backend**: Django 3.2.3
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Email**: SMTP with Gmail integration
- **Static Files**: WhiteNoise for production
- **Icons**: Font Awesome, Simple Line Icons
- **Animations**: AOS (Animate On Scroll)

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Update the following in `plezmo/settings.py`:
   ```python
   EMAIL_HOST_USER = "your-email@gmail.com"
   EMAIL_HOST_PASSWORD = "your-app-password"
   SECRET_KEY = "your-secret-key"
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to view the application.

## 📁 Project Structure

```
project/
├── assets/                 # Static files (CSS, JS, images)
│   ├── admin/             # Django admin static files
│   ├── bootstrap/         # Bootstrap CSS
│   ├── css/              # Custom stylesheets
│   ├── fonts/            # Font files
│   ├── img/              # Images and avatars
│   └── js/               # JavaScript files
├── plezmo/               # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py
│   └── requirements.txt  # Python dependencies
├── plezmoapp/            # Main Django application
│   ├── migrations/       # Database migrations
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py
│   ├── models.py         # Database models
│   ├── tests.py
│   └── views.py          # View functions
├── templates/            # HTML templates
│   ├── registration/     # Password reset templates
│   ├── 404.html
│   ├── blog.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   └── template.html     # Base template
└── manage.py            # Django management script
```

## 🗄️ Database Models

- **user_data**: Extended user profile information
- **appdatabase**: Project/application showcase
- **requested_app**: User project requests
- **Post**: Blog posts
- **BlogComment**: Blog comments with threading
- **message**: Error reporting system

## 🔧 Configuration

### Email Settings
Configure SMTP settings in `settings.py` for email verification:
```python
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your-email@gmail.com"
EMAIL_HOST_PASSWORD = "your-app-password"
```

### Security Settings
The application includes security configurations:
- CSRF protection
- Secure cookies
- XSS protection
- Content type sniffing protection

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up proper database (PostgreSQL recommended)
4. Configure static file serving
5. Set up SSL certificates
6. Use environment variables for sensitive data

## 📱 Features Overview

### User Management
- Registration with email verification
- Automatic avatar generation based on username
- Profile customization
- Secure authentication

### Blog System
- Rich text blog posts
- Commenting system
- User-specific content management
- Post categorization via slugs

### Project Showcase
- Display personal projects
- Project request functionality
- Admin management interface

## 🎨 UI/UX Features

- Responsive design for all devices
- Dark theme with modern aesthetics
- Smooth animations and transitions
- Interactive elements with hover effects
- Toast notifications for user feedback

## 🔒 Security Features

- CSRF protection
- SQL injection prevention
- XSS protection
- Secure password handling
- Email verification system

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 👨‍💻 Author

**Ashutosh Kumar**
- GitHub: [@ashutosh-biotech](https://github.com/ashutosh-biotech/)

## 🐛 Bug Reports

If you find any bugs or issues, please report them through the application's built-in error reporting system or create an issue in the repository.

## ❗NOTE

If you ever thought of this project name AI mean Artificial Intelligence, you are wrong, this project was made before or the initial phase of AI, therefore this project is made by me sololy, without anyone or AI help.


## 📞 Support

For support and questions, please use the contact form available in the application or reach out through the provided social media links.
