import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsqaud_project.settings')
django.setup()

from dashboard.models import SEOData

# Best SEO Data for a Digital Agency
seo_configs = [
    {
        'page_url': '/',
        'title_tag': 'Mzify — World-Class Digital Agency | Django & Web Solutions',
        'meta_description': 'Mzify is a premium digital agency specialized in building scalable, secure, and high-performance web applications using Django, WordPress, and React.',
        'keywords': 'digital agency, django web development, scalable web apps, ui/ux design, enterprise software, mzify agency'
    },
    {
        'page_url': '/services/',
        'title_tag': 'Premium Digital Services | Custom Web & Software Solutions — Mzify',
        'meta_description': 'Explore our wide range of digital services including custom web development, mobile apps, UI/UX design, and SEO-optimized digital marketing strategies.',
        'keywords': 'web design services, custom software development, digital products, software solutions for business'
    },
    {
        'page_url': '/portfolio/',
        'title_tag': 'Our Masterpieces | Featured Web Development Portfolio — Mzify',
        'meta_description': 'See how we have helped businesses scale with our featured projects and client success stories in web and mobile development.',
        'keywords': 'web development portfolio, case studies, agency work, software projects, creative agency portfolio'
    },
    {
        'page_url': '/about/',
        'title_tag': 'Meet the Experts | Our Journey & Mission — Mzify Agency',
        'meta_description': 'Learn about Mzify, our expert team of developers and designers dedicated to delivering world-class digital innovation and business growth.',
        'keywords': 'about mzify, expert developers team, software company culture, digital agency mission'
    },
    {
        'page_url': '/contact/',
        'title_tag': 'Start Your Project | Get a Free Consultation — Mzify',
        'meta_description': 'Ready to grow your business? Contact Mzify today for a 100% free consultation on your next web development or digital product journey.',
        'keywords': 'hire web developers, contact digital agency, start project, free software consultation'
    }
]

def populate_seo():
    print("Starting SEO Optimization...")
    for config in seo_configs:
        obj, created = SEOData.objects.update_or_create(
            page_url=config['page_url'],
            defaults={
                'title_tag': config['title_tag'],
                'meta_description': config['meta_description'],
                'keywords': config['keywords'],
                'og_title': config['title_tag'],
                'og_description': config['meta_description'],
            }
        )
        status = "Created" if created else "Updated"
        print(f"[{status}] SEO for {config['page_url']}")
    print("SEO Optimization Complete!")

if __name__ == '__main__':
    populate_seo()
