import os
from django.core.management.base import BaseCommand
from devsqaud.models import Service, Project, Testimonial, SiteConfig
from django.core.files import File

class Command(BaseCommand):
    help = 'Seeds the database with premium, SEO-optimized content'

    def handle(self, *args, **options):
        self.stdout.write('Seeding premium content...')

        # 1. Update Site Configuration
        config = SiteConfig.load()
        config.hero_headline = "We Build Scalable Digital Excellence"
        config.hero_subheading = "Transforming complex business challenges into high-performance web applications. Expert Django development, strategic UI/UX design, and cloud-native solutions."
        config.about_intro = "We are an elite team of Django experts and creative designers dedicated to building software that drives exponential growth."
        config.about_mission = "To empower ambitious businesses with scalable, secure, and conversion-focused digital products."
        config.about_vision = "To be the global benchmark for high-performance web development and strategic digital innovation."
        config.stat_projects = "120+"
        config.stat_experience = "8+ Years"
        config.stat_clients = "95% Retention"
        config.contact_email = "hello@devsquad.agency"
        config.footer_text = "© 2026 DevSquad Agency. Architecting the Digital Future."
        config.save()

        # 2. Clear and Seed Services
        Service.objects.all().delete()
        
        services_data = [
            {
                'title': 'Enterprise Web Development',
                'icon': 'fas fa-code',
                'image': 'services/web_dev.png',
                'short_description': 'Scalable, secure, and high-performance web applications built with Django and Python.',
                'full_description': 'We specialize in building robust enterprise-level applications that handle massive traffic and complex data workflows. Our Django-first approach ensures rapid development without compromising on security or scalability.',
                'problem': 'Legacy systems that are slow, insecure, and impossible to scale.',
                'solution': 'Modern, cloud-native architectures that provide 99.9% uptime and seamless user experiences.',
                'benefits': 'Unmatched Security\nLightning Fast Performance\nFuture-Proof Scalability',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Premium App Development',
                'icon': 'fas fa-mobile-alt',
                'image': 'services/app_dev.png',
                'short_description': 'Native and cross-platform mobile applications that deliver exceptional user experiences.',
                'full_description': 'From iOS to Android, we build mobile apps that are fast, intuitive, and designed to scale. Our mobile solutions focus on performance, accessibility, and seamless integration with your existing systems.',
                'problem': 'Clunky mobile experiences that drive users away.',
                'solution': 'High-performance native and Flutter-based apps with fluid animations and offline capabilities.',
                'benefits': 'Fluid User Experience\nCross-Platform Efficiency\nScalable Infrastructure',
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'Creative Graphics Design',
                'icon': 'fas fa-paint-brush',
                'image': 'services/graphics.png',
                'short_description': 'Strategic brand identity and visual storytelling that commands attention.',
                'full_description': 'We combine art and strategy to create visual identities that resonate with your audience. From logo design to marketing collateral, we ensure your brand looks premium across all touchpoints.',
                'problem': 'Generic branding that fails to stand out in a crowded market.',
                'solution': 'Modern, cohesive design systems that reflect your brand\'s elite status.',
                'benefits': 'Unique Brand Identity\nHigh-Impact Visuals\nConsistent Multi-Channel Design',
                'is_featured': True,
                'order': 3
            }
        ]

        for s in services_data:
            Service.objects.create(**s)

        # 3. Seed Projects (Mock Data)
        Project.objects.all().delete()
        projects_data = [
            {
                'title': 'FinTech Nexus Platform',
                'short_description': 'A high-frequency trading dashboard for a leading European financial firm.',
                'full_description': 'Built with Django and WebSockets for real-time data streaming. Integrated with multiple third-party APIs and secured with banking-grade encryption.',
                'result_highlight': '40% increase in trading efficiency',
                'tech_stack': 'Django, Redis, PostgreSQL, React, AWS',
                'is_featured': True
            },
            {
                'title': 'E-Com Pro Engine',
                'short_description': 'Headless e-commerce solution for a global fashion brand.',
                'full_description': 'A modular commerce engine designed for high-concurrency during flash sales. Featuring advanced inventory management and global CDN integration.',
                'result_highlight': '$2M+ revenue in first 30 days',
                'tech_stack': 'Django REST Framework, Next.js, Stripe, ElasticSearch',
                'is_featured': True
            }
        ]

        for p in projects_data:
            Project.objects.create(**p)

        self.stdout.write(self.style.SUCCESS('Successfully seeded premium content!'))
