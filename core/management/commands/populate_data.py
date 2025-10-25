from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Profile
from blog.models import BlogPost
from portfolio.models import Project
from public_profile.models import SpeakingEngagement, PressMention, NewsletterSubscriber


class Command(BaseCommand):
    help = 'Populate the database with initial content'

    def handle(self, *args, **options):
        self.stdout.write('Creating initial content...')
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS('Superuser created: admin/admin123')
            )
        
        # Create profile
        profile, created = Profile.objects.get_or_create(
            name='Alex Johnson',
            defaults={
                'title': 'Senior Software Engineer & Public Speaker',
                'bio': '''I'm a passionate software engineer with over 8 years of experience building scalable web applications and leading technical teams. My journey in technology began with a curiosity about how things work, which led me to pursue computer science and eventually specialize in full-stack development.

Throughout my career, I've had the privilege of working with startups and Fortune 500 companies, always focused on creating solutions that make a real impact. I'm particularly passionate about Python, Django, and modern web technologies, and I love sharing knowledge through speaking engagements and technical writing.

Beyond coding, I'm an active member of the tech community, regularly speaking at conferences and meetups, and contributing to open source projects. I believe in the power of knowledge sharing and mentorship to help others grow in their careers.''',
                'short_bio': 'Passionate about technology, innovation, and sharing knowledge with the community through speaking engagements and technical writing.',
                'email': 'alex@example.com',
                'phone': '+1 (555) 123-4567',
                'location': 'San Francisco, CA',
                'github_url': 'https://github.com/alexjohnson',
                'linkedin_url': 'https://linkedin.com/in/alexjohnson',
                'twitter_url': 'https://twitter.com/alexjohnson',
                'youtube_url': 'https://youtube.com/@alexjohnson',
                'skills': 'Python, Django, React, JavaScript, AWS, Docker, PostgreSQL, Redis, Celery, Git, Linux, Agile, Leadership',
                'education': '''Master of Science in Computer Science
University of Technology, 2016-2018

Bachelor of Science in Software Engineering  
State University, 2012-2016''',
                'experience_years': 8,
                'meta_description': 'Senior Software Engineer and Public Speaker specializing in Django, Python, and modern web technologies. Available for speaking engagements and technical consulting.'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created profile: Alex Johnson'))
        
        # Create blog posts
        blog_posts = [
            {
                'title': 'Building Scalable Web Applications with Django',
                'content': '''# Building Scalable Web Applications with Django

In today's digital landscape, building web applications that can handle millions of users is crucial for success. Django, Python's most popular web framework, provides excellent tools for creating scalable applications.

## Key Principles for Scalability

### 1. Database Optimization
- Use database indexing strategically
- Implement query optimization
- Consider database sharding for large datasets
- Use connection pooling

### 2. Caching Strategies
- Implement Redis for session storage
- Use CDN for static assets
- Cache expensive database queries
- Implement page-level caching

### 3. Microservices Architecture
- Break down monolithic applications
- Use API gateways
- Implement service discovery
- Handle inter-service communication

### 4. Performance Monitoring
- Use APM tools like New Relic or DataDog
- Monitor database performance
- Track response times
- Set up alerting

## Django-Specific Optimizations

Django provides several built-in features for scalability:

- **Database connection pooling**: Use django-db-pool
- **Caching framework**: Built-in support for Redis and Memcached
- **Static file handling**: Use WhiteNoise or AWS S3
- **Database migrations**: Careful migration strategies for zero-downtime deployments

## Conclusion

Building scalable web applications requires careful planning and implementation. Django provides excellent tools, but success depends on understanding your application's specific needs and implementing the right strategies.

Remember: scalability is not just about handling more users—it's about maintaining performance, reliability, and user experience as your application grows.''',
                'excerpt': 'Exploring modern approaches to building web applications that can handle millions of users using Django and Python.',
                'tags': 'Django, Python, Web Development, Scalability, Performance',
                'published': True
            },
            {
                'title': 'The Future of AI in Software Development',
                'content': '''# The Future of AI in Software Development

Artificial Intelligence is transforming every industry, and software development is no exception. From code generation to automated testing, AI is reshaping how we build software.

## Current AI Applications in Development

### 1. Code Generation
Tools like GitHub Copilot and ChatGPT are helping developers write code faster and more efficiently. These AI assistants can:
- Generate boilerplate code
- Suggest function implementations
- Help with debugging
- Provide code explanations

### 2. Automated Testing
AI is revolutionizing software testing by:
- Generating test cases automatically
- Identifying edge cases
- Performing visual regression testing
- Optimizing test coverage

### 3. Code Review and Quality
AI-powered tools are improving code quality through:
- Automated code reviews
- Security vulnerability detection
- Performance optimization suggestions
- Code style enforcement

## The Impact on Developers

### Positive Changes
- **Increased Productivity**: Developers can focus on high-level problem solving
- **Reduced Repetitive Work**: AI handles mundane coding tasks
- **Better Code Quality**: AI helps catch bugs and improve code structure
- **Faster Learning**: AI can explain complex concepts and provide examples

### Challenges to Consider
- **Over-reliance on AI**: Developers might lose fundamental programming skills
- **Code Ownership**: Understanding AI-generated code becomes crucial
- **Security Concerns**: AI-generated code might introduce vulnerabilities
- **Job Market Changes**: Some traditional roles might evolve or disappear

## Preparing for the AI-Driven Future

### 1. Embrace AI Tools
- Learn to work effectively with AI assistants
- Understand their capabilities and limitations
- Develop prompt engineering skills
- Stay updated with new AI tools

### 2. Focus on High-Value Skills
- Problem-solving and system design
- Understanding business requirements
- Communication and collaboration
- Domain expertise

### 3. Maintain Core Programming Knowledge
- Understand algorithms and data structures
- Know how to debug and optimize code
- Learn multiple programming languages
- Understand software architecture principles

## Conclusion

AI is not replacing developers—it's augmenting their capabilities. The future belongs to developers who can effectively collaborate with AI tools while maintaining strong fundamental skills. 

The key is to embrace AI as a powerful tool while continuing to develop the critical thinking and problem-solving skills that make great developers.''',
                'excerpt': 'How artificial intelligence is transforming the way we write, test, and deploy code, and what it means for developers.',
                'tags': 'AI, Machine Learning, Software Development, Future Technology, Automation',
                'published': True
            }
        ]
        
        for post_data in blog_posts:
            post, created = BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults=post_data
            )
            if created:
                self.stdout.write(f'Created blog post: {post.title}')
        
        # Create portfolio projects
        projects = [
            {
                'title': 'E-Commerce Platform',
                'slug': 'ecommerce-platform',
                'description': '''A full-featured e-commerce platform built with Django and React. This project demonstrates modern web development practices including:

- **Backend**: Django REST Framework for API development
- **Frontend**: React with TypeScript for type safety
- **Database**: PostgreSQL with optimized queries
- **Authentication**: JWT-based authentication system
- **Payment**: Stripe integration for secure payments
- **Deployment**: Docker containers on AWS

The platform handles thousands of concurrent users and processes millions of transactions securely. It includes features like inventory management, order tracking, customer reviews, and analytics dashboard.

Key technical achievements:
- Implemented microservices architecture for scalability
- Achieved 99.9% uptime with proper monitoring
- Optimized database queries reducing response time by 60%
- Built comprehensive test suite with 95% code coverage''',
                'short_description': 'A scalable e-commerce platform built with Django and React, handling thousands of users and millions of transactions.',
                'technology_stack': 'Django, React, TypeScript, PostgreSQL, Redis, AWS, Docker, Stripe',
                'github_url': 'https://github.com/alexjohnson/ecommerce-platform',
                'live_url': 'https://ecommerce-demo.alexjohnson.com',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Real-Time Chat Application',
                'slug': 'realtime-chat-app',
                'description': '''A real-time chat application built with Django Channels and WebSockets. This project showcases real-time communication capabilities and modern web technologies.

Features include:
- **Real-time messaging**: Instant message delivery using WebSockets
- **User presence**: See who's online and typing
- **File sharing**: Upload and share images and documents
- **Group chats**: Create and manage group conversations
- **Message history**: Persistent chat history with search
- **Mobile responsive**: Works seamlessly on all devices

Technical implementation:
- Django Channels for WebSocket handling
- Redis for message queuing and caching
- Celery for background tasks
- PostgreSQL for data persistence
- Nginx for load balancing
- Docker for containerization

The application handles thousands of concurrent connections and delivers messages with sub-second latency.''',
                'short_description': 'A real-time chat application with WebSocket support, file sharing, and group messaging capabilities.',
                'technology_stack': 'Django Channels, WebSockets, Redis, Celery, PostgreSQL, Docker',
                'github_url': 'https://github.com/alexjohnson/chat-app',
                'live_url': 'https://chat-demo.alexjohnson.com',
                'featured': True,
                'order': 2
            },
            {
                'title': 'Data Analytics Dashboard',
                'slug': 'data-analytics-dashboard',
                'description': '''A comprehensive data analytics dashboard for business intelligence and reporting. This project demonstrates data visualization and analysis capabilities.

Key features:
- **Interactive charts**: Dynamic data visualization with Chart.js
- **Real-time updates**: Live data streaming and updates
- **Custom reports**: Generate and export custom reports
- **User management**: Role-based access control
- **API integration**: Connect to multiple data sources
- **Mobile support**: Responsive design for all devices

Technical stack:
- Django for backend API development
- Vue.js for frontend interactivity
- PostgreSQL for data storage
- Redis for caching and session management
- Celery for background data processing
- Docker for deployment

The dashboard processes millions of data points and provides insights to help businesses make data-driven decisions.''',
                'short_description': 'A comprehensive data analytics dashboard with interactive visualizations and real-time reporting capabilities.',
                'technology_stack': 'Django, Vue.js, PostgreSQL, Redis, Celery, Chart.js, Docker',
                'github_url': 'https://github.com/alexjohnson/analytics-dashboard',
                'live_url': 'https://analytics-demo.alexjohnson.com',
                'featured': True,
                'order': 3
            }
        ]
        
        for project_data in projects:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created project: {project.title}')
        
        # Create speaking engagements
        engagements = [
            {
                'title': 'Building Scalable Web Applications',
                'slug': 'building-scalable-web-applications',
                'description': 'A comprehensive talk about building web applications that can handle millions of users, covering architecture patterns, performance optimization, and best practices.',
                'event_date': '2024-03-15',
                'location': 'TechConf 2024, San Francisco',
                'event_type': 'conference',
                'slides_url': 'https://slides.alexjohnson.com/scalable-web-apps',
                'video_url': 'https://youtube.com/watch?v=scalable-web-apps',
                'event_url': 'https://techconf2024.com'
            },
            {
                'title': 'The Future of Web Development',
                'slug': 'future-of-web-development',
                'description': 'Exploring emerging technologies and trends in web development, including AI integration, WebAssembly, and modern frameworks.',
                'event_date': '2024-02-20',
                'location': 'WebDev Meetup, New York',
                'event_type': 'meetup',
                'slides_url': 'https://slides.alexjohnson.com/future-web-dev',
                'event_url': 'https://webdevmeetup.com'
            },
            {
                'title': 'Django Best Practices',
                'slug': 'django-best-practices',
                'description': 'A workshop covering Django best practices, from project structure to deployment strategies and performance optimization.',
                'event_date': '2024-01-10',
                'location': 'PyCon Workshop, Austin',
                'event_type': 'workshop',
                'slides_url': 'https://slides.alexjohnson.com/django-best-practices',
                'video_url': 'https://youtube.com/watch?v=django-workshop',
                'event_url': 'https://pycon.org'
            }
        ]
        
        for engagement_data in engagements:
            engagement, created = SpeakingEngagement.objects.get_or_create(
                title=engagement_data['title'],
                defaults=engagement_data
            )
            if created:
                self.stdout.write(f'Created speaking engagement: {engagement.title}')
        
        # Create press mentions
        mentions = [
            {
                'title': 'Tech Leader Discusses Future of Web Development',
                'publication': 'TechWeekly Magazine',
                'url': 'https://techweekly.com/interview-alex-johnson',
                'published_date': '2024-03-01',
                'description': 'An in-depth interview about emerging trends in web development and the role of AI in software engineering.'
            },
            {
                'title': 'Engineering Excellence: Building Scalable Systems',
                'publication': 'Developer Insights Podcast',
                'url': 'https://developerinsights.com/episode-45',
                'published_date': '2024-02-15',
                'description': 'A podcast episode discussing best practices for building scalable web applications and engineering leadership.'
            },
            {
                'title': 'Open Source Contributions Drive Innovation',
                'publication': 'Open Source Today',
                'url': 'https://opensourcetoday.com/contributor-spotlight',
                'published_date': '2024-01-20',
                'description': 'A feature article highlighting contributions to open source projects and the impact on the developer community.'
            }
        ]
        
        for mention_data in mentions:
            mention, created = PressMention.objects.get_or_create(
                title=mention_data['title'],
                defaults=mention_data
            )
            if created:
                self.stdout.write(f'Created press mention: {mention.title}')
        
        # Create sample newsletter subscribers
        subscribers = [
            'subscriber1@example.com',
            'subscriber2@example.com',
            'subscriber3@example.com'
        ]
        
        for email in subscribers:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={'active': True}
            )
            if created:
                self.stdout.write(f'Created newsletter subscriber: {email}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with initial content!')
        )








