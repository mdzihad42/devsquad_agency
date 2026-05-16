import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsqaud_project.settings')
django.setup()

from devsqaud.models import FAQ

def seed_faqs():
    # Clear existing
    FAQ.objects.all().delete()
    
    faqs = [
        {
            'question': 'How long does a typical project take?',
            'answer': 'Project timelines vary based on complexity. A Starter MVP usually takes 4-6 weeks, while a more complex Growth-tier project can take 3-5 months.',
            'order': 1
        },
        {
            'question': 'What is your primary tech stack?',
            'answer': 'We specialize in modern, high-performance technologies. For web, we typically use React, Next.js, and Django. For mobile, we use React Native or Flutter.',
            'order': 2
        },
        {
            'question': 'Do you offer ongoing maintenance?',
            'answer': 'Yes, we provide post-launch support and maintenance packages to ensure your product stays secure, up-to-date, and high-performing.',
            'order': 3
        },
        {
            'question': 'Can you work with existing teams?',
            'answer': 'Absolutely. We can act as your primary technology partner or integrate with your in-house team to provide specialized expertise or extra bandwidth.',
            'order': 4
        },
        {
            'question': 'How do you handle project communication?',
            'answer': 'We use a combination of Slack for daily communication, Jira for task tracking, and weekly Zoom/Meet calls to keep everyone aligned.',
            'order': 5
        }
    ]
    
    for faq_data in faqs:
        FAQ.objects.create(**faq_data)

    print("FAQs seeded successfully!")

if __name__ == '__main__':
    seed_faqs()
