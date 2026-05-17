import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsqaud_project.settings')
django.setup()

from devsqaud.models import Project, Testimonial

print("Seeding projects...")

# Clean existing default projects if they are empty or few, and seed new ones
Project.objects.get_or_create(
    title="Apex Global E-Commerce Suite",
    defaults={
        'short_description': "An enterprise-grade headless e-commerce build delivering record-breaking checkout velocities.",
        'full_description': "Designed and deployed a customized decoupled storefront integrated with Stripe and AWS nodes.",
        'result_highlight': "+320% Checkout Velocity",
        'tech_stack': "React, Django, PostgreSQL, AWS, TailwindCSS",
        'is_featured': True
    }
)

Project.objects.get_or_create(
    title="Nova AI Marketing Analytics Platform",
    defaults={
        'short_description': "Automating client acquisition and predictive campaigns utilizing custom LLMs.",
        'full_description': "Integrated AI modules with real-time analytics dashboards for comprehensive customer segmentation.",
        'result_highlight': "4.8x Return on Ad Spend (ROAS)",
        'tech_stack': "Python, PyTorch, Django, Next.js, Redis",
        'is_featured': True
    }
)

Project.objects.get_or_create(
    title="CloudScale DevOps Automation",
    defaults={
        'short_description': "Full infrastructure orchestration migrating traditional servers to fully automated multi-cloud clusters.",
        'full_description': "Configured Kubernetes workloads to scale automatically on demand, cutting hosting costs by 45%.",
        'result_highlight': "99.99% Guaranteed Uptime",
        'tech_stack': "Docker, Kubernetes, AWS, Terraform, Ansible",
        'is_featured': False
    }
)

Project.objects.get_or_create(
    title="FitFlow Cross-Platform Mobile Suite",
    defaults={
        'short_description': "A modern fitness companion application boasting real-time telemetry syncing and cross-platform reliability.",
        'full_description': "Built with React Native to target iOS and Android simultaneously, delivering fluid 60fps animations.",
        'result_highlight': "125k+ Active Install Base",
        'tech_stack': "React Native, Node.js, Express, MongoDB",
        'is_featured': False
    }
)

Project.objects.get_or_create(
    title="SecureVault FinTech Gateway",
    defaults={
        'short_description': "High-security payment ledger processing secure transactions with multi-tenant encryption.",
        'full_description': "Engineered using cryptographic standards to guarantee transaction immutability and compliance.",
        'result_highlight': "PCI-DSS Level 1 Certified",
        'tech_stack': "Go, Django, PostgreSQL, HashiCorp Vault",
        'is_featured': False
    }
)

# Seed Testimonials
print("Seeding testimonials...")
Testimonial.objects.get_or_create(
    client_name="Zihad Rahman",
    defaults={
        'client_role': "CEO, MZ Web Studio Ltd",
        'feedback': "Antigravity redesigned our entire platform with incredible precision. The 3D UI, speed, and standard of engineering are absolutely world-class.",
        'is_featured': True,
        'order': 1
    }
)

Testimonial.objects.get_or_create(
    client_name="Sarah Jenkins",
    defaults={
        'client_role': "VP of Engineering, Apex Global",
        'feedback': "MZ Web Studio delivered our headless commerce site ahead of schedule. Our checkout velocity increased by 3.2x, leading to an immediate boost in conversions.",
        'is_featured': True,
        'order': 2
    }
)

Testimonial.objects.get_or_create(
    client_name="Marcus Vance",
    defaults={
        'client_role': "Product Director, Nova AI",
        'feedback': "Integrating their custom AI engine completely transformed our analytics product. We are now processing millions of data points with near-zero latency.",
        'is_featured': True,
        'order': 3
    }
)

print("Seeding complete successfully!")
