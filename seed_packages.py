import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsqaud_project.settings')
django.setup()

from devsqaud.models import Package, PackageFeature

def seed_packages():
    # Clear existing
    Package.objects.all().delete()
    
    # Starter
    starter = Package.objects.create(
        name='starter',
        display_name='MVP / Landing Page',
        icon='fas fa-paper-plane',
        price='$2,000',
        short_description='Perfect for startups looking to validate their idea with a high-performance landing page or MVP.',
        order=1
    )
    features = [
        'Single Page Application',
        'Custom UI/UX Design',
        'Responsive Layout',
        'Basic SEO Optimization',
        'Contact Form Integration',
        '1 Month Support'
    ]
    for f in features:
        PackageFeature.objects.create(package=starter, text=f)
        
    # Growth
    growth = Package.objects.create(
        name='growth',
        display_name='Professional Business',
        icon='fas fa-rocket',
        price='$8,000',
        short_description='Comprehensive solution for growing businesses needing custom functionality and scalability.',
        is_featured=True,
        order=2
    )
    features = [
        'Up to 10 Custom Pages',
        'Advanced Animations',
        'E-commerce Integration',
        'CMS Implementation',
        'Advanced SEO Strategy',
        '3 Months Priority Support',
        'Performance Optimization'
    ]
    for f in features:
        PackageFeature.objects.create(package=growth, text=f)
        
    # Enterprise
    enterprise = Package.objects.create(
        name='enterprise',
        display_name='Enterprise Solution',
        icon='fas fa-shield-alt',
        price='Custom',
        short_description='Full-scale platforms, SaaS products, and enterprise-grade systems with high security.',
        order=3
    )
    features = [
        'Custom SaaS Architecture',
        'AI/ML Integrations',
        'High-Security Protocols',
        'Unlimited Scalability',
        'Dedicated Project Manager',
        '24/7 Premium Support',
        'API First Development'
    ]
    for f in features:
        PackageFeature.objects.create(package=enterprise, text=f)

    print("Packages seeded successfully!")

if __name__ == '__main__':
    seed_packages()
