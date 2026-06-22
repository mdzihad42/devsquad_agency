from django.core.management.base import BaseCommand
from devsqaud.models import Service, Project, Testimonial, SiteConfig


class Command(BaseCommand):
    help = 'Seed the database with initial demo data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...\n')

        # ---- Site Config ----
        config, created = SiteConfig.objects.get_or_create(pk=1, defaults={
            'hero_headline': 'We Build Scalable Digital Products',
            'hero_subheading': 'Transforming visionary ideas into high-performance digital experiences that accelerate growth, delight users, and dominate markets.',
            'about_intro': 'We are mzify — a collective of elite developers, designers, and strategists who believe great software is built at the intersection of art and engineering. Since our founding, we have partnered with startups and enterprises alike to ship products that matter.',
            'about_mission': 'To empower businesses with world-class digital solutions that are scalable, secure, and beautifully crafted. We obsess over every pixel and every line of code so our clients can focus on what they do best.',
            'about_vision': 'To become the most trusted digital partner for ambitious companies worldwide — known for shipping exceptional products on time, every time.',
            'stat_projects': '50+',
            'stat_experience': '3+',
            'stat_clients': '40+',
            'contact_email': 'hello@mzify.agency',
            'contact_phone': '+880 1234 567890',
            'whatsapp_number': '8801234567890',
            'footer_text': '© 2026 mzify. All rights reserved.',
            'social_facebook': 'https://facebook.com/mzify',
            'social_twitter': 'https://twitter.com/mzify',
            'social_linkedin': 'https://linkedin.com/company/mzify',
            'social_github': 'https://github.com/mzify',
        })
        if created:
            self.stdout.write(self.style.SUCCESS('[OK] SiteConfig created'))
        else:
            self.stdout.write('  SiteConfig already exists, skipping.')

        # ---- Services ----
        services_data = [
            {
                'icon': 'fas fa-code',
                'title': 'Web Development',
                'short_description': 'Custom web applications built with modern frameworks for maximum performance and scalability.',
                'full_description': 'We build fast, responsive, and scalable web applications using Python, Django, React, and Next.js. From MVPs to enterprise platforms, every project is architected for growth.',
                'problem': 'Many businesses struggle with slow, outdated websites that lose customers and revenue.',
                'solution': 'We engineer modern web platforms optimized for speed, SEO, and conversion — built to scale with your business.',
                'benefits': 'Lightning-fast load times\nSEO-optimized architecture\nScalable infrastructure\nClean, maintainable codebase',
                'is_featured': True,
                'order': 1,
            },
            {
                'icon': 'fas fa-mobile-alt',
                'title': 'Mobile App Development',
                'short_description': 'Native and cross-platform mobile apps that deliver seamless experiences on iOS and Android.',
                'full_description': 'We create mobile experiences that users love. Using React Native and Flutter, we build apps that feel native on every platform while sharing a single codebase for efficiency.',
                'problem': 'Building separate apps for iOS and Android is expensive and time-consuming.',
                'solution': 'Cross-platform development delivers native performance on both platforms from a single codebase, cutting costs by up to 40%.',
                'benefits': 'Single codebase, dual platforms\nNative-like performance\n40% cost reduction\nFaster time to market',
                'is_featured': True,
                'order': 2,
            },
            {
                'icon': 'fas fa-paint-brush',
                'title': 'UI/UX Design',
                'short_description': 'User-centered designs that look stunning and convert visitors into loyal customers.',
                'full_description': 'Great design is invisible — it just works. Our design team creates intuitive interfaces backed by user research, ensuring every interaction feels natural and every screen drives engagement.',
                'problem': 'Poor user experience leads to high bounce rates, abandoned carts, and frustrated users.',
                'solution': 'Data-driven UX design that reduces friction, increases engagement, and converts visitors into customers.',
                'benefits': 'Research-backed design decisions\nAccessible and inclusive interfaces\nDesign systems for consistency\nPrototyping and user testing',
                'is_featured': True,
                'order': 3,
            },
            {
                'icon': 'fas fa-cloud',
                'title': 'Cloud & DevOps',
                'short_description': 'Cloud infrastructure and CI/CD pipelines that keep your applications running at peak performance.',
                'full_description': 'We design and manage cloud infrastructure on AWS, GCP, and Azure. From containerization to automated deployments, we ensure your applications are always available, secure, and cost-efficient.',
                'problem': 'Managing servers and deployments manually wastes engineering time and introduces human error.',
                'solution': 'Automated cloud infrastructure with CI/CD pipelines, monitoring, and auto-scaling that runs itself.',
                'benefits': '99.9% uptime guarantee\nAutomated CI/CD pipelines\nCost-optimized infrastructure\n24/7 monitoring and alerts',
                'is_featured': True,
                'order': 4,
            },
            {
                'icon': 'fas fa-shopping-cart',
                'title': 'E-Commerce Solutions',
                'short_description': 'End-to-end e-commerce platforms built for high conversion and seamless checkout.',
                'full_description': 'We build custom e-commerce platforms with secure payment processing, inventory management, and conversion-optimized checkout flows. Every store is designed to maximize revenue.',
                'is_featured': False,
                'order': 5,
            },
            {
                'icon': 'fas fa-chart-bar',
                'title': 'Data & Analytics',
                'short_description': 'Turn your data into actionable insights with custom dashboards and analytics solutions.',
                'full_description': 'We build data pipelines, interactive dashboards, and analytics platforms that help you understand your users, optimize operations, and make data-driven decisions.',
                'is_featured': False,
                'order': 6,
            },
        ]

        for s in services_data:
            obj, created = Service.objects.get_or_create(
                title=s['title'],
                defaults=s
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  [OK] Service: {s["title"]}'))

        # ---- Projects ----
        projects_data = [
            {
                'title': 'FinTrack Pro Dashboard',
                'short_description': 'A real-time financial analytics dashboard for a leading fintech startup.',
                'full_description': 'FinTrack Pro needed a complete overhaul of their analytics platform. We rebuilt it from the ground up using React and Django REST Framework, implementing real-time WebSocket data feeds, interactive charts, and a role-based access system. The result: a platform that processes 10M+ transactions daily with sub-second response times.',
                'result_highlight': '10x faster data processing',
                'tech_stack': 'React, Django, PostgreSQL, WebSocket, Docker, AWS',
                'is_featured': True,
            },
            {
                'title': 'MedConnect Health App',
                'short_description': 'A telemedicine platform connecting patients with doctors seamlessly.',
                'full_description': 'We designed and built a comprehensive telemedicine platform featuring video consultations, appointment scheduling, secure medical records, and integrated payment processing. The app serves 50,000+ active users across iOS and Android with a 4.8-star rating.',
                'result_highlight': '50K+ active users',
                'tech_stack': 'React Native, Node.js, MongoDB, WebRTC, Stripe',
                'is_featured': True,
            },
            {
                'title': 'ShopVerse E-Commerce',
                'short_description': 'A high-performance e-commerce platform with 300% revenue increase.',
                'full_description': 'ShopVerse came to us with a slow, clunky online store. We redesigned the entire shopping experience with a focus on mobile-first design, one-click checkout, and personalized product recommendations powered by ML. Within 6 months, their revenue tripled.',
                'result_highlight': '300% revenue increase',
                'tech_stack': 'Next.js, Django, Redis, Elasticsearch, Stripe, GCP',
                'is_featured': True,
            },
        ]

        for p in projects_data:
            obj, created = Project.objects.get_or_create(
                title=p['title'],
                defaults=p
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  [OK] Project: {p["title"]}'))

        # ---- Testimonials ----
        testimonials_data = [
            {
                'client_name': 'Sarah Mitchell',
                'client_role': 'CEO, FinTrack Pro',
                'feedback': 'mzify transformed our entire analytics platform. The new dashboard is lightning fast and our team productivity has doubled. They delivered on time, on budget, and exceeded every expectation.',
                'is_featured': True,
                'order': 1,
            },
            {
                'client_name': 'James Rodriguez',
                'client_role': 'CTO, MedConnect',
                'feedback': 'Working with mzify felt like having an elite engineering team as part of our company. Their attention to detail, code quality, and design sensibility is unmatched. Highly recommended.',
                'is_featured': True,
                'order': 2,
            },
            {
                'client_name': 'Emily Chen',
                'client_role': 'Founder, ShopVerse',
                'feedback': 'Our revenue tripled within 6 months of launching the new platform. mzify didn\'t just build us a website — they built us a revenue machine. Best investment we\'ve ever made.',
                'is_featured': True,
                'order': 3,
            },
        ]

        for t in testimonials_data:
            obj, created = Testimonial.objects.get_or_create(
                client_name=t['client_name'],
                defaults=t
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  [OK] Testimonial: {t["client_name"]}'))

        self.stdout.write(self.style.SUCCESS('\n[DONE] Database seeded successfully!'))
