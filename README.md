# Professional Personal Website

A comprehensive, professional personal website built with Django, featuring a modern design, responsive layout, and full functionality for both technical portfolio and public persona needs.

## 🚀 Features

### Core Functionality
- **Home Page**: Compelling landing page with professional photo, value proposition, and clear CTAs
- **About Page**: Detailed professional biography with skills, experience, and education
- **Portfolio**: Showcase of engineering projects with detailed project pages
- **Blog**: Technical and public-interest articles with Markdown support
- **Contact**: Professional contact form with email integration
- **Media Kit**: Downloadable assets and professional information for media

### Public Person Features
- **Speaking Engagements**: List of past and upcoming talks/events
- **Press Mentions**: Media coverage and interview highlights
- **Newsletter Signup**: Email collection with validation
- **Social Links**: Integrated social media presence

### Technical Features
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Performance Optimized**: Fast loading with optimized assets
- **SEO Ready**: Meta tags, structured data, and clean URLs
- **Docker Support**: Easy deployment with Docker and docker-compose
- **Admin Interface**: Full Django admin for content management
- **Email Integration**: Contact form and newsletter functionality

## 🛠 Technology Stack

- **Backend**: Django 5.1.1 (Latest LTS)
- **Frontend**: Tailwind CSS (No heavy JS frameworks)
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Styling**: Tailwind CSS with custom configuration
- **Deployment**: Docker & Docker Compose
- **Email**: Django's built-in email system
- **Static Files**: WhiteNoise for serving static files

## 📋 Prerequisites

- Python 3.11+
- Docker & Docker Compose (for containerized deployment)
- Git

## 🚀 Quick Start

### Option 1: Docker Deployment (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd personal-website
   ```

2. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

### Option 2: Local Development

1. **Clone and navigate to the project**
   ```bash
   git clone <repository-url>
   cd personal-website
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Populate initial data**
   ```bash
   python manage.py populate_data
   ```

8. **Start development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

## 📁 Project Structure

```
personal-website/
├── core/                    # Core app (home, about, contact)
│   ├── models.py           # Profile and ContactSubmission models
│   ├── views.py            # Core views
│   ├── forms.py            # Contact form with honeypot
│   └── management/         # Custom management commands
├── blog/                   # Blog app
│   ├── models.py           # BlogPost model
│   └── views.py            # Blog list and detail views
├── portfolio/              # Portfolio app
│   ├── models.py           # Project model
│   └── views.py            # Portfolio views
├── public_profile/         # Public profile app
│   ├── models.py           # Speaking, Press, Newsletter models
│   └── views.py            # Public profile views
├── templates/              # Django templates
│   ├── base.html           # Base template with Tailwind CSS
│   ├── core/               # Core page templates
│   ├── blog/               # Blog templates
│   ├── portfolio/          # Portfolio templates
│   └── public_profile/     # Public profile templates
├── static/                 # Static files
├── media/                  # User uploaded files
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
└── manage.py              # Django management script
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-app-password

# Database (for production)
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### Tailwind CSS Configuration

The project uses Tailwind CSS with a custom configuration that includes:

- **Primary Colors**: Blue-based color scheme
- **Secondary Colors**: Gray-based neutral colors
- **Typography**: Inter font family
- **Custom Components**: Gradient text, hero patterns, and custom utilities

## 📝 Content Management

### Admin Interface

Access the Django admin at `/admin/` to manage:

- **Profile Information**: Update personal details, bio, and social links
- **Blog Posts**: Create and manage blog content
- **Portfolio Projects**: Add and organize portfolio items
- **Speaking Engagements**: Manage speaking events and talks
- **Press Mentions**: Track media coverage and interviews
- **Newsletter Subscribers**: View and manage email subscribers
- **Contact Submissions**: Review contact form submissions

### Initial Data

The project includes a management command to populate initial data:

```bash
python manage.py populate_data
```

This creates:
- Sample profile information
- Example blog posts
- Portfolio projects
- Speaking engagements
- Press mentions
- Newsletter subscribers

## 🎨 Customization

### Design Customization

1. **Colors**: Modify the Tailwind configuration in `templates/base.html`
2. **Typography**: Update font families and sizes
3. **Layout**: Customize templates in the `templates/` directory
4. **Components**: Add new Tailwind components as needed

### Content Customization

1. **Profile**: Update the Profile model and admin interface
2. **Sections**: Modify views and templates for different content
3. **Forms**: Customize forms in the respective `forms.py` files
4. **Models**: Add new fields or models as needed

## 🚀 Deployment

### Production Deployment

1. **Set up production environment variables**
   ```env
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   SECRET_KEY=your-production-secret-key
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

2. **Use Docker Compose for production**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

3. **Set up reverse proxy** (Nginx recommended)
4. **Configure SSL certificates**
5. **Set up monitoring and logging**

### Static Files

For production, collect static files:

```bash
python manage.py collectstatic
```

## 🔧 Development

### Adding New Features

1. **Create new models** in the appropriate app
2. **Add views** for the new functionality
3. **Create templates** following the existing design patterns
4. **Update URLs** to include new routes
5. **Add admin interface** for content management

### Database Migrations

When making model changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Testing

Run the test suite:

```bash
python manage.py test
```

## 📊 Performance

The website is optimized for performance with:

- **Tailwind CSS**: Utility-first CSS for minimal bundle size
- **WhiteNoise**: Efficient static file serving
- **Database Optimization**: Proper indexing and query optimization
- **Caching**: Redis integration ready
- **CDN Ready**: Static files optimized for CDN delivery

## 🔒 Security

Security features include:

- **CSRF Protection**: Built-in Django CSRF protection
- **Honeypot**: Spam protection on contact forms
- **Input Validation**: Proper form validation and sanitization
- **SQL Injection Protection**: Django ORM prevents SQL injection
- **XSS Protection**: Template auto-escaping and content sanitization

## 📱 Responsive Design

The website is fully responsive with:

- **Mobile-First**: Designed for mobile devices first
- **Breakpoints**: Tailwind CSS responsive breakpoints
- **Touch-Friendly**: Optimized for touch interactions
- **Performance**: Optimized for mobile networks

## 🌐 SEO Features

SEO optimization includes:

- **Meta Tags**: Dynamic meta descriptions and titles
- **Structured Data**: Schema.org markup ready
- **Clean URLs**: SEO-friendly URL patterns
- **Sitemap**: Automatic sitemap generation
- **Open Graph**: Social media sharing optimization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:

- Create an issue in the repository
- Contact: alex@example.com
- Documentation: [Project Wiki](link-to-wiki)

## 🙏 Acknowledgments

- Django framework and community
- Tailwind CSS for the design system
- All contributors and supporters

---

**Built with ❤️ using Django and Tailwind CSS**