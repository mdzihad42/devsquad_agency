import os
import django

# Setup Django atmosphere
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsqaud_project.settings')
django.setup()

from devsqaud.models import Service, SiteConfig, Project, Testimonial

def update_data():
    print("Updating Mzify Data...")
    
    # 1. Update SiteConfig
    config = SiteConfig.load()
    config.hero_headline = "We Build Modern Websites & Web Applications That Grow Your Business"
    config.hero_subheading = "At Mzify, we create fast, secure and scalable websites and custom web applications tailored to your needs."
    config.contact_email = "info@mzify.org"
    config.contact_phone = "01608308665"
    config.whatsapp_number = "8801608308665"
    config.footer_text = "© 2026 Mzify. All rights reserved."
    config.save()
    print("- SiteConfig updated.")

    # 2. Update Services
    Service.objects.all().delete()
    
    services_data = [
        {
            'title': 'Business Websites',
            'icon': 'fas fa-globe',
            'short_description': 'Professional business websites to establish your online presence.',
            'full_description': 'We build high-converting business websites that reflect your brand identity and attract more customers. Our websites are fully responsive and optimized for all devices.',
            'order': 1,
            'is_featured': True
        },
        {
            'title': 'WordPress Development',
            'icon': 'fab fa-wordpress',
            'short_description': 'Custom WordPress websites using Elementor & more.',
            'full_description': 'From complex blog sites to e-commerce, we specialize in building highly customizable WordPress sites that are easy for you to manage.',
            'order': 2,
            'is_featured': True
        },
        {
            'title': 'Django Web Applications',
            'icon': 'fas fa-code',
            'short_description': 'Custom, secure and scalable web applications.',
            'full_description': 'Leverage the power of Python and Django to build robust, secure, and highly scalable web applications for your business processes.',
            'order': 3,
            'is_featured': True
        },
        {
            'title': 'API Development & Integration',
            'icon': 'fas fa-plug',
            'short_description': 'REST API development and third-party integration.',
            'full_description': 'We design and develop fast, secure REST APIs and integrate third-party services like payment gateways, social media, and more.',
            'order': 4,
            'is_featured': True
        },
        {
            'title': 'Admin Dashboard & Systems',
            'icon': 'fas fa-tachometer-alt',
            'short_description': 'Custom admin panels and management systems.',
            'full_description': 'Get custom-built internal tools, CRM systems, and admin dashboards to streamline your operations and manage your data efficiently.',
            'order': 5,
            'is_featured': True
        }
    ]
    
    for s in services_data:
        Service.objects.create(**s)
    print(f"- {len(services_data)} Services created.")

    # 3. Clean up old projects and testimonials if they mention mzify
    Testimonial.objects.all().delete()
    Project.objects.all().delete()
    print("- Old projects and testimonials cleared for a fresh start.")

if __name__ == "__main__":
    update_data()
